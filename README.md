1. install docker
2. navigate to directory and git pull this repo there
3. docker build -t green .
4. docker run -p 5000:5000 green


database connection:
install postgresql-client

psql -W -U sgpostgres -p 5432 -h SG-task-1109-pgsql-master.servers.mongodirector.com -d postgres

username password in https://console.scalegrid.io/postgresqlclusters/1109/clusterDetails
to test entries in table, once logged in then type:
 '''
 /c green
  SELECT * from products;
'''
