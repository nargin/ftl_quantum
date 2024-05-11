import qiskit
from qiskit_aer import AerSimulator
from qiskit.visualization import circuit_drawer
import matplotlib.pyplot as plt
import numpy as np

circuit = qiskit.QuantumCircuit(2, 2)

circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])

backend = AerSimulator()

num_shots = 500

job = backend.run(circuit, shots=num_shots)
result = job.result()
counts = result.get_counts(circuit)

print(counts)


zero_counts = counts.get('00', 0) / num_shots
one_counts = counts.get('11', 0) / num_shots

plt.bar(['00', '11'], [zero_counts, one_counts])

for i, v in enumerate([zero_counts, one_counts]):
    plt.text(i, v + 0.01, str(round(v, 2)), ha='center')

plt.yticks(np.arange(0, plt.gca().get_ylim()[1], 0.15))
plt.ylabel('Probabilities')
plt.savefig('histogram.png')
plt.grid(axis='y', linestyle='dashed', alpha=0.6)
plt.show()

filename = "circuit.png"
circuit_drawer(circuit, output='mpl', filename=filename)