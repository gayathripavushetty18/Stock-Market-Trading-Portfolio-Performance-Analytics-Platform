CREATE OR REFRESH STREAMING TABLE bronze_stock_prices
AS
SELECT
  CAST(date AS DATE)        AS date,
  CAST(open AS DOUBLE)      AS open,
  CAST(high AS DOUBLE)      AS high,
  CAST(low AS DOUBLE)       AS low,
  CAST(close AS DOUBLE)     AS close,
  CAST(volume AS BIGINT)    AS volume,
  company,
  sector
FROM STREAM(
  read_files(
    '/Volumes/workspace/default/stock/raw/',
    format => 'csv',
    header => true
  )
);

CREATE OR REFRESH STREAMING TABLE bronze_portfolio_transactions
AS
SELECT
  CAST(transaction_date AS DATE) AS transaction_date,
  stock,
  transaction_type,
  CAST(quantity AS DOUBLE) AS quantity,
  CAST(price AS DOUBLE)    AS price
FROM STREAM(
  read_files(
    '/Volumes/workspace/default/stock/portfolio/',
    format => 'csv',
    header => true
  )
);

CREATE OR REFRESH MATERIALIZED VIEW silver_stock_prices
AS
SELECT
  date,
  open,
  high,
  low,
  close,
  volume,
  company,
  sector,
  (close - LAG(close) OVER (PARTITION BY company ORDER BY date)) /
   LAG(close) OVER (PARTITION BY company ORDER BY date) AS daily_return
FROM bronze_stock_prices
WHERE close IS NOT NULL;

CREATE OR REFRESH STREAMING TABLE silver_portfolio_transactions
AS
SELECT
  stock,
  transaction_type,
  quantity,
  price,
  transaction_date
FROM STREAM(bronze_portfolio_transactions)
WHERE quantity > 0
  AND price > 0
  AND transaction_date IS NOT NULL;

CREATE OR REFRESH MATERIALIZED VIEW gold_portfolio_metrics
AS
SELECT
  stock,
  SUM(quantity * price) AS total_investment
FROM silver_portfolio_transactions
GROUP BY stock;

CREATE OR REFRESH MATERIALIZED VIEW gold_portfolio_summary
AS
SELECT
  SUM(total_investment) AS total_portfolio_value,
  AVG(total_investment) AS avg_investment_per_stock
FROM gold_portfolio_metrics;

CREATE OR REFRESH MATERIALIZED VIEW gold_sector_allocation
AS
SELECT
  s.sector,
  SUM(p.quantity * p.price) AS sector_investment
FROM silver_portfolio_transactions p
JOIN silver_stock_prices s
  ON p.stock = s.company
GROUP BY s.sector;

CREATE OR REFRESH MATERIALIZED VIEW gold_stock_volatility
AS
SELECT
  company,
  AVG(daily_return) AS avg_daily_return,
  STDDEV(daily_return) AS volatility
FROM silver_stock_prices
GROUP BY company;
