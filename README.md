# Log Analysis Project
log analysis project

#### Introduction
This project is under FSND. We need to analyse a fake news database. It is a PostgreSQL database.
This database has three major tables:
- authors : table that has information about authors
- articles : table that has information about all articles
- log : table that has all the ip addresses and article request statuses and other information.

#### Steps to run this application
1. Make sure you have postgresql installed and configured.
2. sudo apt-get install python2 or In windows just install python 2.
3. pip install psycopg2
4. clone the repo
5. To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
Here's what this command does:
psql — the PostgreSQL command line program
- -d news — connect to the database named news which has been set up for you
- -f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
6. run the file using python: python my_log_analysis.py
7. Go for it, psql -d news and explore the tables using the \dt and \d table commands and select statements.
8. Have fun!

#### Views Used
 Query for Question 3.
 It make use of two views, one to count the total number of requests
 and other to count total number of errors.
##### View 1: allreq
```sql
 create view allreq as
 select time ::timestamp::date, cast(count(*) as float) as requests
 from log
 group by time ::timestamp::date
 order by requests desc
 ```
##### View 2: err
```sql
 create view err as
 select time ::timestamp::date, cast(count(*) as float) as errors
 from log
 where status != '200 OK'
 group by time ::timestamp::date
 order by errors desc
 ```
 ###### Took references from fsnd forums.
