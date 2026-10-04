# Transmon Qubits: Coupled and Decoupled analytical analysis

This repository contains the work developed for a Bachelor's Thesis focused on the theoretical study of superconducting transmon qubits.

The project studies the eigenvalues and eigenfunctions of transmon systems using different representations of the Hamiltonian, with particular emphasis on the **Cooper-pair number basis** and the **phase basis**.

## Description

The main objective of this work is to study the quantum-mechanical description of transmon qubits and to obtain their eigenvalues and eigenfunctions using analytical and numerical methods.

The project is divided into two main parts:

1. **Single transmon**

   The Hamiltonian of a single transmon is studied in the Cooper-pair number basis. The analysis makes use of second quantization and matrix algebra to obtain the eigenvalues and eigenfunctions of the system.

   The results are compared with numerical calculations and with the results obtained using the Python package `scqubits`.

2. **Coupled transmons**

   The system of two coupled transmons is subsequently studied. A decoupling procedure is developed in order to obtain the eigenvalues and eigenfunctions associated with the resulting decoupled system.

The analytical and numerical results show good agreement for the single-transmon system. The study of coupled transmons provides a starting point for further investigation of more complex superconducting-qubit systems.

## Repository contents

The repository contains the following main components:

```text
.
├── README.md
├── LICENSE
├── TFG/
│   └── ...
└── Code/
    └── ...
```

### TFG

This directory contains the Bachelor's Thesis in its revised article-style format.

The document presents the theoretical development, methodology, calculations and results of the project in a format intended to resemble a scientific publication.

### Code

This directory contains the Python code developed for the analytical and numerical calculations presented in the thesis.

The code includes the functions and routines used to:

* Construct the transmon Hamiltonian.
* Work in the Cooper-pair number basis.
* Calculate eigenvalues and eigenfunctions.
* Perform matrix-based calculations.
* Compare analytical and numerical results.
* Compare the results with `scqubits`.
* Study systems of coupled transmons.
* Perform the transformations required for the decoupling procedure.
* Generate the numerical results and figures presented in the thesis.

## Theoretical background

A transmon is a type of superconducting qubit derived from the Cooper-pair box regime. Its Hamiltonian can be written as

$ \hat{H} = 4E_C(\hat{n}-n_g)^2 - E_J\cos(\hat{\varphi}) $,

where:

* $E_C$ is the charging energy,
* $E_J$ is the Josephson energy,
* $\hat{n}$ is the Cooper-pair number operator,
* $n_g$ is the offset charge,
* $\hat{\varphi}$ is the superconducting phase operator.

Two representations are particularly relevant in this work:

* **Cooper-pair number basis**, in which the charge operator is diagonal.
* **Phase basis**, in which the superconducting phase is used as the relevant coordinate.

The relationship between these representations provides a useful framework for studying the quantum states of the transmon.

## Numerical calculations

The numerical calculations are performed using Python and standard scientific-computing tools.

The results obtained from the analytical treatment are compared with direct numerical diagonalization of the Hamiltonian.

Additionally, the results for the single transmon are compared with the Python package [`scqubits`](https://scqubits.readthedocs.io/), which provides numerical tools for the simulation and analysis of superconducting quantum circuits.

## Requirements

The exact dependencies may depend on the particular scripts included in the repository. The main Python packages used in the project include:

* Python 3
* NumPy
* SciPy
* Matplotlib
* scqubits

The required packages can be installed using `pip`. For example:

```bash
pip install numpy scipy matplotlib scqubits
```

If a `requirements.txt` file is provided, the recommended installation method is:

```bash
pip install -r requirements.txt
```

## Reproducibility

The code included in this repository is intended to reproduce the main analytical and numerical calculations presented in the thesis.

The scripts can be used independently to investigate the properties of single and coupled transmon systems and to reproduce the numerical results discussed in the accompanying article.

## Thesis

The complete thesis is available in the `TFG` directory.

The article-style version of the work contains the theoretical derivations, methodology, results and discussion associated with the code included in this repository.

## Author

**Salvador A. Rivas Sastre**

Bachelor's Thesis in Physics

## License

This project is distributed under the terms specified in the [`LICENSE`](LICENSE) file.

## Acknowledgements

The author acknowledges the use of the open-source Python package `scqubits` for the numerical analysis and comparison of the transmon systems studied in this work.
