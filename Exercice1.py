from qiskit import QuantumCircuit
from dotenv import load_dotenv
from qiskit.visualization import plot_histogram
import os, sys
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

load_dotenv()

IBMQ_TOKEN = os.getenv("IBMQ_TOKEN")
if not IBMQ_TOKEN:
    print(IBMQ_TOKEN)
    raise ValueError("IBMQ_TOKEN is not set")
 
service = QiskitRuntimeService()
print("Provider:", provider)
all_backends = service.backends(simulator=False)
print("Real quantum computers:")
for backend in all_backends:
    print("\t" + backend.name + " has " + str(backend.n_qubits) + " qubits and " + str(backend.status().pending_jobs) + " pending jobs")

all_backends = service.backends(simulator=True, operational=True)
print("Simulated quantum computers:")
for backend in all_backends:
    print("\t" + backend.name + " has " + str(backend.status().pending_jobs) + " pending jobs")