import cirq_ionq
service = cirq_ionq.Service(api_key="oqrmJf61uZ6COilYZgkGIOkQUg8hAOxS")

import cirq

q0, q1 = cirq.LineQubit.range(2)
circuit = cirq.Circuit(
    cirq.H(q0),
    cirq.CNOT(q0, q1),
    cirq.measure(q0, q1, key='x') 
)

print(circuit)

result = service.run(
    circuit=circuit,
    target="simulator",
    repetitions=1000,
    name="Hello simulator - Cirq"
)

print(result.histogram(key='x'))