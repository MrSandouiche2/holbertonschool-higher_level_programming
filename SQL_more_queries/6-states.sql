-- creer la database (dans le doute ou ça existe pas)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- change pour la nouvelle databaase
USE hbtn_0d_usa;

-- crrere la table si elle n'existe pas
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
