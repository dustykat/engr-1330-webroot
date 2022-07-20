

# vector_matrix_lib.py
# useful linear algebra tools
import math   # This will import math module

def writeM(M,ir,jc,label):
    print ("------",label,"------")
    for i in range(0,ir,1):
        print (M[i][0:jc])
    print ("-----------------------------")
    #return

def writeV(V,ir,label):
    print ("------",label,"------")
    for i in range(0,ir,1):
        print (V[i])
    print ("-----------------------------")
    #return

def mmmult(amatrix,bmatrix,rowNumA,colNumA,rowNumB,colNumB):
    AB =[[0.0 for j in range(colNumB)] for i in range(rowNumA)]
    for i in range(0,rowNumA):
        for j in range(0,colNumB):
            for k in range(0,colNumA):
                AB[i][j]=AB[i][j]+amatrix[i][k]*bmatrix[k][j]
    return(AB)

def mvmult(amatrix,xvector,rowNumA,colNumA):
    bvector=[0.0 for i in range(rowNumA)]
    for i in range(0,rowNumA):
        for j in range(0,1):
            for k in range(0,colNumA):
                bvector[i]=bvector[i]+amatrix[i][k]*xvector[k]
    return(bvector)

def vvadd(avector,bvector,length):
    aplusb=[0.0 for i in range(length)]
    for i in range(length):
        aplusb[i] = avector[i] + bvector[i]
    return(aplusb)

def vvsub(avector,bvector,length):
    aminusb=[0.0 for i in range(length)]
    for i in range(length):
        aminusb[i] = avector[i] - bvector[i]
    return(aminusb)

def vdotv(avector,bvector,length):
    adotb=0.0
    for i in range(length):
        adotb=adotb+avector[i]*bvector[i]
    return(adotb)

# SolveLinearSystem.py
# Code to read A and b
# Then solve Ax = b for x by Gaussian elimination with back substitution
#
##########
def linearsolver(A,b):
    n = len(A)
#    M = A  #this is object to object equivalence
# copy A into M element by element - to operate on M without destroying A
    M=[[0.0 for jcol in range(n)]for irow in range(n)]
    for irow in range(n):
        for jcol in range(n):
            M[irow][jcol]=A[irow][jcol]

#
    i = 0
    for x in M:
     x.append(b[i])
     i += 1

    for k in range(n):
     for i in range(k,n):
       if abs(M[i][k]) > abs(M[k][k]):
          M[k], M[i] = M[i],M[k]
       else:
          pass

     for j in range(k+1,n):
         q = float(M[j][k]) / M[k][k]
         for m in range(k, n+1):
            M[j][m] -=  q * M[k][m]

    x = [0 for i in range(n)]

    x[n-1] =float(M[n-1][n])/M[n-1][n-1]
    for i in range (n-1,-1,-1):
      z = 0
      for j in range(i+1,n):
          z = z  + float(M[i][j])*x[j]
      x[i] = float(M[i][n] - z)/M[i][i]
#    print (x)
    return(x)
#
# hydraulic elements prototype functions
# Jain Friction Factor Function -- Tested OK 23SEP16
import math   # This will import math module

def friction_factor(roughness,diameter,reynolds):
    temp1 = roughness/(3.7*diameter)
    temp2 = 5.74/(reynolds**(0.9))
    temp3 = math.log10(temp1+temp2)
    temp3 = temp3**2
    friction_factor = 0.25/temp3
    return(friction_factor)

# Velocity Function
def velocity(diameter,discharge):
    velocity=discharge/(0.25*math.pi*diameter**2)
    return(velocity)

# Reynolds Number Function  
def reynolds_number(velocity,diameter,mu):
    reynolds_number = abs(velocity)*diameter/mu
    return(reynolds_number)

# Geometric factor function
def k_factor(howlong,diameter,gravity):
    k_factor = (16*howlong)/(2.0*gravity*math.pi**2*diameter**5)
    return(k_factor)

