# Q114: The chain Young metric attains its infimum

**Theorem.** For two rational step words of equal length, the infimum in Messick's chain Young metric is attained if the distances between the letters occurring in the two endpoint words are rational. Distances involving all other alphabet letters may be arbitrary. Furthermore, an optimal chain uses only endpoint letters.

This answers [Catalog Q114](https://github.com/10m-u/open-problems-catalog/blob/ca8d4d44ba3db527f19f28928c240168f545ecfe/problems/mathematics/logic-foundations-set-theory-part-1.md#q114), i.e., [Messick, Continuous Automata, Compactness, and Young Measures, §3.3, Definition 3.7 and footnote 2](https://ecommons.cornell.edu/server/api/core/bitstreams/e61833ea-c15d-40a3-8e93-e0310d91055d/content#page=46). We use the step-word convention of interval values up to endpoints. A push on a constant rational interval of length a costs a times the letter distance; swapping two equal-length adjacent constant rational intervals costs a².

## 1. Transport objective

The length-zero case needs no moves. Partition the source into ordered constant intervals indexed by i=1,...,m, and the target by j=1,...,n. Write a_i,b_j for their positive rational lengths and A_i,B_j for their letters. Consider the transportation polytope P of nonnegative m-by-n matrices X=(x_ij) with row sums a_i and column sums b_j. It is nonempty (for example use the product coupling), compact and rational.

Define
```
F(X) = Σ_(i,j) d(A_i,B_j) x_ij + Σ_(i<k, j>l) x_ij x_kl.
```
Then the chain metric equals min_{X∈P} F(X).

**Lower bound.** For any fixed finite chain choose a common rational grid of width h so all endpoints in the chain and the endpoint partitions are on the grid. Distinguish the grid cells by token identities. A push on q cells can be implemented by q individual pushes for equal cost. A block swap of two q-cell blocks permutes them in exactly q² grid-cell swaps, preserving within-block order, at the same total cost. If a swap exchanges equal letters we may count it as an identity exchange in the abstract token bookkeeping; the word itself is unchanged. Therefore the chain induces a permutation of the original tokens and gives a rational matrix x_ij equal to h times the number of tokens from i to j. The sum of push costs for each token is at least h d(A_i,B_j) by the triangle inequality. For each i<k and j>l, all pairs of tokens from cells (i,j) and (k,l) reverse order. Every reversed pair incurs at least one adjacent grid-cell swap; the pairs counted for different index quadruples are disjoint. Their contribution is at least h²(x_ij/h)(x_kl/h)=x_ij x_kl. Thus any chain costs at least F(X).

**Upper bound for rational X.** Choose a grid width h dividing all x_ij (hence all endpoint lengths). In each source run i, allocate consecutive blocks of x_ij/h grid cells for target runs j in increasing order. Order the tokens in target run j by increasing source index i, preserving order within each group (i,j). The resulting permutation reverses exactly the pairs i<k, j>l, because pairs sharing a source or target run retain relative order. Relabel each token directly to its target letter at the start. Then implement the permutation by adjacent inversion swaps; for a permutation of distinct tokens, swapping an adjacent inverted pair decreases the inversion count by one, so this uses exactly the inversion count. Legal swaps on distinct letters cost h² each. Swaps between equal letters may simply be omitted as word moves while the conceptual token permutation continues, at no additional cost. The resulting chain costs at most F(X). Rational points are dense in P: on the support of any given point, the row and column constraints are rational linear equations, and rational solutions approximate that point while preserving strict positivity on the support. Taking infima, continuity and compactness prove the displayed equality, without requiring rational distances for equality itself.

## 2. A rational optimizer

For rational endpoint distances, F is a quadratic polynomial with rational coefficients. Let X* minimize F over P. Restrict to the affine space E defined by the rational row and column constraints and by setting the zero coordinates of X* equal to zero. The positive coordinates of X* are strictly positive, so a neighborhood of X* in E is feasible. The gradient of F at X* is orthogonal to the tangent space of E. That tangent space has a rational basis, computed from the constraint matrix. Therefore the conditions “X∈E” and “the directional derivatives of F vanish along the basis of the tangent space” form a consistent rational **linear** system for X, since ∇F is affine-linear.

The solutions of this rational system have a rational point arbitrarily close to X*: use rational Gaussian elimination to obtain a rational particular solution and a rational basis of its homogeneous solution space, then approximate free coordinates by rationals. Pick a rational solution Y close enough for all required positive coordinates to stay positive. Along the segment from X* to Y every point solves the stationarity system by linearity, and the derivative along the segment is zero. So F(Y)=F(X*). By the rational construction in §1, Y yields a finite chain with cost at most F(X*); by the lower bound its cost is exactly F(X*).

## 3. Example and sharpness

For source AB and target BA, with both runs of length 1/2, write x_12=x_21=t and x_11=x_22=1/2−t. The objective is d(1−2t)+t², where d=d(A,B). For 0<d<1/2 it is uniquely minimized at t=d, with value d−d². For d=1/3 the optimal value is 2/9 and cannot be reached on the original half-unit grid (whose best cost is 1/4). A grid of sixths suffices. If d is irrational strictly between 0 and 1/2, this instead gives a genuine nonattainment example: every finite chain has a rational transport matrix, so its cost is strictly above the unique real minimum, which is still the infimum by §1.

No claim of priority, peer review, or machine formalization is made. The optional replay independently checks the objective against a shortest-path computation on small grids.
