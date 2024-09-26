# ecef_to_eci.py
#
# Usage: python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km
#  Converts ECEF vector to ECI
# Parameters:
#  year: year in Gregorian
#  month: month in Gregorian
#  day: day in Gregorian
#  hour: hour in Gregorian
#  minute: minute in Gregorian
#  second: second in Gregorian
#  ecef_x_km: ecef x vector in km
#  ecef_y_km: ecef y vector in km
#  ecef_z_km: ecef z vector in km
# Output: print ecef_x_km, ecef_y_km, and ecef_z_km
#
# Written by Yonghwa Kim
# Other contributors: None

# import Python modules
import math # math module
import sys  # argv

# constants
w = 7.292115*pow(10,-5) #rad/s

# initialize script arguments
year = float('nan')
month = float('nan')
day = float('nan')
hour = float('nan')
minute = float('nan')
second = float('nan')
ecef_x_km = float('nan')
ecef_y_km = float('nan')
ecef_z_km = float('nan')

# parse script arguments
if len(sys.argv)==10:
  year = float(sys.argv[1])
  month = float(sys.argv[2])
  day = float(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  second = float(sys.argv[6])
  ecef_x_km = float(sys.argv[7])
  ecef_y_km = float(sys.argv[8])
  ecef_z_km = float(sys.argv[9])
else:
  print(\
   'Usage: '\
   'python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km'\
  )
  exit()

# Caculate Julian date for the given datetime
jd = (day-32075+int(1461*(year+4800+int((month-14)/12))/4)+int(367*(month-2-int((month-14)/12)*12)/12)-int(3*int((year+4900+int((month-14)/12))/100)/4))

# JD at midnight
jd_midnight = jd - 0.5

# Fractional day part based on the time (hour, minute, second)
d_frac = (second + 60 * (minute + 60 * hour)) / 86400.0
    
# Final fractional Julian Date
jd_frac = jd_midnight + d_frac

#
T_UT1 = (jd_frac-2451545)/36525
theta_GMST = 67310.54841+(876600*60*60+8640184.812866)*T_UT1+0.093104*pow(T_UT1,2)+(-6.2*pow(10,-6)*pow(T_UT1,3))
GMST_rad = (theta_GMST%86400)*w
GMST_deg = GMST_rad*180/math.pi

# Time-Dependent Rotation to figure ecef, manually do dot product 
eci_x_km = math.cos(GMST_rad)*ecef_x_km - math.sin(GMST_rad)*ecef_y_km
eci_y_km = math.sin(GMST_rad)*ecef_x_km + math.cos(GMST_rad)*ecef_y_km
eci_z_km = ecef_z_km

# print ecef_x_km, ecef_y_km, and ecef_z_km
print(eci_x_km)
print(eci_y_km)
print(eci_z_km)