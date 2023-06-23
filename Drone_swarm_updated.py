import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point,Polygon
import random

polygon_verticesc=[(0,0),(40,0),(20,30)]
num_points=3
randompoints=[]

polygon=Polygon(polygon_verticesc)

c=[]

for i in range(num_points):
    while True:
        x=random.uniform(polygon.bounds[0],polygon.bounds[2])
        y=random.uniform(polygon.bounds[1],polygon.bounds[3])
        
        point=Point(x,y)
        
        
        if polygon.contains(point):
            randompoints.append(point)
            c.append([x,y])
            break
        
    
     
x=[point.x for point in randompoints]
y=[point.y for point in randompoints]

plt.scatter(x,y,marker='o')


plt.plot([0,20,40],[0,30,0], color='red',marker='o')
plt.plot([0,40],[0,0],color='red',marker='o')

#Swarm logic 
#First i would choose one drone, find the point nearest to it and instruct it to follow a straight line to the vertex. 
#Now instead of choosing another drone , i would choose another vertice except the one of the 1st drone, and now ill choose the drone closest to the vertice and instruct the drone to go to the vertex.
#I did this so that even the slightest possibility of drone collision is avoided.
#Finally the third drone goes to the remaining vertex.


#Drone1
a1=random.choice(c)
a=np.array(a1)
vertices=np.array([[0,0],[40,0],[20,30]])
distances=np.linalg.norm(vertices-a,axis=1).tolist()
print(distances)
b=[i[0] for i in sorted(enumerate(distances),key=lambda x:x[1])]
plt.plot([a[0],vertices[b[0]][0]],[a[1],vertices[b[0]][1]],color='green',label='Drone 1') 


print('The Velocity of drone 1 is :\n')
if distances[b[0]] >= 12:
    print('3t m/s --> t<=2')
    if distances[b[0]] >12:
        print('6 m/s --> 2 < t < ',(distances[b[0]]-12)/6)
    print('6-3t m/s --> ',(distances[b[0]]-12)/6,'< t <',(distances[b[0]]-12)/6 +2) 
if 3<=distances[b[0]]<12:
    print('3t m/s --> t<=1')
    if 3<distances[b[0]]:
        print('3 m/s --> 1 < t < ', (distances[b[0]]-3)/3)
    print('3-3t m/s --> ',(distances[b[0]]-3)/3,' < t < ',(distances[b[0]]-3)/3 +1)
#Now the forward thrust lets say gives only 1 m/s^2    
if 2<distances[b[0]]<3:
    print('t m/s --> t<=1')
    if distances[b[0]]>2:
        print('1 m/s --> 1 < t < ',(distances[b[0]]-2)/1)
    print('1-t m/s --> ',(distances[b[0]]-2)/1,' < t < ',(distances[b[0]]-2)/1 +1)    
if distances[b[0]]<2:
    print('The target point is too close')
print('\n')    

#Drone2
c.remove(a1)
anew=np.array(c)
q=vertices[b[0]].tolist()
ver=vertices.tolist()
ver.remove(q)
vnew=random.choice(ver)
e=np.array(c)
distances=np.linalg.norm(e-vnew,axis=1).tolist()
b=[i[0] for i in sorted(enumerate(distances), key = lambda x:x[1])]
plt.plot([vnew[0],c[b[0]][0]],[vnew[1],c[b[0]][1]],color='Blue',label='Drone 2')


print('The Velocity of drone 2 is :\n')
if distances[b[0]] >= 12:
    print('3t m/s --> t<=2')
    if distances[b[0]] >12:
        print('6 m/s --> 2 < t < ',(distances[b[0]]-12)/6)
    print('6-3t m/s --> ',(distances[b[0]]-12)/6,'< t <',(distances[b[0]]-12)/6 +2) 
if 3<=distances[b[0]]<12:
    print('3t m/s --> t<=1')
    if 3<distances[b[0]]:
        print('3 m/s --> 1 < t < ', (distances[b[0]]-3)/3)
    print('3-3t m/s --> ',(distances[b[0]]-3)/3,' < t < ',(distances[b[0]]-3)/3 +1)
#Now the forward thrust lets say gives only 1 m/s^2    
if 2<distances[b[0]]<3:
    print('t m/s --> t<=1')
    if distances[b[0]]>2:
        print('1 m/s --> 1 < t < ',(distances[b[0]]-2)/1)
    print('1-t m/s --> ',(distances[b[0]]-2)/1,' < t < ',(distances[b[0]]-2)/1 +1)    
if distances[b[0]]<2:
    print('The target point is too close')

print('\n')

#Drone3
c.remove(c[b[0]])
cm=np.array(c)
ver.remove(vnew)
vertices=np.array(ver)
plt.plot([ver[0][0],c[0][0]],[ver[0][1],c[0][1]],color='yellow',label='Drone 3')
plt.legend()
distance = np.linalg.norm(c- vertices,axis=1).tolist()


print('The Velocity of drone 3 is :\n')
if distance[0] >= 12:
    print('3t m/s --> t<=2')
    if distance[0] >12:
        print('6 m/s --> 2 < t < ',(distance[0]-12)/6)
    print('6-3t m/s --> ',(distance[0]-12)/6,'< t <',(distance[0]-12)/6 +2) 
if 3<=distance[0]<12:
    print('3t m/s --> t<=1')
    if 3<distance[0]:
        print('3 m/s --> 1 < t < ', (distance[0]-3)/3)
    print('3-3t m/s --> ',(distance[0]-3)/3,' < t < ',(distance[0]-3)/3 +1)
#Now the forward thrust lets say gives only 1 m/s^2    
if 2<distance[0]<3:
    print('t m/s --> t<=1')
    if distance[0]>2:
        print('1 m/s --> 1 < t < ',(distance[0]-2)/1)
    print('1-t m/s --> ',(distance[0]-2)/1,' < t < ',(distance[0]-2)/1 +1)    
if distance[0]<2:
    print('The target point is too close')
 
        
plt.show()
