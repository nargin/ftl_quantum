from qiskit import QuantumCircuit, transpile
from qiskit_ibm_provider import IBMProvider
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("IBMQ_TOKEN")

IBMProvider.save_account(token)
provider = IBMProvider()

circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])

circuit_image = "circuit_real.png"
circuit_drawer(circuit, output='mpl', filename=circuit_image)
print(f"Le circuit a été sauvegardé dans {circuit_image}")

backend = provider.get_backend('ibmq_lima')

transpiled_circuit = transpile(circuit, backend)

num_shots = 500
job = backend.run(transpiled_circuit, shots=num_shots)
result = job.result()
counts = result.get_counts(circuit)

print("Résultats:")
print(counts)

plt.figure(figsize=(10, 6))
plot_histogram(counts)
plt.title("Distribution des résultats sur un dispositif quantique réel")
plt.ylabel("Nombre d'occurrences")
histogram_image = "histogram_real.png"
plt.savefig(histogram_image)
plt.close()
print(f"L'histogramme a été sauvegardé dans {histogram_image}")

zero_zero_prob = counts.get('00', 0) / num_shots
one_one_prob = counts.get('11', 0) / num_shots
print(f"\nProbabilités :\n00: {zero_zero_prob:.2f}\n11: {one_one_prob:.2f}")

other_results = {k: v/num_shots for k, v in counts.items() if k not in ['00', '11']}
if other_results:
    print("\nAutres résultats (bruit quantique):")
    for state, prob in other_results.items():
        print(f"{state}: {prob:.2f}")