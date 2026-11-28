# Lean certificate

**Adjacent token swaps**

Swapping one adjacent inverted pair of natural-number token keys decreases the inversion count by exactly one, for arbitrary preceding and following token lists.

The transport formula and rational attainment require the other arguments in the paper.

The principal checked declaration is `TokenInversions.swap_decreases`. See [From chains to transport and back](../paper/manuscript.tex#L45) in the manuscript. [Lean source](Q114.lean) · [Verification workflow](../.github/workflows/lean.yml)

Replay with Lean 4.30.0 and its standard library from the repository root.

```sh
lean -DwarningAsError=true formalization/Q114.lean
```
