full= [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30, 31, 32],
        [33, 34, 35, 36, 37, 38, 39, 40],
        [41, 42, 43, 44, 45, 46, 47, 48],
        [49, 50, 51, 52, 53, 54, 55, 56],
        [57, 58, 59, 60, 61, 62, 63, 64]
    ]
userMatrix = [[0] * 2 for i in range(2)]
#take matrix from user
for i in range(2):
	for j in range(2):
		userMatrix[i][j] = input("Enter at index " + str(i) + " " + str(j) + " : " )
a=0
b=0
varbool=False
for i in range(0,8):
	for j in range(0,8):
		if full[i][j]==userMatrix[a][b]:
			if full[i][j+1]==userMatrix[a][b+1]:
				if full[i+1][j]==userMatrix[a+1][b]:
					if full[i+1][j+1]==userMatrix[a+1][b+1]:
						varbool=True
						row=i
						col=j
						break
		
if varbool==True:
	print ("Matrix found at index [" + str(row) + "][" + str(col) +"]")	
else:
	print "matrix Not found"

