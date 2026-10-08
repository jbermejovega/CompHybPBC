# SVRAFTJ — Relational Pauli Polycategory V1

Status: compatibility scaffold; **not a full rewrite** of the legacy PBC algorithms.

## Legacy source boundary
Upstream: jbermejovega/CompHybPBC main@68d7d129b58f1fc11fedb1b4ee7cd842ff83b858.
Author and copyright: Filipa C. R. Peres, 2022; MIT terms in README.
Preserve Main.py, input_prep_t1.py, input_prep_t2.py and c_and_c.py unchanged.
The historical stack is Python 3.7.10 and Qiskit 0.26.2.

## New typed kernel
The SVRAFTJ name is retained literally; no definition was found in the
inspected legacy README or source headers.

Pauli(x,z,p) denotes i^p X^x Z^z with p modulo 4.
Multiplication uses p'=p+q+2(z·x') modulo 4.
Commutation uses the symplectic parity x·z'+z·x' modulo 2.
Hermitian measurement ports require p mod 2 = x·z mod 2.

The new layer is independent of Qiskit, preserves typed qubit arity and
returns HOLD_QUNO when the contextual relation witness is missing.
The term 'polycategory' denotes a **proposed interface discipline**:
the code does not prove polycategorical associativity/coherence or
replace adaptive PBC measurement scheduling.

## Migration phases
1. Pin legacy fixtures, environment and baseline outputs.
2. Map legacy Hermitian Pauli binary/sign convention into typed Pauli.
3. Cross-check products, commutators, dependencies and sign correlations.
4. Port Clifford+T preparation and adaptive measurement semantics.
5. Compare run_pbc and hybrid_pbc distributions with reproducible seeds.
6. Review Qiskit API changes and statistical tolerances separately.
7. Publish only after end-to-end tests and scientific review.

No simulator, quantum device, network, or legacy algorithm is executed by
this source-only scaffold. No physical or categorical equivalence certified.

PIORNALEGO ES CANON · SOURCE != CERTIFICATION · SAFE_REPLAY.