########## Initial Memory Allocations ###############
    bvector = []
    rowNumA = 0
    colNumA = 0
    rowNumB = 0
    verbose = 'false' # set to true for in-class demonstration
""
    elevation = [] # null list node elevations
    diameter =  [] # null list pipe diameters
    distance =  [] # null list pipe lengths
    roughness = [] # null list pipe roughness
    flowguess = [] # null list pipe flow rates
    nodearcs =  [] # node-arc incidence matrix
    rhs_true =  [] # null list for nodal demands
    tempvect = [] # null list for reading from external file, then recasting into one of the above lists

##############################################
# connect and read file for Pipeline Network #
# #############################################
#    infilename="L15-E1.txt"
    afile = open(infilename,"r")
#afile = open("PipeNetworkLesson15.txt","r")
    nnodes = int(afile.readline())
    npipes = int(afile.readline())
# read elevation vector
    tempvect.append([float(n) for n in afile.readline().strip().split()])
    for i in range(0,nnodes,1):
        elevation.append(float(tempvect[0][i]))
    tempvect = [] # reset vector
# read diameter vector
    tempvect.append([float(n) for n in afile.readline().strip().split()])
    for i in range(0,npipes,1):
        diameter.append(float(tempvect[0][i]))
    tempvect = [] # reset vector
# read length vector
    tempvect.append([float(n) for n in afile.readline().strip().split()])
    for i in range(0,npipes,1):
        distance.append(float(tempvect[0][i]))
    tempvect = [] # reset vector
# read roughness vector
    tempvect.append([float(n) for n in afile.readline().strip().split()])
    for i in range(0,npipes,1):
        roughness.append(float(tempvect[0][i]))
    tempvect = [] # reset vector
# read viscosity (scalar)
    viscosity = float(afile.readline())
# read current flow guess
    tempvect.append([float(n) for n in afile.readline().strip().split()])
    for i in range(0,npipes,1):
        flowguess.append(float(tempvect[0][i]))
    tempvect = [] # reset vector
# read nodearc incidence matrix
## future revisions read directly into augmented matrix, or find way to release nodearc from stack
    for irow in range(0,nnodes,1):  # then read each row
        nodearcs.append([float(n) for n in afile.readline().strip().split()])
# read demands guess
    tempvect.append([float(n) for n in afile.readline().strip().split()])
    for i in range(0,nnodes+npipes,1):
        rhs_true.append(float(tempvect[0][i]))
    tempvect = [] # reset vector      
######################################
# end file read ,disconnect file     #
# #####################################
    afile.close() # Disconnect the file

######################################
# echo the input in human readable   #
# #####################################
    print('####ECHO INPUT################\nInput File: ',infilename)
    print('number of nodes : ',nnodes)
    print('number of pipes : ',npipes)
    print('viscosity       : ',viscosity)
    print ("-----------------------------")
    for irow in range(0,nnodes):
        print('node id:',irow, ', elevation :',elevation[irow],' head :',rhs_true[irow+npipes])
    print ("-----------------------------")
    for jcol in range(0,npipes):
        print('pipe id:',jcol,', diameter : ' ,diameter[jcol],', distance : ',distance[jcol],
              ', roughness : ',roughness[jcol],', flow  : ',flowguess[jcol])
    print ("-----------------------------")
##for jcol in range(0,nnodes+npipes):
##    print('irow :',jcol,' RHS True :',rhs_true[jcol])
##print ("-----------------------------")
    print("node-arc incidence matrix")
    for i in range(0,nnodes,1):
        print (nodearcs[i][0:npipes])
    print ("-----------------------------")

# create augmented matrix
    colNumA = npipes+nnodes
    rowNumA = nnodes+npipes
    augmentedMat = [] # null list to store augmented matrix

""
    augmentedMat = [[0.0 for j in range(colNumA)]for i in range(rowNumA)] #fill with zeroes
