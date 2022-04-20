-- create pysports_user and grant them all privileges to the pysports database
CREATE USER 'paul'@'localhost' IDENTIFIED WITH mysql_native_password BY 'BigBadWolfEater9/er';

-- grant all priveleges to the pysports database to user pysports_user on localhost
GRANT ALL PRIVILEGES ON pysports.* TO'root'@'localhost';

-- drop test user if exists
DROP USER IF EXISTS 'pysports_user'@'localhost';


-- create the team table
CREATE TABLE team(
	team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
);

-- create the player table and set the foreign key
CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);

-- insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Team Nebraska', 'Huskers');

-- drop tables if they are present
DROP TABLE IF EXISTS player;


