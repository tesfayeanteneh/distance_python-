from math import sin, cos, sqrt, atan2, radians
def calc_Distance(lat1,long1,lat2,long2):
    R=6373.0 # radious of earth
    
    # convert points to radian
    lat1_rad = radians(lat1)
    long1_rad = radians(long1)
    lat2_rad = radians(lat2)
    long2_rad = radians(long2)
    
    # find respective differencces
    long_dist=radians(long2-long1)
    lat_dist=radians(lat2-lat1)
    
    #haversine formula
    a = sin(lat_dist / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(long_dist / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    #calculate the distance
    distance = R * c
    
    return distance

# The distance between Tel Aviv and Chennai
#Telaviv 
tel_lat=32.0853
tel_long=34.7818

#Chennai
che_lat=13.0827
che_long=80.2707
    
#calculate distance
distance=calc_Distance(tel_lat,tel_long,che_lat,che_long)

print('The distance Between Tel Aviv and Chennai is = ',distance,' KM')

'''
The distance Between Tel Aviv and Chennai is =  5079.882920713635  KM

'''