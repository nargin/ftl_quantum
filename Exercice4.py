import qiskit
from qiskit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt

circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])

circuit_image = "circuit.png"
circuit_drawer(circuit, output='mpl', filename=circuit_image)

service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False)

manager = generate_preset_pass_manager(backend=backend, optimization_level=1)
transpiled_circuit = manager.run(circuit)

sampler = Sampler(backend)
job = sampler.run([transpiled_circuit], shots=500)
print(f"Job ID {job.job_id()}")

results = job.result()
result = results[0]
counts = result.data.c.get_counts()

print("Results:")
print(counts)

plt.figure(figsize=(10, 6))
plot_histogram(counts)
histogram_image = "histogram_ex04.png"
plt.savefig(histogram_image)

zero_prob = counts.get('00', 0)
one_prob = counts.get('11', 0)
print(f"\nProbabilities:\n00: {zero_prob:.2f}\n11: {one_prob:.2f}")