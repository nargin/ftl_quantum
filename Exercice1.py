from dotenv import load_dotenv
import os
from qiskit_ibm_runtime import QiskitRuntimeService

load_dotenv()

IBMQ_TOKEN = os.getenv("IBMQ_TOKEN")
if not IBMQ_TOKEN:
    print(IBMQ_TOKEN)
    raise ValueError("IBMQ_TOKEN is not set")

service = QiskitRuntimeService(channel="ibm_quantum", token=IBMQ_TOKEN)
all_backends = service.backends(simulator=False)
print("Real quantum computers:")
for backend in all_backends:
    print("\t" + backend.name + " has " + str(backend.n_qubits) +
          " qubits and " + str(backend.status().pending_jobs) +
          " pending jobs")

all_backends = service.backends(simulator=True, operational=True)
print("Simulated quantum computers:")
if not all_backends:
    print("\tNo simulated quantum computers available")
for backend in all_backends:
    print("\t" + backend.name + " has " +
          str(backend.status().pending_jobs) + " pending jobs")