#build upper left partition -- from nodearcs
    for ir in range(0,nnodes):
        for jc in range (0,npipes):
            augmentedMat[ir][jc] = nodearcs[ir][jc]
    istart=nnodes
    iend=nnodes+npipes
    jstart=npipes
    jend=npipes+nnodes
    for ir in range(istart,iend):
        for jc in range (jstart,jend):
            augmentedMat[ir][jc] = -1.0*nodearcs[jc-jstart][ir-istart] + 0.0
    if verbose == 'true' :
        print("augmented matrix before loss factors")
        writeM(augmentedMat,rowNumA,colNumA,"augmented matrix")
    
#########Simulation Constants and Additional Memory Allocation #######
    howmany=50 #iterations max
    tolerance1 = 1e-24
    tolerance2 = 1e-24
    velocity_pipe = [0 for i in range(npipes)]  # null list velocities
    reynolds      = [0 for i in range(npipes)]  # null list reynolds numbers
    friction      = [0 for i in range(npipes)]  # null list friction 
    geometry      = [0 for i in range(npipes)]  # null list geometry
    lossfactor    = [0 for i in range(npipes)]  # null list loss
    jacbMat = [] # null list to store jacobian matrix
    jacbMat = [[0.0 for j in range(colNumA)]for i in range(rowNumA)] #fill with zeroes


    solvecguess =[ 0.0 for i in range(rowNumA)] 
    solvecnew =[ 0.0 for i in range(rowNumA)]
    for i in range(0,npipes,1):
        solvecguess[i] = flowguess[i]
        geometry[i] = k_factor(distance[i],diameter[i],32.2)
#solvecguess is a current guess -- wonder if more pythonic way for this assignment
##    print('irow :',i,' Geometry Factor :',geometry[i])
##print ("-----------------------------")

###############################################################
# # ITERATION LOOP                                             #
# ##############################################################
    for iteration in range(howmany): # iteration outer loop
        if verbose == 'true' :
            print("solutions at begin of iteration",iteration)
            for jcol in range(0,nnodes+npipes):
                print('irow :',jcol,' solvecnew :',solvecnew[jcol]," solvecguess ",solvecguess[jcol])
            print ("-----------------------------")
        for i in range(0,npipes,1):
            velocity_pipe[i] = velocity(diameter[i],flowguess[i])    
            reynolds[i]=reynolds_number(velocity_pipe[i],diameter[i],viscosity)
            friction[i]=friction_factor(roughness[i],diameter[i],reynolds[i])
            lossfactor[i]=friction[i]*geometry[i]*abs(flowguess[i])
        if verbose == 'true' :
            for jcol in range(0,npipes):
                print('pipe id:',jcol,', velocity : ' ,velocity_pipe[jcol],', reynolds : ',reynolds[jcol],
              ', friction : ',friction[jcol],', loss factor : ',lossfactor[jcol],'flow guess',flowguess[jcol])
################################################################
# BUILD AUGMENTED MATRIX CURRENT Q+H SOLUTION                  #
# ###############################################################
        augmentedMat = [[0.0 for j in range(colNumA)]for i in range(rowNumA)] #fill with zeroes
    #build upper left partition -- from nodearcs
        for ir in range(0,nnodes):
            for jc in range (0,npipes):
                augmentedMat[ir][jc] = nodearcs[ir][jc]
    #build lower right == transpose of upper left
        istart=nnodes
        iend=nnodes+npipes
        jstart=npipes
        jend=npipes+nnodes
        for ir in range(istart,iend):
            for jc in range (jstart,jend):
                augmentedMat[ir][jc] = -1.0*nodearcs[jc-jstart][ir-istart] + 0.0
    # build lower left partition of the matrix
        istart = nnodes
        iend = nnodes+npipes
        jstart = 0
        jend = npipes
        for i in range(istart,iend ):
            for j in range(jstart,jend ):
    #        print('i =',i,'j=',j)
                if (i-istart) == j :
    #            print('i =',i,'j=',j)
                    augmentedMat[i][j] = -1.0*lossfactor[j] + 0.0
        if verbose == 'true' :
            print("updated augmented matrix in iteration",iteration)
            writeM(augmentedMat,rowNumA,colNumA,"augmented matrix")
