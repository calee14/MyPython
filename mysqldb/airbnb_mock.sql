
-- @block
/* 
primary key identifies a unique row and is auto created with
the auto increment keyword.
varchar is a string that has a max char length of 255.
text keyword can store string value of unspecified size.
*/
CREATE TABLE Users(
    id INT PRIMARY KEY AUTO_INCREMENT, 
    email VARCHAR(255) NOT NULL UNIQUE, 
    bio TEXT, 
    country VARCHAR(2));

-- @block
/*
insert many elements into the Users table at the specific values
*/
INSERT INTO Users(email, bio, country)
VALUES (
    'hello2@world.com',
    'i love stranger things!',
    'US'
),
(
    'hello3@world.com',
    'i love stranger things 2!',
    'UK'
);

-- @block
/*
add new rows to the table but only fill in the first 
two columns
*/
INSERT INTO Users(email, bio)
VALUES (
    'hello56@world.com',
    'i love stranger things!'
),
(
    'hello4@world.com',
    'i love stranger things 2!'
);

-- @block
-- SELECT * from Users;

-- SELECT id, email, country from Users;

-- SELECT email, id FROM Users LIMIT 2;

SELECT email, id, bio, country FROM Users 
-- 'where' keyword is good for filters
WHERE country = 'US'
-- use 'like' keyword to find patterns in data
-- the 'h%' means that find all emails with h as the first letter
AND email like 'h%'
ORDER BY id DESC 
LIMIT 2;


--@block
-- this will create an index on the email column of the users table.
-- increase look up times but waste more space and take longer 
-- to add data to the table.
CREATE INDEX email_index ON Users(email);

-- @block
CREATE TABLE Rooms(
    id INT AUTO_INCREMENT,
    street VARCHAR(255),
    owner_id INT NOT NULL,
    -- set the primary key of the row to 'id'
    -- this helps us identify rows using the correct id
    PRIMARY KEY (id),
    -- set the foreign key of the row to 'owner_id'
    -- this means that the column value of this table.
    -- will actually be pointing/ref another row in a diff
    -- table, in this case the Users table's 'id' column
    -- using the 'reference' keyword will mean that data can't 
    -- be deleted if there is a reference to that data/row
    FOREIGN KEY (owner_id) REFERENCES Users(id)
);

-- @block
INSERT INTO Rooms(owner_id, street)
VALUES
    (1, 'san diego sailboat'),
    (1, 'nantucket cottage'),
    (1, 'cabin in yosemite');

-- @block
-- selects all users but joins with another table and checks if 
-- they id's match, this is an example of INNER JOIN.
-- 
-- SELECT * FROM Users
-- INNER JOIN Rooms
-- ON Rooms.owner_id = Users.id;

-- selects all users but joins with another table and checks if 
-- they id's match, this is an example of LEFT JOIN.
-- or it also selects all of the rows from the left table which is Users
-- SELECT * FROM Users
-- LEFT JOIN Rooms
-- ON Rooms.owner_id = Users.id;

-- selects all users but joins with another table and checks if 
-- they id's match, this is an example of LEFT JOIN.
-- or it also selects all of the rows from the right table which is Rooms
SELECT Users.id AS user_id, Rooms.id AS room_id, email, street FROM Users
RIGHT JOIN Rooms
ON Rooms.owner_id = Users.id;

-- @block
CREATE TABLE Bookings(
    id INT AUTO_INCREMENT,
    guest_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in DATETIME,
    PRIMARY KEY (id),
    -- have two foriegn keys to reference the users table
    -- and reference the room table
    FOREIGN KEY (guest_id) REFERENCES Users(id),
    FOREIGN KEY (room_id) REFERENCES Rooms(id)
);

-- @block
-- select all bookings and join it with rooms
-- then list the rows where the bookings and rooms
-- have the same User id
SELECT 
    guest_id,
    street,
    check_in
FROM Bookings
INNER JOIN Rooms ON Rooms.owner_id = guest_id
WHERE guest_id = 1;

-- @block
DROP TABLE Users;
DROP DATABASE airbnb;
