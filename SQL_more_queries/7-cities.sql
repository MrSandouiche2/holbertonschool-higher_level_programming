-- creer la data si elle existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- va switch pour la bonne database
USE hbtn_0d_usa;

-- va creer la database pour la ville
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
