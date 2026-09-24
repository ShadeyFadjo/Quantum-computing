# from qiskit_ionq import IonQProvider
# from qiskit import QuantumCircuit

# provider = IonQProvider()

# # print(provider.backends())

# simulator_backend = provider.get_backend("simulator")

# # Create a basic Bell State circuit:
# qc = QuantumCircuit(2, name="IonQ Qiskit guide - simulator example")
# qc.h(0)
# qc.cx(0, 1)
# qc.measure_all()

# # Run the circuit on IonQ's platform:
# job = simulator_backend.run(qc, shots=10000)

# # Print the counts
# print(job.get_counts())

from qiskit import QuantumCircuit
from qiskit_ionq import IonQProvider

provider = IonQProvider()
simulator_backend = provider.get_backend("simulator")

# Define two quantum circuits
qc1 = QuantumCircuit(2, name="IonQ Qiskit guide - Bell state")
qc1.h(0)
qc1.cx(0, 1)
qc1.measure_all()

qc2 = QuantumCircuit(3, name="IonQ Qiskit guide - GHZ state")
qc2.h(0)
qc2.cx(0, 1)
qc2.cx(0, 2)
qc2.measure_all()

# Submit both circuits as a single job
job = simulator_backend.run([qc1, qc2])

# Print the results
print(job.get_counts())

# Or a specific job
print(job.get_counts(qc1))