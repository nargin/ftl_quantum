import qiskit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt
import numpy as np

def oracle_3qubit(circuit, n):
    """Example oracle for 3 qubits (marks state |111>)"""
    circuit.cz(0, 2)
    circuit.cz(1, 2)

def oracle_2qubit(circuit, n):
    """example subject |11>"""
    circuit.cz(0, 1)

def diffuser(circuit, n):
    """Implements the Grover diffuser"""
    circuit.h(range(n))	
    circuit.x(range(n))

    circuit.h(n-1)
    circuit.mcx(list(range(n-1)), n-1)
    circuit.h(n-1)

    circuit.x(range(n))
    circuit.h(range(n))

# Qiskit code for Grover's algorithm
# Not me who wrote this

def grover_circuit(n, oracle):
    circuit = qiskit.QuantumCircuit(n, n)
    
    # Initialize superposition for all
    # oblige truc de dingue (chokbar)
    circuit.h(range(n))
    
    # Number of iterations
    iterations = int(np.pi/4 * np.sqrt(2**n))
    print(f"Random iterations: {iterations}", " (no)")
    
    for _ in range(iterations):
        print("Iteration", _)
        oracle(circuit, n)
        diffuser(circuit, n)
    
    circuit.measure(range(n), range(n))
    
    return circuit

service = QiskitRuntimeService()

qubits = 2

if qubits < 2:
    raise ValueError("More qubits AHAHAHA")

circuit = grover_circuit(qubits, oracle_2qubit)

circuit_image = "circuit_grover.png"
circuit_drawer(circuit, output='mpl', filename=circuit_image)
print(f"Le circuit a été sauvegardé dans {circuit_image}")

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
histogram_image = "histogram_grover.png"
plt.savefig(histogram_image)
print(f"L'histogramme a été sauvegardé dans {histogram_image}")