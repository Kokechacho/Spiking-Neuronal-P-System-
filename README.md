# **Spiking Neural P Systems (SN P Systems) Simulation**

This repository provides an implementation of **Spiking Neural P Systems (SN P Systems)** based on the specifications described in the research paper:

> **Modeling Spiking Neural P Systems using Timed Petri Nets**  
> Authors: Venkata Padmavati Metta, Kamala Krithivasan, Deepak Garg  

While the paper presents a methodology to translate SN P systems into deterministic P-timed Petri nets with inhibitory and test arcs, this repository **only implements the SN P system specifications** described in the paper. Additionally, the example of a **non-deterministic simulation of an SN P system** presented in the paper is included.

---

## **Features**
- **Neuron modeling**:
  - Supports spiking and forgetting rules for each neuron.
  - Implements delays to control when spikes are propagated to connected neurons.
- **Non-deterministic simulation**:
  - Neurons apply rules non-deterministically when multiple applicable rules are available.
- **Step-by-step simulation**:
  - Tracks spikes and delays for each neuron over multiple simulation steps.
- **Synapse management**:
  - Handles connections between neurons, enabling spike propagation based on system rules.

---

## **Repository Structure**
The code is organized into three main components for better clarity and modularity:

1. **`neuron.py`**  
   Contains the `Neuron` class, representing individual neurons in the SN P system. This class manages the neuron's state, rules, and delays.

2. **`snpsystem.py`**  
   Contains the `SNPSystem` class, which models the overall SN P system. It includes functionality for simulating the interaction of neurons and propagating spikes across synapses.

3. **`main.py`**  
   The main script that sets up an SN P system based on the example from the paper, connects neurons, and runs the non-deterministic simulation.

---

## **Getting Started**

### **Prerequisites**
This project requires Python 3.x and the following library:
- **NumPy** (for non-deterministic rule selection).

Install the dependency using pip:
```bash
pip install numpy
