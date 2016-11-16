from pygeocoder import Geocoder


fp=open('postal_bdoc.csv','r')
out=open('latlong.csv','w')

line=fp.readline()
c=0;
while(line!=""):
    fields=line.split(',')
    c=c+1
    print (c)
    print (fields[1])
    latlong=Geocoder.geocode(fields[1]+', Bangalore')    
    print latlong[0].coordinates
    out.write(str(latlong[0].coordinates[0])+','+str(latlong[0].coordinates[1])+'\n')
    out.flush()
    
    line=fp.readline()
    
out.close()
fp.close()
