#SQL operations:

SQL--->Structured Query LAngauge--->followed by all the databses

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| digitalnest        |
| djangodb1          |
| djangodb2          |
| information_schema |
| mydb1              |
| mydb10             |
| mydb11             |
| mydb12             |
| mydb13             |
----------------------
#Creating our own database:
#Create database databasename

mysql> create database mydb14;


mysql> show databases;

+--------------------+
| Database           |
+--------------------+
| digitalnest        |
| djangodb1          |
| djangodb2          |
| information_schema |
| mydb1              |
| mydb10             |
| mydb11             |
| mydb12             |
| mydb13             |
| mydb14             |
----------------------

mysql> use mydb14;

#1.Creating a table in the database
mysql> create table emp(eid int,ename varchar(10),sal int,sex varchar(1),dno int,city varchar(10));

#2.Inserting data into the table
mysql> insert into emp values(101,'Miller',10000,'m',11,'pune'),(102,'Blake',20000,'m',12,'hyd'),(103,'Sony',30000,'f',11,'pune'),(104,'Sita',40000,'f',12,'hyd'),(105,'James',50000,'m',13,'hyd');

#3.Retrieving the data from the database table using select
mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | pune |
|  102 | Blake  | 20000 | m    |   12 | hyd  |
|  103 | Sony   | 30000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
|  105 | James  | 50000 | m    |   13 | hyd  |
+------+--------+-------+------+------+------+

#4. Retrieving specific columns

mysql> select ename,sal from emp;
+--------+-------+
| ename  | sal   |
+--------+-------+
| Miller | 10000 |
| Blake  | 20000 |
| Sony   | 30000 |
| Sita   | 40000 |
| James  | 50000 |
+--------+-------+

#----------------------------------------------------------------------------------------------
#CRUD Operations:
C-CREATE
R-READ
U-UPDATE
D-DELETE

#5. UPDATE:

mysql> update emp set sal=sal+5000 where ename="Blake";


mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | pune |
|  102 | Blake  | 25000 | m    |   12 | hyd  |
|  103 | Sony   | 30000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
|  105 | James  | 50000 | m    |   13 | hyd  |
+------+--------+-------+------+------+------+
#----------------------------------------------------------------------------------------------
#6. DEETE:

mysql> delete from emp where eid=105;

mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | pune |
|  102 | Blake  | 25000 | m    |   12 | hyd  |
|  103 | Sony   | 30000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
+------+--------+-------+------+------+------+

#Update the salaries of the emps belonging to dno=11 with 5000
mysql> update emp set sal=sal+5000 where dno=11;

mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 15000 | m    |   11 | pune |
|  102 | Blake  | 25000 | m    |   12 | hyd  |
|  103 | Sony   | 35000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
+------+--------+-------+------+------+------+

#----------------------------------------------------------------------------------------------
#7.Filtering data from a database table using where clause

#Filter those emps who belongs to the city "hyd"

mysql> select * from emp where city='hyd';
+------+-------+-------+------+------+------+
| eid  | ename | sal   | sex  | dno  | city |
+------+-------+-------+------+------+------+
|  102 | Blake | 25000 | m    |   12 | hyd  |
|  104 | Sita  | 40000 | f    |   12 | hyd  |
+------+-------+-------+------+------+------+

#ii. Filter only "male" emp recs

mysql> select * from emp where sex='m';
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 15000 | m    |   11 | pune |
|  102 | Blake  | 25000 | m    |   12 | hyd  |
+------+--------+-------+------+------+------+

#iii) Filter those emps whose sal>25000 and dno is 12

mysql> select * from emp where sal > 25000 and dno=12;
+------+-------+-------+------+------+------+
| eid  | ename | sal   | sex  | dno  | city |
+------+-------+-------+------+------+------+
|  104 | Sita  | 40000 | f    |   12 | hyd  |
+------+-------+-------+------+------+------+

#--------------------------------------------------------------------------------------------
#Groupings and Aggregations:
#Aggregated Functions---->sum(),avg(),max(),min(),count()
#Case1 : Single Grouping and Single Aggregation
#ex:
     m --->totsal
     f --->totsal
mysql> select sex,sum(sal) from emp group by sex;
+------+----------+
| sex  | sum(sal) |
+------+----------+
| m    |    40000 |
| f    |    75000 |
+------+----------+
2 rows in set (0.01 sec)

#ex:2
      11 ----->totsal
      12 ----->totsal

mysql> select dno,sum(sal) from emp group by dno;
+------+----------+
| dno  | sum(sal) |
+------+----------+
|   11 |    50000 |
|   12 |    65000 |
+------+----------+

#---------------------------------------------------------------------------------------------
#Case 2: Multi Grouping and single Aggregation

o/p:

