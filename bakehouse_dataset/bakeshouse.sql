CREATE SCHEMA IF NOT EXISTS bakehouse;

CREATE TABLE IF NOT EXISTS bakehouse.sales_suppliers AS
SELECT * FROM samples.bakehouse.media_customer_reviews;

CREATE TABLE IF NOT EXISTS bakehouse.sales_customers AS
SELECT * FROM samples.bakehouse.sales_customers;

CREATE TABLE IF NOT EXISTS bakehouse.sales_franchises AS
SELECT * FROM samples.bakehouse.sales_franchises;

CREATE TABLE IF NOT EXISTS bakehouse.sales_transactions AS
SELECT * FROM samples.bakehouse.sales_transactions;