################################################################
# BUILD JACOBIAN MATRIX CURRENT Q+H SOLUTION                   #
# ###############################################################        
    # now build current jacobian
        for i in range(rowNumA):
            for j in range(colNumA):
                jacbMat[i][j] = augmentedMat[i][j]
    # modify lower left partition
        istart = nnodes
        iend = nnodes+npipes
        jstart = 0
        jend = npipes
        for i in range(istart,iend ):
            for j in range(jstart,jend ):
    #        print('i =',i,'j=',j)
                if (i-istart) == j :
    #            print('i =',i,'j=',j)
                    jacbMat[i][j] = 2.0*jacbMat[i][j]
##        for jcol in range(0,nnodes+npipes):
##            print('irow :',jcol,' solvecnew :',solvecnew[jcol]," solvecguess ",solvecguess[jcol])
##        print ("-----------------------------")
# matrix multiply augmentedMat*solvecguess to get current g(Q)
#    gq = [0.0 for i in range(rowNumA)] # zero gradient vector
##    if verbose == 'true' :
##        print("augmented matrix in iteration",iteration)
##        writeM(augmentedMat,rowNumA,colNumA,"augmented matrix before mmult")
    gq = matrixvectormult(augmentedMat,solvecguess,rowNumA,colNumA)
##    if verbose == 'true' :
##        writeV(gq,rowNumA,"gq vectorbefore subtract rhs_true")
# subtract rhs
#    for i in range(rowNumA):
        gq = vectorsub(gq,rhs_true,rowNumA)#vector subtract
        if verbose == 'true' :
            print("computed g(q) in iteration",iteration)
            writeV(gq,rowNumA,"gq vector")
            print("compare current and new guess")
            for jcol in range(0,nnodes+npipes):
                print('irow :',jcol,' solvecnew :',solvecnew[jcol]," solvecguess ",solvecguess[jcol])
            print ("-----------------------------")
        dq = [0.0 for i in range(rowNumA)] # zero update vector
        if verbose == 'true' :
            writeV(dq,rowNumA,"dq vector before linear solve")
        if verbose == 'true' :
            print("jacobian before linearsolve in iteration",iteration)
            writeM(jacbMat,rowNumA,colNumA,"jabobian matrix")
        dq = linearsolver(jacbMat,gq) # memory leak after this call - linearsolve clobbers input lists
#    dq = numpy.linalg.solve(jacbMat,gq) #the numpy equivalent
        if verbose == 'true' :
            print("jacobian after linearsolve in iteration",iteration)
            writeM(jacbMat,rowNumA,colNumA,"jabobian matrix")

        if verbose == 'true' :
            writeV(dq,rowNumA,"dq vector -after linear solve")
        solvecnew = vectorsub(solvecguess,dq,rowNumA)#vector subtract
        if verbose == 'true' :
            print("Q_new = Q_old - DQ")
            writeV(solvecnew,rowNumA,"new guess vector")
#    tempvect =[ 0.0 for i in range(rowNumA)]
##        tempvect = matrixvectormult(jacbMat,dq,rowNumA,colNumA)
##        writeV(tempvect,rowNumA,"J*dq vector")
##        tempvect = vectorsub(tempvect,gq,rowNumA)
##        writeV(tempvect,rowNumA,"J*dq - gq vector")
            print("just after computing new guess, should be different")
            for jcol in range(0,nnodes+npipes):
                print('irow :',jcol,' solvecnew :',solvecnew[jcol]," solvecguess ",solvecguess[jcol])
            print ("-----------------------------")
