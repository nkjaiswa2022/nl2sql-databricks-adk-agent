CREATE TABLE IF NOT EXISTS flights (
    flight_id INT,
    origin STRING,
    destination STRING,
    departure_time TIMESTAMP,
    arrival_time TIMESTAMP,
    price DOUBLE
);

-- 2. Create HOTELS table
-- Using DOUBLE for price and rating, and STRING for location/name.
CREATE TABLE IF NOT EXISTS hotels (
    hotel_id INT,
    name STRING,
    location STRING,
    price_per_night DOUBLE,
    rating DOUBLE
);

-- 3. Create BOOKINGS table
-- Using DATE for booking_date and STRING for the type column.
-- Note: Spark/Databricks SQL typically does not enforce CHECK constraints.
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INT,
    customer_name STRING,
    type STRING, -- Expected values: 'flight' or 'hotel'
    item_id INT,
    booking_date DATE
);
