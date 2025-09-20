-- Insert data into FLIGHTS table
INSERT INTO flights (flight_id, origin, destination, departure_time, arrival_time, price) VALUES
(1, 'JFK', 'LAX', '2025-06-01 08:00:00', '2025-06-01 11:00:00', 350.00),
(2, 'LAX', 'JFK', '2025-06-01 12:00:00', '2025-06-01 20:00:00', 320.00),
(3, 'JFK', 'MIA', '2025-06-02 09:00:00', '2025-06-02 12:00:00', 250.00),
(4, 'MIA', 'JFK', '2025-06-02 13:00:00', '2025-06-02 16:00:00', 230.00),
(5, 'LAX', 'MIA', '2025-06-03 10:00:00', '2025-06-03 17:00:00', 400.00);


-- Insert data into HOTELS table
INSERT INTO hotels (hotel_id, name, location, price_per_night, rating) VALUES
(101, 'Hilton LAX', 'LAX', 150.00, 4.5),
(102, 'Marriott JFK', 'JFK', 180.00, 4.8),
(103, 'Hyatt Regency Miami', 'MIA', 120.00, 4.2),
(104, 'Embassy Suites LAX', 'LAX', 160.00, 4.4);


-- Insert data into BOOKINGS table
INSERT INTO bookings (booking_id, customer_name, type, item_id, booking_date) VALUES
(1001, 'Alice', 'flight', 1, '2025-05-20'),
(1002, 'Bob', 'hotel', 101, '2025-05-21'),
(1003, 'Charlie', 'flight', 3, '2025-05-22'),
(1004, 'David', 'hotel', 103, '2025-05-23'),
(1005, 'Alice', 'hotel', 102, '2025-05-23'),
(1006, 'Bob', 'flight', 2, '2025-05-24');
