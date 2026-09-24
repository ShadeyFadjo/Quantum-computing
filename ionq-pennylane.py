import pennylane as qp
import os

# Setup the device
dev = qp.device(
    'ionq.simulator',
    api_key=os.getenv("IONQ_API_KEY"),
    wires=2
)

@qp.set_shots(100)
@qp.qnode(dev)
def bell_state():
    qp.Hadamard(wires=0)
    qp.CNOT(wires=[0, 1])
    return qp.probs(wires=[0, 1])

print(bell_state())