# random_on_sphere
I created this project to present such an unpopular topic in a comprehensive manner, while I was learning tensor averaging, I encountered significant problems in terms of a lack of teaching materials and any kind of practical experience. I decided not only to talk about it, but also to provide scripts that would help in understanding this topic.
# sphere-tensor-moments

This project is a small playground about **random points on the sphere** and **tensor averaging**.

The main goal is to show how isotropy + the fact that the only invariant rank-2 tensor is the Kronecker delta  
allow us to compute expectations like

\[
\mathbb{E}[r_i r_j], \qquad
\mathbb{E}[r_i r_j r_k r_l]
\]

for a random point \(r\) on the unit sphere, and then apply these formulas to non-trivial geometric quantities,
such as the average squared volume of a random tetrahedron inscribed in the sphere.

The results are verified numerically by Monte Carlo simulations.

---

## Mathematical background

Let \(r\in \mathbb{R}^3\) be a random vector uniformly distributed on the unit sphere \(S^2\).

By isotropy and parity:
- \(\mathbb{E}[r_i] = 0\);
- the only invariant rank-2 tensor is proportional to \(\delta_{ij}\), so
  \[
  \mathbb{E}[r_i r_j] = \lambda\,\delta_{ij},
  \]
  and from \(|r|^2 = 1\) we get \(\lambda = 1/3\).

Similarly, for the 4-th order moment one can show that
\[
\mathbb{E}[r_i r_j r_k r_l]
  = \alpha\bigl(
      \delta_{ij}\delta_{kl}
    + \delta_{ik}\delta_{jl}
    + \delta_{il}\delta_{jk}
    \bigr),
\]
and \(\alpha = 1/15\) in 3D.

These tensor identities are then used to compute
the expected square of the volume of a random tetrahedron with vertices on the unit sphere.
If \(A,B,C,D\) are independent uniform points on \(S^2\), the volume is

\[
V_{ABCD} = \frac{1}{6} \left|\det(B-A,\ C-A,\ D-A)\right|.
\]

The tensor calculation gives
\[
\mathbb{E}\,V_{ABCD}^2 = \frac{2}{81}, \qquad
\sqrt{\mathbb{E}\,V_{ABCD}^2} = \frac{\sqrt{2}}{9}.
\]

The Monte Carlo script in this repository numerically confirms these formulas.

---

## Repository structure

- `sphere_tensor_moments.py`  
  Analytic formulas for tensor moments of a random point on the sphere:
  - builds \( \mathbb{E}[r_i r_j] \) and \( \mathbb{E}[r_i r_j r_k r_l] \) as explicit numpy arrays
  - prints slices of these tensors for inspection.

- `verify_moments_monte_carlo.py`  
  Monte Carlo verification:
  - samples random points on the sphere via normalized Gaussian vectors,
  - estimates empirical \( \mathbb{E}[r_i r_j] \) and \( \mathbb{E}[r_i r_j r_k r_l] \),
  - compares them with the analytic tensors (Frobenius norm of the difference),
  - samples random tetrahedra on the sphere and estimates \( \mathbb{E}V^2 \),
    comparing it to the theoretical value \(2/81\).

- `requirements.txt`  
  Minimal list of Python dependencies (currently just `numpy`).

- `LICENSE`  
  MIT license for the code.

---
##References
Random Point Sets on the Sphere --- Hole Radii, Covering, and Separation , https://arxiv.org/abs/1512.07470
tensors_like_physicist.pdf --- https://vk.com/doc110337008_616974849?hash=DVpa01j0BZRvQ4pCZqwo5m5IBKQNkZhmkrlLd4NcJ38&dl=MqBGU2ZNpYFUgQHSFKbwEmcHO0DA2s8uNJeuZGOzBuT ( From MIPT Students public in VK )
tensors.pdf --- Lecture notes “Tensors and integrals on a sphere,” MIPT teaching manual (author not specified, in Russian).
## Installation

```bash
git clone https://github.com/nnoskovsky/random_on_sphere.git
cd random_on_sphere
pip install -r requirements.txt



