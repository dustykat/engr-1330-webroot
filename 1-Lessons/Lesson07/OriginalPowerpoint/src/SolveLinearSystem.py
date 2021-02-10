# SolveLinearSystem.py
# Code to read A and b
# Then solve Ax = b for x by Gaussian elimination with back substitution
#
amatrix = [] # null list to store matrix reads
bvector = []
rowNumA = 0
colNumA = 0
rowNumB = 0
######################################
# connect and read file for MATRIX A #
######################################
afile = open("A.txt","r")
for line in afile:
    amatrix.append([float(n) for n in line.strip().split()])
    rowNumA += 1
afile.close() # Disconnect the file
######################################
# end file read ,disconnect file     #
######################################
colNumA = len(amatrix[0])
afile = open("B.txt","r")
for line in afile:
    bvector.append(float(line))  # vector read different -- just float the line
    rowNumB += 1
afile.close() # Disconnect the file
print (bvector)
# check the arrays
if rowNumA != rowNumB:
    print ("row ranks not same -- aborting now")
    quit()
else:
    print ("row ranks same -- continuing operation")
# print all columns each row
cmatrix = [[0 for j in range(colNumA)]for i in range(rowNumA)]
dmatrix = [[0 for j in range(colNumA)]for i in range(rowNumA)]
xvector = [0 for i in range(rowNumA)]
dvector = [0 for i in range(rowNumA)]
for i in range(0,rowNumA,1):
    print (amatrix[i][0:colNumA], bvector[i],cmatrix[i][0:colNumA])
print ("-----------------------------")
# copy amatrix into cmatrix
cmatrix = [[amatrix[i][j] for j in range(colNumA)]for i in range(rowNumA)]
dmatrix = [[amatrix[i][j] for j in range(colNumA)]for i in range(rowNumA)]
dvector = [bvector[i] for i in range(rowNumA)]
# build the diagonal -- assume diagonally dominant
for k in range(rowNumA-1):
    l = k+1
    for i in range(l,rowNumA):
        for j in range(colNumA):
            cmatrix[i][j]=amatrix[i][j]-amatrix[k][j]*amatrix[i][k]/amatrix[k][k]
        bvector[i] = bvector[i]-bvector[k]*amatrix[i][k]/amatrix[k][k]
    for i in range(rowNumA):
        for j in range(colNumA):
            amatrix[i][j] = cmatrix[i][j]
# gaussian reduction done
# now for the back substitution
#for i in range(0,rowNumA,1):
#    print (amatrix[i][0:colNumA], bvector[i],cmatrix[i][0:colNumA])
#print ("-----------------------------")
for k in range(rowNumA-1,-1,-1):
    sum = 0.0
    for i in range(rowNumA):
        if i == k:
            continue 
        else:
            sum = sum + amatrix[k][i]*xvector[i]
        xvector[k]=(bvector[k]-sum)/amatrix[k][k]
for i in range(0,rowNumA,1):
    print (dmatrix[i][0:colNumA],xvector[i],dvector[i])
print ("-----------------------------")


##
### print all columns each row
##for i in range(0,rowNumA,1):
##    print amatrix[i][0:colNumA]
##print "-----------------------------"
##bmatrix = [] # null list to store matrix reads
##rowNumB = 0
##colNumB = 0
########################################
### connect and read file for MATRIX B #
########################################
##bmatrix = [] # null list for reading file
##afile = open("A_Inverse.txt","r")
##for line in afile:
##    bmatrix.append([float(n) for n in line.strip().split()])
##    rowNumB += 1
##afile.close() # Disconnect the file
########################################
### end file read ,disconnect file     #
########################################
##colNumB = len(bmatrix[0])
### print all columns each row
##for i in range(0,rowNumB,1):
##    print bmatrix[i][0:colNumB]
##print "------------------------------"
############################################################
##### multiply the matrices, store result in result_matrix #
############################################################
##result_matrix = [[0 for j in range(colNumB)] for i in range(rowNumA)]
##for i in range(0,rowNumA):
##    for j in range(0,colNumB):
##        for k in range(0,colNumA):
##            result_matrix[i][j]=result_matrix[i][j]+amatrix[i][k]*bmatrix[k][j]
### observe the triple for-loop structure and the counting scheme
### print all cooumns each row
##for i in range(0,rowNumA,1):
##    print result_matrix[i][0:colNumB]
##
##    
##
##    
