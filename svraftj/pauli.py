"""SVRAFTJ relational Pauli polycategory: independent modern compatibility kernel.

Representation: i**phase * X**x Z**z, phase in Z4.
Y = iXZ, and Hermitian Paulis have phase parity x.z (mod 2).
No Qiskit dependency, no quantum execution, no legacy mutation.
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Pauli:
    x: tuple[int,...]
    z: tuple[int,...]
    phase: int = 0

    def __post_init__(self):
        if not self.x or len(self.x)!=len(self.z):
            raise ValueError("QUBIT_REGISTER_MISMATCH")
        if any(type(b) is not int or b not in (0,1) for b in self.x+self.z):
            raise ValueError("BINARY_PAULI_BITS_REQUIRED")
        if type(self.phase) is not int or self.phase not in range(4):
            raise ValueError("PHASE_Z4_REQUIRED")

    @property
    def n(self): return len(self.x)

    @property
    def hermitian(self):
        return self.phase%2 == sum(a*b for a,b in zip(self.x,self.z))%2

    def commutes(self,other):
        self._compatible(other)
        return sum(a*b+c*d for a,b,c,d in zip(self.x,other.z,self.z,other.x))%2==0

    def _compatible(self,other):
        if not isinstance(other,Pauli) or self.n!=other.n:
            raise ValueError("PAULI_PORT_MISMATCH")

    def multiply(self,other):
        self._compatible(other)
        p=(self.phase+other.phase+2*sum(a*b for a,b in zip(self.z,other.x)))%4
        return Pauli(tuple(a^b for a,b in zip(self.x,other.x)),
                     tuple(a^b for a,b in zip(self.z,other.z)),p)

def typed_attitude(left:Pauli,right:Pauli,*,context:str,witness:str="")->dict:
    if not context:
        return {"verdict":"REJECT","reason":"CONTEXT_REQUIRED"}
    if not isinstance(left,Pauli) or not isinstance(right,Pauli):
        return {"verdict":"REJECT","reason":"PAULI_TYPES_REQUIRED"}
    try:
        commuting=left.commutes(right)
    except ValueError as exc:
        return {"verdict":"REJECT","reason":str(exc)}
    if not left.hermitian or not right.hermitian:
        return {"verdict":"REJECT","reason":"MEASUREMENT_REQUIRES_HERMITIAN_PAULI"}
    return {"verdict":"ADMIT_SOURCE_PLAN" if witness else "HOLD_QUNO",
            "context":context,"relation":"COMMUTES" if commuting else "ANTICOMMUTES",
            "symplectic_parity":0 if commuting else 1,
            "left":left,"right":right,"witness":witness,
            "no_measurement_executed":True,"no_authority_transport":True}
