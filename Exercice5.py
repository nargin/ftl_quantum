import qiskit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
# from qiskit_aer import AerSimulator
# from qiskit_aer.noise import NoiseModel
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt


def bal_oracle(circuit, n):
    for qubit in range(n):
        circuit.cx(qubit, n)


def miracle(circuit, n):
    circuit.cx(0, 1)
    circuit.z(1)


def deutsch_jozsa_circuit(n, oracle):
    circuit = qiskit.QuantumCircuit(n + 1, n)

    circuit.x(n)
    circuit.h(range(n + 1))

    oracle(circuit, n)

    circuit.h(range(n))

    circuit.measure(range(n), range(n))

    return circuit


service = QiskitRuntimeService()

qubits = 3

circuit = deutsch_jozsa_circuit(qubits, miracle)

circuit_image = "circuit_ex05.png"
circuit_drawer(circuit, output='mpl', filename=circuit_image)

# Simulation
# backend = AerSimulator()
# num_shots = 500
# job = backend.run(circuit, shots=num_shots)
# result = job.result()
# counts = result.get_counts(circuit)

# Real device
backend = service.least_busy(operational=True, simulator=False)

manager = generate_preset_pass_manager(backend=backend, optimization_level=1)
transpiled_circuit = manager.run(circuit)

sampler = Sampler(backend)
job = sampler.run([transpiled_circuit], shots=500)
print(f"Job ID {job.job_id()}")

results = job.result()
result = results[0]
counts = result.data.c.get_counts()

print("Résultats:")
print(counts)

plt.figure(figsize=(10, 6))
plot_histogram(counts)
histogram_image = "histogram_ex05.png"
plt.savefig(histogram_image)
