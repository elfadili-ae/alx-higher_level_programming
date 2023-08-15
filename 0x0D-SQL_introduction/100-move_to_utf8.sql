-- convert table to utf8
USE hbtn_0c_0
ALTER TABLE second_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
