import math
print("Mencari Jarak antara Dua Titik pada Permukaan Bumi")
R = 6371.2 #jari-jari bumi

#Langitude
lat1 = float(input("Latitude 1 = "))
Lat1 = math.radians(lat1)
print("Radian Latitude 1 =", Lat1)

lat2 = float(input("Latitude 2 = "))
Lat2 = math.radians(lat2)
print("Radian Latitude 2 =", Lat2)

DLat = Lat2 - Lat1
print("Selisih Latitude =", DLat)
havDLat = math.sin(DLat/2)**2
print("Haversine Latitude =", havDLat)

#Longitude
long1 = float(input("Longitude 1 = "))
Long1 = math.radians(long1)
print("Radian Longitude 1 =", Long1)

long2 = float(input("Longitude 2 = "))
Long2 = math.radians(long2)
print("Radian Longitude 2 =", Long2)

DLong = Long2 - Long1
print("Selisih Longitude =", DLong)
havDLong = math.sin(DLong/2)**2
print("Haversine Longitude =", havDLong)

#haversine teta
havTeta = havDLat + math.cos(Lat1) * math.cos(Lat2) * havDLong
print("Haversine Teta =", havTeta)
#inverse pake arc sin biar dapet radian Teta
Teta = 2*math.asin(math.sqrt(havTeta))
print("Teta =", Teta)

Jarak = Teta * R
print("Jarak =", Jarak)