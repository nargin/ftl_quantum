import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt

def balanced_oracle(circuit, n):
	for qubit in range(n):
		circuit.cx(qubit, n)

def constant_oracle(circuit, n):
	pass

def deutsch_jozsa_circuit(n, oracle):
	circuit = qiskit.QuantumCircuit(n + 1, n)
	circuit.h(range(n))

	circuit.x(n)
	circuit.h(n)

	oracle(circuit, n)

	circuit.h(range(n))

	circuit.measure(range(n), range(n))

	return circuit

n = 3

# constant_circuit = deutsch_jozsa_circuit(n, constant_oracle)
# circuit = constant_circuit

balanced_circuit = deutsch_jozsa_circuit(n, balanced_oracle)
circuit = balanced_circuit

circuit_image = "circuit.png"
circuit_drawer(circuit, output='mpl', filename=circuit_image)
print(f"Le circuit a été sauvegardé dans {circuit_image}")

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
plt.title("Distribution des résultats")
plt.ylabel("Nombre d'occurrences")
histogram_image = "histogram.png"
plt.savefig(histogram_image)
plt.close()
print(f"L'histogramme a été sauvegardé dans {histogram_image}")