# Connection to mySQL
import mysql.connector

# Read file and run each line. If OK add to OK_file, else discard

fich = open("C:/_WORK/bactiva/IT-Academy/ex-database/scripts/ex2/6.sales.sql", "r")
for line in fich:
    print(line)

fich.close()