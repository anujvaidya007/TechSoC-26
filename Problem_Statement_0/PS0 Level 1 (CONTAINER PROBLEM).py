print("Enter max adport capacity")
C = int(input())
print("Enter the number of containers")
N = int(input())
container = [0]*N
for x in range (0 , N):
     print("Enter weight of W",x+1," container")
     container[x] = int(input()) 
S = 0
for x in range (0 , N):
      S += container[x]
print("Total Shipment Weight: ", S )
print("Average Container Weight: ", S/N)
largest = container[0]
for x in range (0 , N-1):
      if container[x+1] > largest :
          largest = container[x+1]
print("Heaviest container: " , largest)
smallest = container[0]
for x in range (0 , N-1):
      if container[x+1] < smallest :
          smallest = container[x+1]
print("Lightest container: " , smallest)
if S > 200 :
    print("Classification : Heavy ")
else :
    print("Classification : Light ")
print ("Port Capacity: " , C)
if S >= C :
    print("Shipment exceeds port capacity")
else :
    print("Shipment can be unloaded")
          