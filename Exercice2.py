from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

import os
from dotenv import load_dotenv
load_dotenv()

IBMQ_TOKEN = os.getenv("IBMQ_TOKEN")
if not IBMQ_TOKEN:
    print(IBMQ_TOKEN)
    raise ValueError("IBMQ_TOKEN is not set")

qc = QuantumCircuit(2)

qc.h(0)
qc.cx(0, 1)
qc.cx(1, 0)

qc.measure_all()
# plot_histogram(qc)

# QiskitRuntimeService.save_account(channel="ibm_quantum", token=IBMQ_TOKEN, set_as_default=True)
 
service = QiskitRuntimeService()
backend = service.backend("ibmq_qasm_simulator")
sampler = Sampler(backend)
job = sampler.run([qc], shots=500)
print(job.result())
