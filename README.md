# League of Legends AI Analyst

A machine learning project that predicts the outcome of a League of Legends ranked match using information on game statistics available around the 10-minute mark.

The goal of the project is to investigate whether early-game information such as gold difference, experience difference, kills, objectives and vision can be used to predict which team will eventually win the match.

---

## Project Question

> **Can we predict the winner of a League of Legends match already after 10 minutes?**

The project uses historical League of Legends ranked matches and focuses specifically on the game state at **frame 10**, representing the 10-minute mark.

The final model predicts the probability that the selected team will eventually win the match.

---

## Project Goals

The main goals of the project are to:

- Explore and understand a League of Legends match dataset.
- Investigate relationships between early-game features and match outcomes.
- Prepare the data for machine learning.
- Apply dimensionality reduction and unsupervised learning.
- Compare several supervised machine learning models.
- Evaluate the final model using several classification metrics.
- Build an interactive Streamlit application where users can enter a 10-minute game state (with statistics based on the trained data) and receive a predicted win probability.

---

## Dataset

The project uses the **League of Legends SOLO-Q Ranked Games** dataset from Kaggle.

The original dataset contains multiple observations for each match at different points in the game.

The dataset contains:

- **242,572 rows**
- **59 columns**
- **24,912 unique matches**

Because each match can occur at several different frames, the project focuses only on:

```python
df[df["frame"] == 10]

## Installation

### Requirements

- Python 3.10 or later
- Git
- A virtual environment is recommended

### 1. Clone the repository

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd LoL_AI_Analyst

### 2.Create a Python virtual environment in the project directory:

python -m venv .venv

### 3. Activate the virtual environment

## Bash

source .venv/Scripts/activate

## PowerShell

.venv\Scripts\Activate.ps1

### 4. Install requirements

python -m pip install -r requirements.txt

### 5. Run the application

python -m streamlit run app/app.py