import utilities
import math
def qubit():
    return [[0,0]]
def H(mat1:utilities.Matrix):
    hadamard=utilities.scale([[1,1],[1,-1]],math.sqrt(2))
    return utilities.matmul(mat1,hadamard)
def NOT(mat1:utilities.Matrix):
    notGate=[[0,1],[1,0]]
    return utilities.matmul(mat1,notGate)
def Zgate(mat1:utilities.Matrix):
    zgate=[[1,0],[0,-1]]
    return utilities.matmul(mat1,zgate)
def rGate(mat1:utilities.Matrix,theta:float):
    rgate=[[math.cos(theta),math.sin(theta)],[-math.sin(theta),math.cos(theta)]]
    return utilities.matmul(mat1,rgate)
def Control(mat1:utilities.Matrix,gateFunction,theta=None):#Gate function being one of the above gates
    mat2=[]
    if theta != None:
        mat2=[[1,0],[0,1],gateFunction(mat1,theta)]
    else: 
        mat2= [[1,0],[0,1],gateFunction(mat1)]
    return mat2
