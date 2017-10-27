import psycopg2

db = psycopg2.connect(database="news")
c = db.cursor()

# Query for Question 1.
print "What are the most popular three articles of all time?"
q1 = """select title, count(*) as views from articles, log
        where log.path like '%'||articles.slug
        group by articles.title, articles.author
        order by Views desc limit 3
    """

c.execute(q1)
res = c.fetchall()

for r in res:
    print r[0] + " - " + str(r[1]) + " views"


# Query for Question 2.
print "Who are the most popular article authors of all time?"
q2 = """ select name, count(*) as views from authors, articles, log
         where log.path like '%'||articles.slug and articles.author=authors.id
         group by articles.title, articles.author, authors.name
         order by views desc
     """

c.execute(q2)
res = c.fetchall()

for r in res:
    print r[0] + " - " + str(r[1]) + " views"

# Query for Question 3.
# It make use of two views, one to count the total number of requests
# and other to count total number of errors.
# View 1: allreq
# create view allreq as
# select time ::timestamp::date, cast(count(*) as float) as requests
# from log
# group by time ::timestamp::date
# order by requests desc
# View 2: err
# create view err as
# select time ::timestamp::date, cast(count(*) as float) as errors
# from log
# where status != '200 OK'
# group by time ::timestamp::date
# order by errors desc

print "On which days did more than 1 percent of requests lead to errors?"
q3 = """ select err.time, (err.errors*100/allreq.requests) as percent_err
         from err, allreq
         where (err.errors*100/allreq.requests)>1
     """

c.execute(q3)
res = c.fetchall()

for r in res:
    print "%s - %0.2f%%" % (r[0], r[1])

db.close()
