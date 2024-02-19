-- Creates a MySQL server with:
--   Database hbnb_dev_test.
--   User hbnb_dev with password hbnb_dev_test in localhost.
--   Grants all privileges for hbnb_test on hbnb_test_db.
--   Grants SELECT privilege for hbnb_test on performance.

-- create the dtabase if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grants all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_test
GRANT SELECT ON performance_schema.* To 'hbnb_test'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
