import Std

namespace TokenInversions
/-- Tokens carry their target order as a natural-number key. -/
def below (a : Nat) (xs : List Nat) := (xs.filter (· < a)).length
def inversions : List Nat → Nat
  | [] => 0
  | a :: xs => below a xs + inversions xs

theorem below_swap (x a b : Nat) (p s : List Nat) :
    below x (p ++ a :: b :: s) = below x (p ++ b :: a :: s) := by
  simp only [below, List.filter_append, List.length_append]
  by_cases ha : a < x <;> by_cases hb : b < x <;> simp [ha, hb]

/-- An adjacent inverted-token swap removes precisely one inversion in
any surrounding context, including in the presence of equal target keys. -/
theorem swap_decreases (p s : List Nat) (a b : Nat) (h : b < a) :
    inversions (p ++ a :: b :: s) = inversions (p ++ b :: a :: s) + 1 := by
  induction p with
  | nil =>
    have hn : ¬ a < b := by omega
    simp [inversions, below, h, hn]
    omega
  | cons x xs ih =>
    simp only [List.cons_append, inversions]
    rw [below_swap, ih]
    omega
#print axioms swap_decreases
end TokenInversions
