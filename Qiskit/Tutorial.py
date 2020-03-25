import qiskit
import numpy
from matplotlib import pyplot as plt
from qiskit import QuantumProgram
qp = QuantumProgram()
qr = qp.create_quantum_register('qr',2)
cr = qp.create_classical_register('cr',2)
qc = qp.create_circuit('HelloWorldCircuit', [qr],[cr])
backend = 'ibmqx5'token = '4f576d93e6d8084fbba56446a291ab1b0d48ce11f9a6d7e93e46b3d0de2858bfa183632eb9a44120a8d37a26ce869a631e8e4b81568937629432cfe7f86f1379'qp.set_api(token,url='https://quantumexperience.ng.bluemix.net/api')
qc.h(qr[1])
qc.cx(qr[1], qr[0])
qc.measure(qr[0],cr[0])
qc.measure(qr[1],cr[1])
results = qp.execute(['HelloWorldCircuit'] ,backend ,timeout=2400)
print(results.get_counts('HelloWorldCircuit')
