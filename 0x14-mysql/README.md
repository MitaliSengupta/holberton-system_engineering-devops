# Creating Master Slave Databases

## Project information

-  At the end of this project the learnings:
   - What is the main role of a database
   - What is a database replica
   - What is the purpose of a database replica
   - Why database backups need to be stored in different physical locations
   - What operation should you regularly perform to make sure that your database backup strategy actually works

## Tasks

- Setup a Primary-Replica infrastructure using MySQL
  - Install and configure MySQL onweb-01 and web-02 so that they for a primary/replica (master/slave) cluster.
  - Having a replica member on for your MySQL database has 2 advantages:
    - Redundancy: if you lose one of the database servers, you will still have another working one and a copy of your data
    - Load distribution: you can split the read operations between the 2 servers, allowing to reduce the load on the primary member and improve query response speed
  - Requirements:
    - MySQL primary must be hosted on web-01 - do no use the bind-address, just comment this parameter
    - MySQL replica must be hosted on web-02
    - Setup replication for the MySQL database named holberton
    - Provide your MySQL primary configuration as answer file(my.cnf) with the name 0-mysql_configuration_primary
    - Provide your MySQL replica configuration as answer file with the name 0-mysql_configuration_replica
    - Create a MySQL user named holberton, password projectcorrection280hbtn with read access on replication status (the checker will use it to verify that replication is running fine)

- Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.
  - Requirements:
    - The MySQL dump must contain all your MySQL databases
    - The MySQL dump must be named backup.sql
    - The MySQL dump file has to be compressed to a tar.gz archive
    - This archive must have the following name format: day-month-year.tar.gz
    - The user to connect to the MySQL database must be root
    - The Bash script accepts one argument that is the password used to connect to the MySQL database