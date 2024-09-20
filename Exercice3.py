import qiskit
# from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
# from qiskit_aer.noise import NoiseModel
import matplotlib.pyplot as plt

circuit = qiskit.QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])

circuit_image = "circuit.png"
circuit_drawer(circuit, output='mpl', filename=circuit_image)

# Noisy simulation
# service = QiskitRuntimeService()
# backend = service.least_busy(operational=True, simulator=False)
# noise_model = NoiseModel.from_backend(backend)
# backend = AerSimulator(noise_model=noise_model)

backend = AerSimulator()

# Simulation
num_shots = 500
job = backend.run(circuit, shots=num_shots)
result = job.result()
counts = result.get_counts(circuit)

print("Résultats:")
print(counts)

# Création de l'histogramme
plt.figure(figsize=(10, 6))
plot_histogram(counts)
histogram_image = "histogram_ex03.png"
plt.savefig(histogram_image)

# Calcul et affichage des probabilités
zero_prob = counts.get('00', 0) / num_shots
one_prob = counts.get('11', 0) / num_shots
print(f"\nProbabilités :\n00: {zero_prob:.2f}\n11: {one_prob:.2f}")
