# lap
log analysis

#### Introduction
This project is under FSND. We need to analyse a news database.

#### Steps to run this application
1. Make sure you have postgresql installed and configured.
2. install python
3. install psycopg2
4. clone the repo
5. run the file using python.
6. Go for it.

#### Views Used
 Query for Question 3.
 It make use of two views, one to count the total number of requests
 and other to count total number of errors.
##### View 1: allreq
 create view allreq as
 select time ::timestamp::date, cast(count(*) as float) as requests
 from log
 group by time ::timestamp::date
 order by requests desc
##### View 2: err
 create view err as
 select time ::timestamp::date, cast(count(*) as float) as errors
 from log
 where status != '200 OK'
 group by time ::timestamp::date
 order by errors desc
 
 ###### Took references from fsnd forums.
