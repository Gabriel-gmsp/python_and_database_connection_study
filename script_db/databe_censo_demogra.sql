CREATE DATABASE IF NOT EXISTS censo_demogra;

USE censo_demogra;

CREATE TABLE IF NOT EXISTS data_censo_demogra (
	id TINYINT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	estado CHAR(2) NOT NULL,
	municipio VARCHAR(255) NOT NULL,
	area_territorial DOUBLE NOT NULL,
	dens_demogra DOUBLE NOT NULL
);

DESCRIBE data_censo_demogra ;