11 m  totsal
11 f  totsal

12 m  totsal
12 f  totsal

mysql> select dno,sex,sum(sal) from emp group by dno,sex;
+------+------+----------+
| dno  | sex  | sum(sal) |
+------+------+----------+
|   11 | m    |    15000 |
|   12 | m    |    25000 |
|   11 | f    |    35000 |
|   12 | f    |    40000 |
+------+------+----------+
#----------------------------------------------------------------------------------------------
#Case 3: Single Grouping and Multiple Aggregations

o/p:
   11  totsal   avgsal  maxsal  minsal  count
   12    "        "       "        "      "

mysql> SELECT dno,sum(sal),avg(sal),min(sal),max(sal),count(*) from emp group by dno;

+------+----------+------------+----------+----------+----------+
| dno  | sum(sal) | avg(sal)   | min(sal) | max(sal) | count(*) |
+------+----------+------------+----------+----------+----------+
|   11 |    50000 | 25000.0000 |    15000 |    35000 |        2 |
|   12 |    65000 | 32500.0000 |    25000 |    40000 |        2 |
+------+----------+------------+----------+----------+----------+

#---------------------------------------------------------------------------------------------
#Case 4: Multi Grouping and Multiple Aggregations

o/p:
   11  m totsal   avgsal  maxsal  minsal  count
   11  F   "        "       "        "
   12  m totsal   avgsal  maxsal  minsal  count
   12  F   "        "       "        " 


mysql> SELECT dno,sex,sum(sal),avg(sal),min(sal),max(sal),count(*) from emp group by dno,sex;
+------+------+----------+------------+----------+----------+----------+
| dno  | sex  | sum(sal) | avg(sal)   | min(sal) | max(sal) | count(*) |
+------+------+----------+------------+----------+----------+----------+
|   11 | m    |    15000 | 15000.0000 |    15000 |    15000 |        1 |
|   12 | m    |    25000 | 25000.0000 |    25000 |    25000 |        1 |
|   11 | f    |    35000 | 35000.0000 |    35000 |    35000 |        1 |
|   12 | f    |    40000 | 40000.0000 |    40000 |    40000 |        1 |
+------+------+----------+------------+----------+----------+----------+

#----------------------------------------------------------------------------------------------
#Creating a table from another table

mysql> create table emp2 like emp;  #Here we get only the table structure but not the data

mysql> select * from emp2;
Empty set (0.00 sec)
  
#describe---->To see the table structure
mysql> describe emp2;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| eid   | int         | YES  |     | NULL    |       |
| ename | varchar(10) | YES  |     | NULL    |       |
| sal   | int         | YES  |     | NULL    |       |
| sex   | varchar(1)  | YES  |     | NULL    |       |
| dno   | int         | YES  |     | NULL    |       |
| city  | varchar(10) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+

#---------------------------------------------------------------------------------------------
#Inserting data from one table to another table

mysql> insert into emp2 select * from emp;

mysql> select * from emp2;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 15000 | m    |   11 | pune |
|  102 | Blake  | 25000 | m    |   12 | hyd  |
|  103 | Sony   | 35000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
+------+--------+-------+------+------+------+

#----------------------------------------------------------------------------------------------
#Table to table copy
#CTAS --> CREATE - TABLE -AS -SELECT

mysql> create table emp3 as select * from emp;

mysql> select * from emp3;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 15000 | m    |   11 | pune |
|  102 | Blake  | 25000 | m    |   12 | hyd  |
|  103 | Sony   | 35000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
+------+--------+-------+------+------+------+
#----------------------------------------------------------------------------------------------
#Merging the tables:

mysql> create table empres as select * from emp2 union all select * from emp3;

mysql> select * from empres;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 15000 | m    |   11 | pune |
|  102 | Blake  | 25000 | m    |   12 | hyd  |
|  103 | Sony   | 35000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
|  101 | Miller | 15000 | m    |   11 | pune |
|  102 | Blake  | 25000 | m    |   12 | hyd  |
|  103 | Sony   | 35000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
+------+--------+-------+------+------+------+

#Q) If one emp table has 6 columns and the other table has 4 columns,
#    is merging possible....??

mysql> create table emp4(eid int,ename varchar(10),sal int,sex varchar(1));

mysql> insert into emp4 values (101,'George',50000,'m'),(102,'Kohli',70000,'m');


mysql> select * from emp4;
+------+--------+-------+------+
| eid  | ename  | sal   | sex  |
+------+--------+-------+------+
|  101 | George | 50000 | m    |
|  102 | Kohli  | 70000 | m    |
+------+--------+-------+------+

now merge emp3 and emp4---->here merging is not possible as they have
different columns, so neutralize the schema

#-----------------------------------------------------------------------------------
#Adding  2 additional columns to emp4 table using alter command

