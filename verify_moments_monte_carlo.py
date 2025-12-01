#!/usr/bin/env python3
import argparse
import math
import numpy as np
from sphere_tensor_moments import second_moment_sphere, fourth_moment_sphere_3d


def random_point_on_sphere(d: int = 3) -> np.ndarray:
    v = np.random.normal(size=d)
    return v / np.linalg.norm(v)


def tetrahedron_volume(a, b, c, d) -> float:
    """
    Volume of tetrahedron with vertices a,b,c,d in R^3:
    V = |det(b-a, c-a, d-a)| / 6
    """
    mat = np.stack([b - a, c - a, d - a], axis=1)
    det = np.linalg.det(mat)
    return abs(det) / 6.0


def estimate_moments_and_volume(n_samples: int, seed: int | None = None):
    if seed is not None:
        np.random.seed(seed)

    d = 3
    M2_emp = np.zeros((d, d))
    M4_emp = np.zeros((d, d, d, d))
    v2_list = []

    for _ in range(n_samples):
        # one random point for tensor moments
        r = random_point_on_sphere(d)
        outer2 = np.outer(r, r)             # r_i r_j
        outer4 = np.einsum("i,j,k,l->ijkl", r, r, r, r)

        M2_emp += outer2
        M4_emp += outer4

        # random tetrahedron volume
        A, B, C, D = [random_point_on_sphere(d) for _ in range(4)]
        V = tetrahedron_volume(A, B, C, D)
        v2_list.append(V * V)

    M2_emp /= n_samples
    M4_emp /= n_samples
    v2_emp = float(np.mean(v2_list))

    return M2_emp, M4_emp, v2_emp


def main():
    parser = argparse.ArgumentParser(
        description="Monte Carlo verification of tensor moments on the sphere "
                    "and E[V^2] for a random tetrahedron."
    )
    parser.add_argument("-n", "--samples", type=int, default=200_000,
                        help="number of Monte Carlo samples (default: 200000)")
    parser.add_argument("--seed", type=int, default=None,
                        help="random seed (optional)")
    args = parser.parse_args()

    M2_emp, M4_emp, v2_emp = estimate_moments_and_volume(
        args.samples, args.seed
    )

    # analytic tensors
    M2_theory = second_moment_sphere(3)
    M4_theory = fourth_moment_sphere_3d()

    print(f"Samples: {args.samples}")
    print("\nSecond moment E[r_i r_j]")
    print("Empirical:")
    print(M2_emp)
    print("Theoretical δ_ij / 3:")
    print(M2_theory)
    print("Frobenius norm of difference:",
          np.linalg.norm(M2_emp - M2_theory))

    print("\nFourth moment E[r_i r_j r_k r_l]")
    print("||Empirical - Theory||_F =",
          np.linalg.norm(M4_emp - M4_theory))

    print("\nE[V^2] for random tetrahedron (vertices on S^2)")
    print(f"Empirical E[V^2] ≈ {v2_emp:.6f}")
    print(f"Theoretical E[V^2] = 2/81 ≈ {2/81:.6f}")
    print(f"Difference ≈ {v2_emp - 2/81:.6e}")


if __name__ == "__main__":
    main()
