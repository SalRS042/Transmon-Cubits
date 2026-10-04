# Analytical Methods for the Resolution of Coupled and Decoupled Transmon Qubits

This repository contains the work developed for a Bachelor's Thesis focused on the theoretical and numerical study of transmon qubits.

The project investigates the eigenvalues and eigenfunctions of single and coupled transmon systems using analytical methods, matrix algebra and numerical calculations. Particular attention is given to the description of the system in the Cooper-pair number basis and in the phase basis.

## Abstract

The present work studies transmons. Here is explained the existence of two main bases for describing the eigenvalues and eigenfunctions of the system: the Number of Cooper Pair basis and the Phase basis. Firstly, is performed an analysis in the Cooper Pair basis of a single transmon, with the aid of the method of the second quantization and matrix algebra, obtaining an eigenfunction that matches almost equally to the one that generates the python package Scubits, and eigenvalues that match almost entirely the numerical resolution of the Hamiltonian. Secondly, a study of two coupled transmons is done through a decoupling procedure that allows one to find the eigenfunctions and eigenvalues of the decoupled system. Further investigation is needed.

## Repository contents

The repository contains the Bachelor's Thesis in article format together with the Python scripts used for the analytical and numerical calculations.

### Article

**`Analytical methods for the resolution of coupled and decoupled transmon qubits - SARS.pdf`**

This document contains the theoretical development, methodology, calculations and results of the project.

The work focuses on:

* The Hamiltonian of a single transmon.
* The Cooper-pair number basis.
* The phase basis.
* The calculation of eigenvalues and eigenfunctions.
* The use of second-quantization methods and matrix algebra.
* Numerical diagonalization of the Hamiltonian.
* Comparison with the `scqubits` Python package.
* The study of two coupled transmons.
* The decoupling procedure for the coupled system.
* The calculation of the eigenvalues and eigenfunctions of the resulting decoupled system.

### Python scripts

#### `EIgenvalues_Single_Transmon.py`

Calculates and plots the eigenvalues of a single transmon using the corresponding Hamiltonian matrix.

The results can be used to study the energy spectrum of the transmon and to compare the analytical treatment with numerical calculations.

#### `Eigenfunction_Single_Transmon.py`

Calculates and visualizes the eigenfunctions of a single transmon.

The script is used to study the wave functions obtained from the numerical treatment and to compare them with the corresponding results obtained using `scqubits`.

#### `Eigenvalues_Decoupled_Transmon.py`

Calculates the eigenvalues of the decoupled transmon system obtained after applying the decoupling procedure developed in the thesis.

#### `Eigenfunction_Decoupled_Transmon.py`

Calculates and visualizes the eigenfunctions of the decoupled transmon system using numerical methods.

The script includes the calculation of the corresponding wave functions and their three-dimensional visualization.

## Theoretical background

The Hamiltonian of a transmon can be written as

$\hat{H} = 4E_C(\hat{n}-n_g)^2 - E_J\cos(\hat{\varphi})$,

where:

* $E_C$ is the charging energy,
* $E_J$ is the Josephson energy,
* $\hat{n}$ is the Cooper-pair number operator,
* $n_g$ is the offset charge,
* $\hat{\varphi}$ is the superconducting phase operator.

The transmon can be described using different representations. In this work, particular attention is given to the **Cooper-pair number basis** and the **phase basis**.

For the single-transmon system, the Hamiltonian is expressed in the Cooper-pair number basis and solved using matrix methods. The resulting eigenvalues and eigenfunctions are subsequently compared with numerical results.

The study is then extended to a system of two coupled transmons. A transformation is introduced to decouple the system, allowing its eigenvalues and eigenfunctions to be studied in the resulting representation.

## Numerical methods

The calculations are performed using Python and numerical linear algebra techniques.

The main computational tasks include:

* Construction of the transmon Hamiltonian.
* Matrix representation of the Hamiltonian.
* Numerical diagonalization.
* Calculation of eigenvalues.
* Calculation of eigenfunctions.
* Visualization of the resulting wave functions.
* Comparison with `scqubits`.
* Analysis of the decoupled coupled-transmon system.

## Requirements

The scripts require Python 3 and the scientific Python packages used in the calculations.

The main dependencies are:

* NumPy
* SciPy
* Matplotlib
* scqubits

They can be installed with:

```bash
pip install numpy scipy matplotlib scqubits
```

## How to use

Clone the repository:

```bash
git clone https://github.com/SalRS042/Transmon-Cubits.git
```

Move into the repository:

```bash
cd Transmon-Cubits
```

The individual Python scripts can then be executed independently according to the calculation of interest.

For example:

```bash
python EIgenvalues_Single_Transmon.py
```

or:

```bash
python Eigenfunction_Single_Transmon.py
```

The scripts generate the corresponding numerical results and plots.

## Purpose of the repository

The purpose of this repository is to make the theoretical and numerical work developed during the Bachelor's Thesis available together with the corresponding computational tools.

The code can be used as a starting point for further studies of transmon qubits, superconducting quantum circuits and coupled-qubit systems.

## Author

**Salvador A. Rivas Sastre**

Bachelor's Thesis in Physics

## License

This project is distributed under the **GNU General Public License v3.0**.

See the [`LICENSE`](LICENSE) file for the complete license text.

## Acknowledgements

The numerical comparison of the single-transmon system makes use of the Python package `scqubits`.

The author acknowledges the developers and contributors of `scqubits` for providing an open-source framework for the simulation and analysis of superconducting quantum circuits.

Personals acknowledgements are placed in the article.
