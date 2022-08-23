
-- @block
CREATE TABLE coffee_table (
    id INT,
    name VARCHAR(255),
    region VARCHAR(255),
    roast VARCHAR(255)
);

-- @block
DESCRIBE coffee_table;

-- @block
INSERT INTO coffee_table VALUES 
    (2, "default", "ethiopia", "light"),
    (3, "black", "USA", "hard"),
    (4, "brown", "CHINA", "heavy"),
    (5, "creamy", "INDIA", "light"),
    (6, "default", "PENIS", "light");

-- @block
SELECT * FROM coffee_table;
-- @block
SELECT * FROM coffee_table
WHERE name = "default"
OR region = "usa";

-- @block
DELETE FROM coffee_table
WHERE region = "china" LIMIT 1;

-- @block
UPDATE coffee_table 
SET roast = 'dark' 
WHERE name = 'DEFAULT';

-- @block
SELECT * FROM coffee_table
ORDER BY region DESC;

-- @block
ALTER TABLE coffee_table
ADD COST FLOAT;

