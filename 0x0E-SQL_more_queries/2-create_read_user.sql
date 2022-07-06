-- Write a script that creates the database hbtn_0d_2 and user_0d_2.
-- Database
CREATE database IF NOT EXISTS hbtn_0d_2;
-- User
CREATE user IF	NOT EXISTS user_0d_2@localhost IDENTIFIED BY "user_02_2_pwd";
-- Grant privileges
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
