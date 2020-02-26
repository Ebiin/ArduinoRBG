import MySQLdb
import serial
import time

i=1

while i==1:
    try:
        db = MySQLdb.connect(host="leddb.cpd96oxpry4s.us-east-1.rds.amazonaws.com",
                             user="t8mios00", passwd="kahvia1234", db="ledDB")

    except:
        print("error while connecting to database")
    
    else:
        print("connected to database")
        i = 0

port = "/dev/ttyACM0"
baud = 9600

ser = serial.Serial(port, baud, timeout = 1)

colorR = 0
colorG = 0
colorB = 0

oldQueryId = 0
lastQueryId = 0

cur = db.cursor()

cur.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")

while True:
    oldQueryId = lastQueryId
    
    cur.execute("SELECT MAX(idcolor) FROM color")
    lastQueryId = str(cur.fetchall())
    lastQueryId = int(lastQueryId.replace("(", "").replace(",", "").replace(")", ""))
    
    if(oldQueryId != lastQueryId):
        cur.execute("SELECT varir FROM color ORDER BY idcolor DESC LIMIT 1")
        colorR = str(cur.fetchall())
        colorR = int(colorR.replace("(", "").replace(",", "").replace(")", ""))
        
        cur.execute("SELECT varig FROM color ORDER BY idcolor DESC LIMIT 1")
        colorG = str(cur.fetchall())
        colorG = int(colorG.replace("(", "").replace(",", "").replace(")", ""))
        
        cur.execute("SELECT varib FROM color ORDER BY idcolor DESC LIMIT 1")
        colorB = str(cur.fetchall())
        colorB = int(colorB.replace("(", "").replace(",", "").replace(")", ""))
        
        colorString = str(colorR) + " " + str(colorG) + " " + str(colorB) + "x" + "\r\n"
        
        print(colorString.encode())
        
        ser.write(colorString.encode())

    print("id: " + str(lastQueryId))
    print(ser.readline())
    
    time.sleep(1)

db.close()
ser.close()