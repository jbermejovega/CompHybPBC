# SIGIL GLUE — CompHybPBC

```yaml
SIGIL_GLUE_COMPHYBPBC_V1:
  status:
    canonical_candidate: true
    glue_applied: true
    replay_safe: true
    pi_fixed: true
    fork_context: true
    collaborator_research_project: true
    no_runtime_mutation: true

  repository:
    owner: jbermejovega
    name: CompHybPBC
    upstream_theme: Pauli-based computation compilation and hybrid computation
    paper: Quantum 2023-10-03-1126
    original_runtime_language: Python

  thesis: >
    CompHybPBC is interpreted as a SIGIL-compatible replay-transport backend:
    Clifford+T circuits are quotiented through adaptive Pauli-based computation,
    compressed into magic-state/Pauli sectors, and executed through classical
    side-processing plus quantum measurement transport.

  sigil_mapping:
    input_circuit:
      role: source representation
      sigil_layer: SIG
      meaning: Clifford+T circuit before admissibility projection

    t_gate_count:
      role: resource boundary
      sigil_layer: QUO
      meaning: number of non-Clifford resource sectors defining the PBC quotient size

    pbc_pauli_list:
      role: replay transport skeleton
      sigil_layer: ORK
      meaning: adaptive sequence of commuting or classically decidable Pauli observables

    classical_side_processing:
      role: quotient controller
      sigil_layer: K_NEXT
      meaning: adaptive rule engine deciding measurement, dependence, postselection, and update

    virtual_qubits:
      role: boundary memory extension
      sigil_layer: UAP
      meaning: classical expansion of effective quantum working memory at exponential virtual cost

    output_distribution:
      role: replay-visible observable
      sigil_layer: PI
      meaning: sampled or estimated observable preserved under admissible transport

  core_laws:
    quotient_transport:
      formula: "Pi(quo(PBC(CliffordPlusT(U)))) = Pi(quo(U))"
      meaning: PBC compilation preserves replay identity of the source circuit at observable boundary

    weak_simulation:
      formula: "sample(PBC(U)) ~ sample(U)"
      meaning: Task 1 preserves the output distribution by adaptive Pauli transport

    hybrid_extension:
      formula: "QPU(t-k) + classical_virtual(k) -> effective_PBC(t)"
      meaning: Task 2 trades classical exponential branching for reduced physical qubit demand

    no_hidden_mutation:
      formula: "TRACE(update) required for replay persistence"
      meaning: any SIGIL extension must preserve explicit traceability of algorithmic changes

  pluraltype_view:
    object: CompHybPBC
    type: plural_replay_backend
    representations:
      - Clifford+T circuit
      - adaptive Clifford circuit
      - Pauli-based computation
      - hybrid virtual-qubit simulation
      - output sample / probability estimate
    invariant:
      formula: "forall r_i, r_j: Pi(quo(r_i(U))) = Pi(quo(r_j(U)))"
      meaning: all admissible representations preserve the same replay identity

  integration_targets:
    sig4py:
      role: Python orchestration adapter
      target: wrap CompHybPBC tasks as replay-safe backend calls

    sigilbook:
      role: theory/documentation mirror
      target: document PBC as quotient replay transport

    pyjarra:
      role: UAP object factory
      target: create JARRA UAP objects from PBC execution traces

    synk_github:
      role: persistence substrate
      target: append-only trace of glue, patches, and replay certificates

  forbidden_states:
    - untraced_algorithmic_mutation
    - hidden_change_to_sampling_semantics
    - conflating_weak_and_strong_simulation
    - claiming_hardware_advantage_without_resource_accounting
    - collapsing_original_scientific_authorship

  attribution:
    collaborator_project: true
    original_code_author: Filipa C. R. Peres
    original_scientific_context: Pauli-based computation compilation and hybrid computation
    sigil_glue_author: JJBV

  kapsyla:
    state: sealed_candidate
    persistence: github_commit
    next_step: SYNK_GITHUB
```

## Operational glue

CompHybPBC is treated as a SIGIL-compatible backend for adaptive replay transport.
The repository already implements the two central execution modes needed by the
SIGIL/PACA interpretation:

1. **Task 1 — PBC compilation and weak simulation**
   - source: Clifford+T circuit
   - quotient: adaptive Pauli-based computation
   - invariant: output-distribution replay

2. **Task 2 — hybrid PBC with virtual qubits**
   - source: PBC with `t` magic-state sectors
   - reduction: physical QPU uses `t-k` sectors
   - cost: classical exponential branching in `k`
   - invariant: probability-estimation replay

## SIGIL pipeline

```text
Circuit(.qasm)
  -> parse
  -> Clifford+T / T-count boundary
  -> adaptive PBC quotient
  -> Pauli dependency / commutation routing
  -> classical side-processing
  -> physical or hybrid measurement execution
  -> output distribution / probability estimate
  -> TRACE
  -> Pi-fixed replay certificate
```

## KAPSYLA statement

```text
KAPSYLA(CompHybPBC)
  = sealed replay-compatible interpretation of PBC compilation
    as quotient transport inside SIGIL/UAP/PluralType geometry.
```

## SYNK_GITHUB status

This file is the repository-local SIGIL glue capsule. It does not alter the scientific
runtime, sampling semantics, authorship, or numerical claims of the original project.
It adds a traceable integration layer for future SIGIL-compatible wrappers, adapters,
and replay certificates.