#alter:
 #i.adding columns
 #syntax:
  alter table tablename
  add columnname1 datatype,
  add columnname2 datatype,
  .
  .
  add columnnamen datatype;

mysql> alter table emp4
    -> add dno int,
    -> add city varchar(10);

mysql> select * from emp4;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | George | 50000 | m    | NULL | NULL |
|  102 | Kohli  | 70000 | m    | NULL | NULL |
+------+--------+-------+------+------+------+

#Now merging the tables

mysql> create table empres2 as select * from emp3 union all select * from emp4;

mysql> select * from empres2;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 15000 | m    |   11 | pune |
|  102 | Blake  | 25000 | m    |   12 | hyd  |
|  103 | Sony   | 35000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
|  101 | George | 50000 | m    | NULL | NULL |
|  102 | Kohli  | 70000 | m    | NULL | NULL |
+------+--------+-------+------+------+------+


mysql> create table empres4 as select * from emp3 union all select eid,ename,sal,
       sex,0 as dno,'xxxx' as city from emp4;


mysql> select * from empres4;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 15000 | m    |   11 | pune |
|  102 | Blake  | 25000 | m    |   12 | hyd  |
|  103 | Sony   | 35000 | f    |   11 | pune |
|  104 | Sita   | 40000 | f    |   12 | hyd  |
|  101 | George | 50000 | m    |    0 | xxxx |
|  102 | Kohli  | 70000 | m    |    0 | xxxx |
+------+--------+-------+------+------+------+  

#----------------------------------------------------------------------------------
#alter:

#i.adding columns
add 2 columns---->dname and desig to the emp table

mysql> alter table emp
    -> add dname varchar(10),
    -> add desig varchar(10);

mysql> select * from emp;
+------+--------+-------+------+------+------+-------+-------+
| eid  | ename  | sal   | sex  | dno  | city | dname | desig |
+------+--------+-------+------+------+------+-------+-------+
|  101 | Miller | 15000 | m    |   11 | pune | NULL  | NULL  |
|  102 | Blake  | 25000 | m    |   12 | hyd  | NULL  | NULL  |
|  103 | Sony   | 35000 | f    |   11 | pune | NULL  | NULL  |
|  104 | Sita   | 40000 | f    |   12 | hyd  | NULL  | NULL  |
+------+--------+-------+------+------+------+-------+-------+

#ii. Renaming the columns----->'sex' to 'Gender'
                               'sal' to 'income'

#syntax:
 alter table tablename
 change oldcolumnname newcolumnname datatype;

mysql> alter table emp
    -> change sex Gender varchar(1),
    -> change sal Income int;

mysql> select * from emp;
+------+--------+--------+--------+------+------+-------+-------+
| eid  | ename  | Income | Gender | dno  | city | dname | desig |
+------+--------+--------+--------+------+------+-------+-------+
|  101 | Miller |  15000 | m      |   11 | pune | NULL  | SE    |
|  102 | Blake  |  25000 | m      |   12 | hyd  | NULL  | NULL  |
|  103 | Sony   |  35000 | f      |   11 | pune | NULL  | SE    |
|  104 | Sita   |  40000 | f      |   12 | hyd  | NULL  | NULL  |
+------+--------+--------+--------+------+------+-------+-------+

#iii) dropping a column
#syntax:
       alter table tablename
       drop column columnname;

mysql> alter table emp
    -> drop column dname;

mysql> select * from emp;
+------+--------+--------+--------+------+------+-------+
| eid  | ename  | Income | Gender | dno  | city | desig |
+------+--------+--------+--------+------+------+-------+
|  101 | Miller |  15000 | m      |   11 | pune | SE    |
|  102 | Blake  |  25000 | m      |   12 | hyd  | NULL  |
|  103 | Sony   |  35000 | f      |   11 | pune | SE    |
|  104 | Sita   |  40000 | f      |   12 | hyd  | NULL  |
+------+--------+--------+--------+------+------+-------+

#iv) altering or renaming the tablename
mysql> alter table emp
    -> rename to emps;

mysql> select * from emp;
ERROR 1146 (42S02): Table 'mydb14.emp' doesn't exist
mysql> select * from emps;
+------+--------+--------+--------+------+------+-------+
| eid  | ename  | Income | Gender | dno  | city | desig |
+------+--------+--------+--------+------+------+-------+
|  101 | Miller |  15000 | m      |   11 | pune | SE    |
|  102 | Blake  |  25000 | m      |   12 | hyd  | NULL  |
|  103 | Sony   |  35000 | f      |   11 | pune | SE    |
|  104 | Sita   |  40000 | f      |   12 | hyd  | NULL  |
+------+--------+--------+--------+------+------+-------+

















 








