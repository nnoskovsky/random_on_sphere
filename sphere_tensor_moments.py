#!/usr/bin/env python3
import numpy as np


def kron_delta(d: int = 3) -> np.ndarray:
    return np.eye(d)


def second_moment_sphere(d: int = 3) -> np.ndarray:
    """
    E[r_i r_j] for r uniformly distributed on the unit sphere S^{d-1} in R^d.

    Isotropy + |r| = 1 gives: E[r_i r_j] = (1/d) δ_ij.
    """
    delta = kron_delta(d)
    return delta / d


def fourth_moment_sphere_3d() -> np.ndarray:
    """
    E[r_i r_j r_k r_l] for r uniform on S^2 (3D).

    For d = 3 one has:
    E[r_i r_j r_k r_l] = (1/15)(
        δ_ij δ_kl + δ_ik δ_jl + δ_il δ_jk
    ).
    """
    d = 3
    delta = kron_delta(d)

    M4 = np.zeros((d, d, d, d), dtype=float)
    for i in range(d):
        for j in range(d):
            for k in range(d):
                for l in range(d):
                    M4[i, j, k, l] = (
                        delta[i, j] * delta[k, l]
                        + delta[i, k] * delta[j, l]
                        + delta[i, l] * delta[j, k]
                    )
    M4 /= 15.0
    return M4


def main():
    M2 = second_moment_sphere(3)
    M4 = fourth_moment_sphere_3d()

    print("Analytic E[r_i r_j] = δ_ij / 3 :")
    print(M2)
    print()

    print("Analytic E[r_i r_j r_k r_l] tensor (shape = 3x3x3x3):")
    print("M4[0,0,:,:] slice:")
    print(M4[0, 0, :, :])


if __name__ == "__main__":
    main()
