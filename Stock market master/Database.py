import pymysql
db = pymysql.connect("localhost","root","root","ticker" )
mycursor = db.cursor()
try:
    mycursor.execute("DROP TABLE Statistics")
except Exception as e:
    pass
try:
    mycursor.execute("CREATE TABLE Statistics(SNO VARCHAR(300),STAT_TICKER VARCHAR(300),MARKETCAP VARCHAR(300),ENTERPRISE_VALUE VARCHAR(300),RETURN_ON_ASSESTS VARCHAR(300),TOTAL_CASH VARCHAR(300),OPERATING_CASH_FLOW VARCHAR(300),LEVERED_FREE_CASH_FLOW VARCHAR(300),TOTAL_DEBT VARCHAR(300),CURRENT_RATIO VARCHAR(300),GROSS_PROFIT VARCHAR(300),PROFIT_MARGIN VARCHAR(300),PRIMARY KEY(STAT_TICKER))")
    print("Statistics table is created")
except Exception as e:
    pass

try:
    mycursor.execute("DROP TABLE Profiles")
except Exception as e:
    pass
try:
    mycursor.execute("CREATE TABLE Profiles( PROF_TICKER VARCHAR(300),NAME VARCHAR(300),ADDRESS VARCHAR(300),PHONENUM VARCHAR(300),WEBSITE VARCHAR(300),SECTOR VARCHAR(300),INDUSTRY VARCHAR(300),FULL_TIME VARCHAR(300),BUS_SUMM VARCHAR(300),PRIMARY KEY(PROF_TICKER))")
    print("Profiles table is created")
except Exception as e:
    pass

try:
    mycursor.execute("DROP TABLE Finances")
except Exception as e:
    pass
try:
    mycursor.execute("CREATE TABLE Finances( FIN_TICKER VARCHAR(300),TOTAL_REVENUE VARCHAR(300),COST_OF_REVENUE VARCHAR(300),INCOME_BEFORE_TAX VARCHAR(300),NET_INCOME VARCHAR(300),PRIMARY KEY(FIN_TICKER))")
    print("Finances table is created")
except Exception as e:
    pass

db.close()



