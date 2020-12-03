N = 2

def transpose(A,B): 

	for i in range(N): 
		for j in range(N): 
			B[i][j] = A[j][i] 


A = [ [1, 1], 
	[2, 2] ] 


B = [[0,0],[0,0]] 

transpose(A, B) 

for i in range(N): 
	for j in range(N): 
		print(B[i][j], " ", end='') 
	print() 
	

