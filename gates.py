import utilities
import math
def qubit():
    return [[0,0]]
def I():
    return [[1,0],[0,1]]
def H():
    return utilities.scale([[1,1],[1,-1]],math.sqrt(2))
def NOT():
    return [[0,1],[1,0]]
def Z():
    return [[1,0],[0,-1]]
def rGate(theta:float):
    return [[math.cos(theta),math.sin(theta)],[-math.sin(theta),math.cos(theta)]]

def zeroQubit():
    return [[1,0]]
def oneQubit():
    return [[0,1]]

def apply_gate(gate:utilities.Matrix,qubits:utilities.Matrix,position_of_qubit_to_modify,control_qubits=[]):
    fullGate = make_full_gate(gate, round(math.log(len(qubits[0]),2)), position_of_qubit_to_modify, control_qubits)
    return utilities.matmul(qubits,fullGate), fullGate

def make_full_gate(gate:utilities.Matrix,total_number_of_qubits, qubitPosition, controlQubits=[]):
    tensorView = make_complete_identity_tensor(total_number_of_qubits)
    matrixView = []
    for row in tensorView:
        for i in range(0,len(controlQubits)):
            if row[controlQubits[i]] != [1,0]:
                break
        else:
            row[qubitPosition] = utilities.matmul(row[qubitPosition],gate)
        newRow = row[0]
        for i in range(1,len(row)):
            newRow = utilities.tensor(newRow,row[i])
        matrixView.append(newRow)
    return matrixView[0]
    

def make_complete_identity_tensor(size):
    prodMatrix = []
    for i in range(0, size):
        newRow = bin(int(i))[2:].zfill(size)
        newMatrRow = []
        for j in range(0,len(newRow)):#Pseudo-code until I figure out what actually works
            if newRow[j] == 0:
                newMatrRow.append(zeroQubit())
            else:
                newMatrRow.append(oneQubit())
        prodMatrix.append(newMatrRow)
    return prodMatrix
        