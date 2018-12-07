# 11/16/18--11/20/18--11/28/18--11/29/18--11/30/18
# 12/04/18--12/05/18--12/06/18--12/07/18--

import obd
import time
# import datetime
# print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))


def getSpeed():
    connection = obd.OBD()

    with open('car.csv', "w") as f:
        f.write("Speed kpm,RPM,Air Flow g/ps,Coolant Temp °C,Engine Load %,02 B1S1 volts,Run Time S,Bio Pressure,Intake Temp °C\n") # xxx

    while True:


#       open file for appending w+
        with open('car.csv', "a") as f:
                values = []

                cmd = obd.commands.SPEED # kph shown, can change to mph
                response = connection.query(cmd)
             #  if response.unit traceback
                print(1)
                print(response.value)
             #  print(response.value("mph"))
                speed = response.value.magnitude
                values.append("{0:.2f}".format(speed))

                try:
                   print("Hello Error City")
                except:
                   print("This is an error message for try catch")

                cmd = obd.commands.RPM # 4281.0 revolutions_per_minute 
                response = connection.query(cmd)
                print(2)
                print(response.value)
                rpm = response.value.magnitude
                values.append("{0:.2f}".format(rpm))

                cmd = obd.commands.MAF # 196.68 gps grams per second
                response = connection.query(cmd)
                print(3)
                print(response.value)
                gps = response.value.magnitude
                values.append("{0:.2f}".format(gps))

                cmd = obd.commands.STATUS # not supported
                response = connection.query(cmd)
                print(4)
                print(response.value)
             #  values.append(response.value)
             #  zzz = response.value.magnitude
             #  values.append("{0:.2f}".format(zzz))
             #  needs to be a special

                cmd = obd.commands.FUEL_PRESSURE # None
                response = connection.query(cmd)
                print(5)
                print(response.value)
             #  values.append(response.value)
             #  zzz = response.value.magnitude
             #  values.append("{0:.2f}".format(zzz))
             #  comes out as a kilopascal           

             #  cmd = obd.commands.xxx # none
             #  response = connection.query(cmd)
             #  print(6)        
             #  print(response.value)

                cmd = obd.commands.FUEL_STATUS # not working, because no engine temp. Open loop/closed loop
                response = connection.query(cmd)
                print(7)
                print(response.value)
             #  zoom = response.value.magnitude
             #  values.append("{0:.2f}".format(zoom))
             #  needs to be a string

                cmd = obd.commands.INTAKE_PRESSURE # not supported, none
                response = connection.query(cmd)
                print(8)
                print(response.value)
             #  zzz = response.value.magnitude
             #  values.append("{0:.2f}".format(zzz))
             #  comes out as a kilopascal

                cmd = obd.commands.COOLANT_TEMP # works -14 DegC
                response = connection.query(cmd)
                print(9)
                print(response.value)
                DegC = response.value.magnitude
                values.append("{0:.2f}".format(DegC))
             #  zzz = response.value.magnitude
             #  values.append("{0:.2f}".format(zzz))
             #  convert C to F

                cmd = obd.commands.PIDS_A # 10111110000110110011000000010011 bitarray
                response = connection.query(cmd)
                print(10)        
                print(response.value)
             #  pid = response.value.magnitude
             #  values.append("{2**200}".format(pid))
             #  needs to be a bitarray
                
                cmd = obd.commands.ENGINE_LOAD # 19.607843137254903 percent
                response = connection.query(cmd)
                print(11)
                print(response.value)
                Eload = response.value.magnitude
                values.append("{0:.2f}".format(Eload))
             #  comes out as a percentage 

                cmd = obd.commands.O2_SENSORS # ((), (False, False, False, False), (False, False, False, True))
                response = connection.query(cmd)
                print(13)
                print(response.value)
             #  senb = response.value.magnitude
             #  values.append("{true}".format(senb))
             #  needs to be a boolean

                cmd = obd.commands.O2_B1S1 # 0.01 volt
                response = connection.query(cmd)
                print(14)        
                print(response.value)
                zvolt = response.value.magnitude
                values.append("{0:.2f}".format(zvolt))

              # cmd = obd.commands.xxx # none
              # response = connection.query(cmd)
              # print(16)
              # print(response.value)
              # cmd = obd.commands.xxx # none 
              # response = connection.query(cmd)
              # print(17)
              # print(response.value)

                cmd = obd.commands.OIL_TEMP # none not supported
                response = connection.query(cmd)
                print(18)        
                print(response.value)
             #  oilt = response.value.magnitude
             #  values.append("{0:.2f}".format(oilt))
             #  comes out as a celsius

                cmd = obd.commands.FUEL_RATE # none not supported
                response = connection.query(cmd)
                print(19)
                print(response.value)
                # zzz = response.value.magnitude
                # values.append("{0:.2f}".format(zzz))
                # comes out as a liter per hour

                cmd = obd.commands.FUEL_INJECT_TIMING # none not supported
                response = connection.query(cmd)
                print(20)
                print(response.value)
               # zzz = response.value.magnitude
               # values.append("{0:.2f}".format(zzz))
               # comes out as a degree

                cmd = obd.commands.DISTANCE_SINCE_DTC_CLEAR # none not supported
                response = connection.query(cmd)
                print(21)
                print(response.value)
               # zzz = response.value.magnitude
               # values.append("{0:.2f}".format(zzz)) 

                cmd = obd.commands.THROTTLE_POS # none not supported 
                response = connection.query(cmd)
                print(22)
                print(response.value)
               # zzz = response.value.magnitude
               # values.append("{0:.2f}".format(zzz)
               # comes out as a percentage  

                cmd = obd.commands.OBD_COMPLIANCE # OBD-II as defined by the CARB, not supported
                response = connection.query(cmd)
                print(23)
                print(response.value)
               # zzz = response.value.magnitude
               # values.append("{0:.2f}".format(zzz))
               # needs a string

                cmd = obd.commands.WARMUPS_SINCE_DTC_CLEAR # None
                response = connection.query(cmd)
                print(24)
                print(response.value)
              # zzz = response.value.magnitude
              # values.append("{0:.2f}".format(zzz))

                cmd = obd.commands.RUN_TIME # 600 seconds
                response = connection.query(cmd)
                print(25)        
                print(response.value)
                runtm = response.value.magnitude
                values.append("{0:.1f}".format(runtm))
                           
                cmd = obd.commands.COMMANDED_EGR # none not supported
                response = connection.query(cmd)
                print(26)
                print(response.value)
               # zzz = response.value.magnitude
               # values.append("{0:.2f}".format(zzz))
               # comes out as a percentage

                cmd = obd.commands.RUN_TIME_MIL # none not supported
                response = connection.query(cmd)
                print(29)
                print(response.value)
               # zzz = response.value.magnitude
               # values.append("{0:.2f}".format(zzz))

                cmd = obd.commands.ABSOLUTE_LOAD #
                response = connection.query(cmd)
                print(30)
                print(response.value)
               # zzz = response.value.magnitude
               # values.append("{0:.2f}".format(zzz))

                cmd = obd.commands.TIME_SINCE_DTC_CLEARED # None
                response = connection.query(cmd)
                print(31)
                print(response.value)
               # zzz = response.value.magnitude
               # values.append("{0:.2f}".format(zzz))

                cmd = obd.commands.BAROMETRIC_PRESSURE # 100 kilopascal
                response = connection.query(cmd)
                print(32)
                print(response.value)
                barp = response.value.magnitude
                values.append("{0:.2f}".format(barp))
               # comes out as a kilopascal

                cmd = obd.commands.BAROMETRIC_PRESSURE # 100 kilopascal
                response = connection.query(cmd)
                print(32)        
                print(response.value)
                barp = response.value.magnitude
                values.append("{0:.2f}".format(barp))
             #  comes out as a kilopascal 

                cmd = obd.commands.GET_CURRENT_DTC # []
                response = connection.query(cmd)
                print(33)        
                print(response.value)        
             #  zzz = response.value.magnitude
             #  values.append("{0:.2f}".format(zzz))
             #  needs to be a special

                cmd = obd.commands.INTAKE_TEMP # 25 degC
                response = connection.query(cmd)
                print(34)        
                print(response.value)
                DegI = response.value.magnitude
                values.append("{0:.2f}".format(DegI))
             #  zzz = response.value.magnitude
             #  values.append("{0:.2f}".format(zzz))

                cmd = obd.commands.FUEL_LEVEL # 50.19607843137255 percent 50.2 on chart
                response = connection.query(cmd)
                print(35)        
                print(response.value)
             #  gas = response.value.magnitude
             #  values.append("{0:.2f}".format(gas))
             #  comes out as a percentage

             # cmd = obd.commands.xxx # none
               # response = connection.query(cmd)
               # print(36)
               # print(response.value)

                cmd = obd.commands.FUEL_RAIL_PRESSURE_VAC # none not supported
                response = connection.query(cmd)
                print(37)
                print(response.value)
               # zzz = response.value.magnitude
               # values.append("{0:.2f}".format(zzz))
               # comes out as a kilopascal

                cmd = obd.commands.FUEL_RAIL_PRESSURE_DIRECT # none not supported
                response = connection.query(cmd)
                print(38)
                print(response.value)
               # zzz = response.value.magnitude
               # values.append("{0:.2f}".format(zzz))

                cmd = obd.commands.EVAP_VAPOR_PRESSURE # None
                response = connection.query(cmd)
                print(39)
                print(response.value)
               # zzz = response.value.magnitude
               # values.append("{0:.2f}".format(zzz))

                cmd = obd.commands.FUEL_LEVEL # 50.19607843137255 percent
                response = connection.query(cmd)
                print(40)
                print(response.value)
                gas = response.value.magnitude
                values.append("{0:.2f}".format(gas))
               # comes out as a percentage

                cmd = obd.commands.EGR_ERROR # none not supported
                response = connection.query(cmd)
                print(41)
                print(response.value)
               # zzz = response.value.magnitude
               # values.append("{0:.2f}".format(zzz))
               # comes out as a percentage

               # cmd = obd.commands.EVAPORATIVE_PURGE # none
               # response = connection.query(cmd)
               # print(42)
               # print(response.value)
               # zzz = response.value.magnitude
               # values.append("{0:.2f}".format(zzz))
               # comes out as a percentage

                f.write(",".join(str(value) for value in values) + "\n")

        time.sleep(0.05)
        # 1 hour = 3600 seconds 
        # 1 day =  86400 seconds

if __name__ == '__main__':
      getSpeed()