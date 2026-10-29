from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

initial_state = Statevector.from_label('10')

qc = QuantumCircuit(2)
qc.cx(1, 0)

final_state = initial_state.evolve(qc)

print("Initial state:", initial_state)
print("Quantum circuit:")
print(qc.draw())
print("Final state:", final_state)

plot_bloch_multivector(initial_state)
plt.show()

plot_bloch_multivector(final_state)
plt.show()