#test for stopping
        tempvect =[ 0.0 for i in range(rowNumA)]
        for i in range(rowNumA):
            tempvect[i] = abs(solvecnew[i] - solvecguess[i])
        test1 = vdotv(tempvect,tempvect,rowNumA)
        if verbose == 'true' :
            print('test1',test1)
        tempvect =[ 0.0 for i in range(rowNumA)]
        for i in range(rowNumA):
            tempvect[i] = abs(gq[i])
        test2 = vdotv(tempvect,tempvect,rowNumA)
        if verbose == 'true' :
            print('test2',test2)
        if test1 < tolerance1 :
            print("###EXIT TYPE###\nUpdate not changing --exit and report current update")
            print("iteration",iteration)
# update guess
            solvecguess[:] = solvecnew[:]
            for i in range(0,npipes,1):
                flowguess[i] = solvecguess[i]

            break
        if test2 < tolerance2 :
            print("###EXIT TYPE###\nGradient near zero --exit and report current update")
            print("iteration",iteration)
# update guess
            solvecguess[:] = solvecnew[:]
            for i in range(0,npipes,1):
                flowguess[i] = solvecguess[i]

            break
        if verbose == 'true' :
            print("solution continuing")
            print("iteration",iteration)
    # update guess
        solvecguess[:] = solvecnew[:]
        if verbose == 'true' :
            for i in range(0,npipes,1):
                flowguess[i] = solvecguess[i]
## Write Current State ######################
            gq = matrixvectormult(augmentedMat,solvecguess,rowNumA,colNumA)
            print('number of nodes : ',nnodes)
            print('number of pipes : ',npipes)
            print('viscosity       : ',viscosity)
            print ("-----------------------------")
            for irow in range(0,nnodes):
                print('node id:',irow, ', elevation :',elevation[irow])
            print ("-----------------------------")
            for jcol in range(0,npipes):
                print('pipe id:',jcol,', diameter : ' ,diameter[jcol],', distance : ',distance[jcol],
              ', roughness : ',roughness[jcol],', flow guess : ',round(flowguess[jcol],3))
            print ("-----------------------------")
            for jcol in range(0,nnodes+npipes):
                print('irow :',jcol,' RHS True :',rhs_true[jcol],"RHS Current",round(gq[jcol],3))
            print ("-----------------------------")
            for jcol in range(0,nnodes+npipes):
                print('irow :',jcol,' solvecnew :',solvecnew[jcol]," solvecguess ",solvecguess[jcol])
            print ("-----------------------------")   
################################################
# end of outer loop
# ###############################################

# Report Results
    print("#####SIMULATION RESULTS#####\nResults at iteration = :",iteration)
    for i in range(0,npipes,1):
        flowguess[i] = solvecguess[i]
    print('number of nodes : ',nnodes)
    print('number of pipes : ',npipes)
    print('viscosity       : ',viscosity)
    print ("-----------------------------")
    istart = int(npipes)
    for irow in range(0,nnodes):
        print('node id:',irow+1, ', elevation (feet) :',elevation[irow],' head (feet) :',round(solvecnew[irow+npipes],3),' pressure (psi) :',round((14.75/33)*(solvecnew[irow+npipes]-elevation[irow]),3))
    print ("-----------------------------")
    for jcol in range(0,npipes):
        print('pipe id:',jcol,', diameter (feet) : ' ,diameter[jcol],', distance (feet) : ',distance[jcol],', friction factor : ',round(friction[jcol],3),', flow (cfs) : ',round(flowguess[jcol],3))
    print ("-----------------------------")
    if verbose == 'true' :
        for jcol in range(0,nnodes+npipes):
            print('irow :',jcol,' RHS True :',rhs_true[jcol],"RHS Current",gq[jcol])
        print ("-----------------------------")
        for jcol in range(0,nnodes+npipes):
            print('irow :',jcol,' solvecnew :',solvecnew[jcol]," solvecguess ",solvecguess[jcol])
        print ("-----------------------------")
    return()
