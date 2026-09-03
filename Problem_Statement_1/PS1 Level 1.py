print("Input the number of Rows")
R = int(input())
print("Input the number of Column")
C = int(input())
print("Input the number of generations to simulate")
G = int(input())

Total_grids = [0]*(G+1)
for x in range (G+1):
    Total_grids[x] = [0]*(R+2)

for x in range(G+1):
    for y in range (R+2):
        Total_grids[x][y] = [ '.' ]*(C+2)
        
print("Type ' . ' for dead, ' # ' for alive.")
for x in range(R):
    print("Write the", x+1 , "row ")
    Total_grids[0][x+1] = list('.' + input() + '.')

Hash = 0
for x in range(G):
    for y in range (1, R+1):
        for z in range (1, C+1):
            for i in range (-1 , 2):
                for j in range(-1 , 2):
                    if Total_grids[x][y+i][z+j] == '#':
                       Hash+=1
            if Total_grids[x][y][z] == '#':
                Hash+=-1
                if Hash < 2 :
                    Total_grids[x+1][y][z] = '.'
                elif Hash == 2 or Hash == 3:
                    Total_grids[x+1][y][z] = '#'
                elif Hash > 3 :
                    Total_grids[x+1][y][z] = '.'
                           
            elif Total_grids[x][y][z] == '.':
                if Hash == 3:
                    Total_grids[x+1][y][z] = '#'
            Hash = 0
for x in range (R):
    for y in range (C):
        print(Total_grids[G][x+1][y+1] , end = "")
    print("")