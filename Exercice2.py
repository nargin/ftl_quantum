import qiskit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt

# Création du circuit
circuit = qiskit.QuantumCircuit(1, 1)
circuit.h(0)
circuit.measure(0, 0)

# Affichage du circuit (sauvegarde dans un fichier)
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

# Création de l'histogramme
plt.figure(figsize=(10, 6))
plot_histogram(counts)
plt.title("Distribution des résultats")
plt.ylabel("Nombre d'occurrences")
histogram_image = "histogram.png"
plt.savefig(histogram_image)
plt.close()
print(f"L'histogramme a été sauvegardé dans {histogram_image}")

# Calcul et affichage des probabilités
zero_prob = counts.get('0', 0) / num_shots
one_prob = counts.get('1', 0) / num_shots
print(f"\nProbabilités :\n0: {zero_prob:.2f}\n1: {one_prob:.2f}")