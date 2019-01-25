# The code sent to Todd 1/25/19 @1244


# Asymmetric Technologies, LLC
# Vehicle Data Logger
# https://python-obd.readthedocs.io/en/latest/  obd commands 

import csv
import datetime
import os.path
import time
import obd

print()  
print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))

def run():
   connection = obd.OBD()
   fileName = "car.csv"   # need to change name to "/Dev/ttyUSB0"? per Todd's instructions

   if not os.path.isfile(fileName):

      with open(fileName, "w") as f: # possibly add a
         f.write("Time Stamp,Speed kpm,RPM,Air Flow g/ps,Coolant Temp °C,Engine Load %,Run Time Sec,Bio Pressure,Intake Temp °C,Fuel Level %\n") # xxx

   dt = 0
   n = 0
   t = int(time.time())

   while True:
      try:
   #     open file for appending w+
         with open(fileName, "a") as f: # possibly add w
            values = []

            start = time.perf_counter()

            timeStamp = datetime.datetime.now()
            values.append(timeStamp)
            print('Timestamp: {:%Y-%m-%d %H:%M:%S}\n'.format(timeStamp))
            
            speed = getValue("Speed", connection, obd.commands.SPEED)
            values.append(speed)

            rpm = getValue("Rpm", connection, obd.commands.RPM)
            values.append(rpm)

            maf = getValue("Air Flow g/ps", connection, obd.commands.MAF)
            values.append(maf)

            degC = getValue("Coolant Temp °C", connection, obd.commands.COOLANT_TEMP)
            values.append(degC)

            Eload = getValue("Engine Load %", connection, obd.commands.ENGINE_LOAD)
            values.append(round(Eload, 2))
         #  values.append(Eload)

            runtm = getValue("Run Time Sec", connection, obd.commands.RUN_TIME)
            values.append(runtm)
   
            barp = getValue("Bio Pressure", connection, obd.commands.BAROMETRIC_PRESSURE)
            values.append(barp)

            DegI = getValue("Intake Temp °C", connection, obd.commands.INTAKE_TEMP)
            values.append(DegI)

            juice = getValue("Fuel Level", connection, obd.commands.FUEL_LEVEL)
            values.append(round(juice, 2))
         #  values.append(juice)

            f.write(",".join(str(value) for value in values) + "\n")

            dt += time.perf_counter() - start
            n += 1
            if int(time.time()) - t == 5:
               dt /= n
               print("\ndt = {}".format(dt))
               dt = 0
               n = 0
               t = int(time.time())
         time.sleep(0.05) # speed in which the request performs in seconds

# need to use tuples if doing multiple try exceptions
      except Exception as e:
     #   print(f'An exception occurred while running') #: {e}
         time.sleep(2)
         print('Restarting Connection')
         connection = obd.OBD()
         fileName = "car.csv"   # need to change name to "/Dev/ttyUSB0"? per Todd's instructions
         if not os.path.isfile(fileName):
            with open(fileName, "w") as f:
               f.write("Time Stamp,Speed kpm,RPM,Air Flow g/ps,Coolant Temp °C,Engine Load %,Run Time Sec,Bio Pressure,Intake Temp °C,Fuel Level %\n") # xxx
         dt = 0
         n = 0
         t = int(time.time())

def getValue(commandName, connection, cmd):
      print(commandName)         
      try:
         response = connection.query(cmd)
         print(response.value)
         value = response.value.magnitude
         return value
      except Exception as e:
         print("Error occured while reading {}: {}".format(commandName, e))
         return "Error"
      print()

def timeTest(): # testing speed
      connection = obd.OBD()
      start = time.perf_counter()
      for i in range(250): # 250
         response = connection.query(obd.commands.SPEED) # Speed can be set to other commands
         value = response.value.magnitude

      dt = (time.perf_counter() - start) / (250) # 250
      print("dt = {}".format(dt))

if __name__ == '__main__':
      run()
