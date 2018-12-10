# Asymmetric Technologies LLC, Blake Murphy
# 11/16/18--11/20/18--11/28/18--11/29/18--11/30/18
# 12/04/18--12/05/18--12/06/18--12/07/18--12/10/18

import obd
import time
import datetime
import csv

print()
print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))

def getSpeed():
    connection = obd.OBD()

    with open('car.csv', "a") as f:
        f.write("Speed kpm,RPM,Air Flow g/ps,Coolant Temp °C,Engine Load %,02 B1S1 volts,Run Time S,Bio Pressure, xxx,Intake Temp °C, Fuel Level\n") # xxx

    while True:

#       open file for appending w+
        with open('car.csv', "a") as f:
                values = []

                print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
 #              print("______________________________")
                print()

                cmd = obd.commands.SPEED # kph shown, can change to mph
                response = connection.query(cmd)
                print("Speed")
                print(response.value)
                speed = response.value.magnitude
                values.append("{0:.2f}".format(speed))
  #              try:
  #                 print("Functioning")
  #              except:
  #                 print("This is an error message for try catch")
                print()

                cmd = obd.commands.RPM # 4281.0 revolutions_per_minute 
                response = connection.query(cmd)
                print("RPM")
                print(response.value)
                rpm = response.value.magnitude
                values.append("{0:.2f}".format(rpm))
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.MAF # 196.68 gps grams per second
                response = connection.query(cmd)
                print("Air Flow Rate/ grams per second")
                print(response.value)
                gps = response.value.magnitude
                values.append("{0:.2f}".format(gps))
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.FUEL_PRESSURE # None
                response = connection.query(cmd)
                print("Fuel Pressure")
                print(response.value)
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.INTAKE_PRESSURE # not supported, none
                response = connection.query(cmd)
                print("Intake Pressure")
                print(response.value)
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()              

                cmd = obd.commands.COOLANT_TEMP # works -14 DegC
                response = connection.query(cmd)
                print("Coolant Temp °C")
                print(response.value)
                DegC = response.value.magnitude
                values.append("{0:.2f}".format(DegC))
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.PIDS_A # 10111110000110110011000000010011 bitarray
                response = connection.query(cmd)
                print("PIDS")        
                print(response.value)     
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.ENGINE_LOAD # 19.607843137254903 percent
                response = connection.query(cmd)
                print("Engine Load")
                print(response.value)
                Eload = response.value.magnitude
                values.append("{0:.2f}".format(Eload))
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.O2_SENSORS # ((), (False, False, False, False), (False, False, False, True))
                response = connection.query(cmd)
                print("O2 Sensors Boolean")
                print(response.value)
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.O2_B1S1 # 0.01 volt
                response = connection.query(cmd)
                print("Bank 1/Sensor 1 Voltage")        
                print(response.value)
                zvolt = response.value.magnitude
                values.append("{0:.2f}".format(zvolt))
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.THROTTLE_POS # none not supported 
                response = connection.query(cmd)
                print("Rel Throttle Pos")
                print(response.value)
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.WARMUPS_SINCE_DTC_CLEAR # None
                response = connection.query(cmd)
                print("Warm Since DTC Clear")
                print(response.value)
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.RUN_TIME # 600 seconds
                response = connection.query(cmd)
                print("Run Time/Seconds")        
                print(response.value)
                runtm = response.value.magnitude
                values.append("{0:.1f}".format(runtm))
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.TIME_SINCE_DTC_CLEARED # None
                response = connection.query(cmd)
                print("Time Since Codes Cleared")
                print(response.value)
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.BAROMETRIC_PRESSURE # 100 kilopascal
                response = connection.query(cmd)
                print("Barometric Pressure")
                print(response.value)
                barp = response.value.magnitude
                values.append("{0:.2f}".format(barp))
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.GET_CURRENT_DTC # []
                response = connection.query(cmd)
                print("Current DTC")
                print(response.value)
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.INTAKE_TEMP # 25 degC
                response = connection.query(cmd)
                print("Intake Temp °C")
                print(response.value)
                DegI = response.value.magnitude
                values.append("{0:.2f}".format(DegI))
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.FUEL_LEVEL # 50.19607843137255 percent 50.2 on chart
                response = connection.query(cmd)
                print("Fuel Level Input %")        
                print(response.value)
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                cmd = obd.commands.EVAP_VAPOR_PRESSURE # None
                response = connection.query(cmd)
                print("Evaporative System Vapor Pressure")
                print(response.value)
                try:
                   print("Functioning")
                except:
                   print("This is an error message for try catch")
                print()

                f.write(",".join(str(value) for value in values) + "\n")

        time.sleep(6)
        # 1 hour = 3600 seconds 
        # 1 day =  86400 seconds
        # Todd wants micro-seconds (0.05)

if __name__ == '__main__':
      getSpeed()