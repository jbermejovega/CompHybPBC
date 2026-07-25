# ARAKNE_FUSION_UAP_COMPHYBPBC_GLUE_V1

## Status

`ACTIVE_ARCHITECTURAL_GLUE`

This document lifts the Pauli-based computation architecture in `CompHybPBC` into an ARAKNE typed-fusion layer while preserving the existing Pauli/PyZX-compatible implementation as a strict special case.

## Canonical lift

```text
ordinary ZX / PyZX spider fusion
        ⊂
ARAKNE typed spider fusion
        ↓
fusion-category semantic layer
        ↓
JJBV hypergroup-Pauli projection
        ↓
logical topological operators
        ↓
generalized lattice-surgery measurement plans
        ↓
PACAPDG contextual glue
        ↓
UAP
   ├── ADMIT
   ├── HOLD_WITH_OBSTRUCTION
   └── REJECT
```

## Semantic boundary

ARAKNE fusion lifts spider fusion; it does not erase the original ZX semantics.

```text
ZX spider fusion
≠ arbitrary anyon fusion
≠ runtime execution
≠ physical lattice surgery
```

The abelian Pauli sector remains available through a compatibility embedding. Nonabelian sectors require explicit fusion-category data.

## Required nonabelian data

A nonabelian logical sector must declare:

- simple objects / topological charges;
- duals;
- fusion multiplicities `N_ab^c`;
- `F`-symbols;
- `R`-symbols where braiding is used;
- quantum dimensions;
- boundary and condensation types;
- coherence witnesses;
- provenance and replay digest.

A hypergroup-Pauli object is a decategorified or projected logical layer. It is not a replacement for the full braided fusion-category model.

## Logical measurements

Supported measurement-plan classes are kept distinct:

1. charge-projector / Verlinde-algebra measurement;
2. Wilson-loop or monodromy measurement;
3. generalized lattice surgery;
4. braiding;
5. Dehn twist;
6. cocycle-twisted injection;
7. vacuum pair creation.

```text
braid
≠ Dehn twist
≠ charge projection
≠ cocycle injection
≠ pair creation
```

## Generalized lattice surgery

A canonical ancilla-assisted charge measurement is represented as:

```text
vacuum
→ create anyon–anti-anyon pair with total trivial charge
→ route one member to the surgery boundary
→ perform joint fusion-channel or topological-charge measurement
→ update the encoded fusion-space sector
→ record consumed ancilla and topological resources
```

The comparison with Hawking radiation is retained only as an analogy involving vacuum-pair creation and separation across an effective boundary. No gravitational equivalence is claimed.

## PACAPDG contract

PACAPDG glues typed measurement plans and logical interfaces while preserving:

- local identities;
- fusion-channel multiplicity;
- boundary typing;
- resource accounting;
- obstruction witnesses;
- provenance;
- deterministic replay.

No identity transport or plural collapse is permitted.

## UAP contract

UAP evaluates the resulting plan:

```text
ADMIT
HOLD_WITH_OBSTRUCTION
REJECT
```

Typical HOLD conditions include:

- missing `F`/`R` coherence;
- unresolved boundary-condensation compatibility;
- unsupported fusion multiplicity;
- absent resource witness;
- ambiguous projection from fusion-category data to hypergroup-Pauli labels;
- unsupported backend target.

## Repository relation

- repository: `jbermejovega/CompHybPBC`;
- default branch: `main`;
- sibling architectural consumer: `jbermejovega/Mi_TFM` PR #3;
- this glue does not copy, execute, or replace existing source code;
- this glue does not establish a theorem, decoder, physical protocol, or deployment.

## Invariants

```yaml
ordinary_zx_is_special_case: true
arakne_lifts_spider_fusion: true
fusion_category_not_reduced_to_hypergroup: true
vacuum_pair_total_charge_trivial: true
resource_consumption_recorded: true
f_and_r_coherence_required: true
identity_transport: false
plural_collapse: false
hawking_equivalence_claimed: false
runtime_execution_implied: false
physical_validation_implied: false
```
