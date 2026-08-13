import math
print("Mencari Jarak antara Dua Titik pada Permukaan Bumi")
R = 6371.2 #jari-jari bumi

#Langitude
lat1 = float(input("Latitude 1 = "))
Lat1 = math.radians(lat1)

lat2 = float(input("Latitude 2 = "))
Lat2 = math.radians(lat2)

DLat = Lat2 - Lat1

havDLat = math.sin(DLat/2)**2


#Longitude
long1 = float(input("Longitude 1 = "))
Long1 = math.radians(long1)


long2 = float(input("Longitude 2 = "))
Long2 = math.radians(long2)


DLong = Long2 - Long1

havDLong = math.sin(DLong/2)**2


#haversine teta
havTeta = havDLat + math.cos(Lat1) * math.cos(Lat2) * havDLong

#inverse pake arc sin biar dapet radian Teta
Teta = 2*math.asin(math.sqrt(havTeta))


Jarak = Teta * R
print("Jarak =", Jarak)