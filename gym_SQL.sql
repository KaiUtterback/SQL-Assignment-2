CREATE DATABASE IF NOT EXISTS gym_database;
USE gym_database;

CREATE TABLE IF NOT EXISTS Members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    trainer_id INT NOT NULL,
    FOREIGN KEY (trainer_id) REFERENCES Trainers(id)  -- Assuming you have a Trainers table
);

CREATE TABLE IF NOT EXISTS WorkoutSessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    date DATE,
    duration_minutes INT,
    calories_burned INT,
    FOREIGN KEY (member_id) REFERENCES Members(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Trainers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);


-- Sample Data


INSERT INTO Trainers (name) VALUES
('John Doe'), ('Jane Smith'), ('Alice Johnson'), ('Bob Brown'), ('Mary Davis');

INSERT INTO Members (name, age, trainer_id) VALUES
('Michael Scott', 45, CEIL(RAND() * 5)),
('Dwight Schrute', 39, CEIL(RAND() * 5)),
('Jim Halpert', 35, CEIL(RAND() * 5)),
('Pam Beesly', 34, CEIL(RAND() * 5)),
('Angela Martin', 38, CEIL(RAND() * 5));


INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES
(1, CURDATE() - INTERVAL FLOOR(RAND()*10) DAY, FLOOR(RAND()*120) + 30, FLOOR(RAND()*500) + 100),
(2, CURDATE() - INTERVAL FLOOR(RAND()*10) DAY, FLOOR(RAND()*120) + 30, FLOOR(RAND()*500) + 100),
(3, CURDATE() - INTERVAL FLOOR(RAND()*10) DAY, FLOOR(RAND()*120) + 30, FLOOR(RAND()*500) + 100),
(4, CURDATE() - INTERVAL FLOOR(RAND()*10) DAY, FLOOR(RAND()*120) + 30, FLOOR(RAND()*500) + 100),
(5, CURDATE() - INTERVAL FLOOR(RAND()*10) DAY, FLOOR(RAND()*120) + 30, FLOOR(RAND()*500) + 100);

-- View

SELECT * FROM Members;
SELECT * FROM WorkoutSessions;
SELECT * FROM Trainers;

-- Relationships

SELECT Members.id, Members.name, Members.age, Trainers.name AS trainer_name
FROM Members
JOIN Trainers ON Members.trainer_id = Trainers.id;


SELECT WorkoutSessions.id, Members.name AS member_name, WorkoutSessions.date, 
       WorkoutSessions.duration_minutes, WorkoutSessions.calories_burned
FROM WorkoutSessions
JOIN Members ON WorkoutSessions.member_id = Members.id;


SELECT DISTINCT Members.name
FROM Members
JOIN WorkoutSessions ON Members.id = WorkoutSessions.member_id
WHERE WorkoutSessions.date >= CURDATE() - INTERVAL 7 DAY;

