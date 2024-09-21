import qiskit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt

circuit = qiskit.QuantumCircuit(1, 1)
circuit.h(0)
circuit.measure(0, 0)

circuit_image = "circuit_ex02.png"
circuit_drawer(circuit, output='mpl', filename=circuit_image)

# Simulation
backend = AerSimulator()
num_shots = 500
job = backend.run(circuit, shots=num_shots)
result = job.result()
counts = result.get_counts(circuit)

print("Résultats:")
print(counts)

plt.figure(figsize=(10, 6))
plot_histogram(counts)
histogram_image = "histogram_ex02.png"
plt.savefig(histogram_image)

zero_prob = counts.get('0', 0) / num_shots
one_prob = counts.get('1', 0) / num_shots
print(f"\nProbabilités :\n0: {zero_prob:.2f}\n1: {one_prob:.2f}")
