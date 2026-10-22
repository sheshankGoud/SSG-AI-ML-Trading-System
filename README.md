<div align="center">

# 📈 SSG AI/ML Trading System

### Market Data Engineering • Feature Engineering • Machine Learning

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/FYERS_API-Integration-00AEEF?style=flat-square" alt="FYERS API">
  <img src="https://img.shields.io/badge/Auto--Trading-Disabled-success?style=flat-square" alt="Automatic trading disabled">
</p>

*A Python-based machine-learning project that collects market data, builds candles and technical features, generates BUY/HOLD/SELL predictions, and evaluates outcomes.*

</div>

---

## 🧭 Project at a Glance

| Area | Current setup |
|---|---|
| 📊 Market instrument used in the documented experiment | `NSE:WIPRO-EQ` |
| ⏱️ Candle interval | 1 minute |
| 🔭 Prediction horizon | 10 minutes |
| 🎯 Target threshold | ±0.10% |
| 🧮 Feature set | 26 features |
| 🏷️ Prediction classes | `BUY`, `HOLD`, `SELL` |
| 🤖 Automatic trade execution | **Disabled** |

> ⚠️ **Important:** This is an experimental market-prediction and engineering project, not a proven profitable trading strategy or financial advice. The project documentation says directional performance is not strong enough to claim reliable profitability. Predictions can be wrong and live-market use involves financial risk.

## ✨ What It Does

- 🔌 Connects to market-data services through the FYERS API integration.
- 📡 Collects live ticks using a WebSocket-based pipeline.
- 🕯️ Builds completed one-minute candles.
- 🧰 Creates features from returns, momentum, volatility, candle structure, volume, and moving-average relationships.
- 🧠 Runs machine-learning models to classify potential future movement.
- 🗃️ Stores market data and prediction/evaluation records in SQLite.
- 🔍 Evaluates predictions against later outcomes.
- 📊 Includes a dashboard application for viewing project information and results.

## 🏗️ Pipeline Architecture

```text
FYERS market feed
       │
       ▼
Live tick collection
       │
       ▼
SQLite market database
       │
       ▼
1-minute candle builder
       │
       ▼
Feature engineering
       │
       ▼
Machine-learning prediction
       │
       ▼
Prediction database
       │
       ▼
10-minute outcome evaluation
```

## 🧠 Machine Learning

The repository contains model training, feature-generation, prediction, and evaluation scripts under `ml/`.

### Target definition

The documented target compares the future price return over the next 10 minutes:

- 🟢 **BUY:** future return is greater than or equal to `+0.10%`
- 🟡 **HOLD:** future return is between `-0.10%` and `+0.10%`
- 🔴 **SELL:** future return is less than or equal to `-0.10%`

### Model experiments

The repository includes experiments involving:

- Logistic Regression baseline
- Random Forest variants
- Histogram Gradient Boosting
- Multiple model versions and evaluation utilities

The project README identifies `HIST_GRADIENT_V2_1` as the current production-model selection, stored at:

```text
data/models/production_model_wipro_v2_1.joblib
```

Model selection in this project does **not** mean the model is profitable. Evaluate it on unseen data and account for fees, slippage, class imbalance, and changing market conditions before drawing conclusions.

## 🧰 Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit">
</p>

- **Python** — application logic and orchestration
- **Pandas / NumPy** — data processing and feature preparation
- **scikit-learn / joblib** — model training, inference, and model persistence
- **SQLite** — local market-data and prediction storage
- **FYERS API / WebSocket** — market-data integration
- **Streamlit / Matplotlib** — dashboard and visualization dependencies

## 📁 Repository Structure

```text
.
├── auth/             # Authentication helpers
├── config/           # Configuration template
├── dashboard/        # Dashboard application
├── data/models/      # Saved model artifacts
├── engine/           # Candle builder and indicators
├── evaluation/       # Evaluation package
├── fyers/            # Market data and API integration
├── ml/               # Features, training, prediction, evaluation
├── paper_trading/    # Paper-trading components
├── requirements.txt  # Python dependencies
└── README.md
```

## 🚀 Getting Started

### 1. Requirements

- Python compatible with the pinned dependencies in `requirements.txt`
- A FYERS developer/app setup only if you intend to use authenticated market-data features
- Local credentials configured securely
- Internet access for API-based data collection

### 2. Clone the repository

Replace the placeholder URL with your own repository URL:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### 3. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Configure credentials safely

1. Review `config/settings_template.py`.
2. Create your local configuration file according to the project's expected import structure.
3. Add your own credentials locally.
4. **Never commit API secrets, access tokens, personal account data, or live databases.**

The repository's `.gitignore` excludes `config/settings.py` and local database files. Verify this before every push.

### 6. Run components

From the project root, the documented entry points include:

```bash
python .\fyers\fyers_collector.py
python .\engine\candle_builder.py
python -m ml.live_predictor
python -m ml.live_evaluator
```

On macOS/Linux, replace Windows-style `.\` path separators with `/`. API authentication, configuration, available market sessions, and required data files may need to be set up first. These commands are documented entry points; successful execution has not been independently verified in your environment.

## 🔐 Safety & Responsible Use

- 🔒 Keep API credentials and tokens out of GitHub.
- 🧪 Prefer historical testing and paper trading over real-money execution.
- 📴 Automatic trading is documented as disabled (`LIVE_TRADING = False`).
- 📉 Do not interpret a BUY/SELL label as a guaranteed outcome.
- 🧾 Include transaction costs, slippage, and out-of-sample testing in any performance analysis.
- 🧹 Review the repository for local databases, account data, and generated files before publishing.

## 🛣️ Potential Next Improvements

- 📏 Publish reproducible out-of-sample metrics, including precision/recall by class.
- 📉 Compare model performance with simple baseline strategies.
- 💸 Include brokerage, taxes, slippage, and realistic execution assumptions.
- 🧪 Add automated tests for candle construction, feature generation, and target labels.
- 📊 Add screenshots of the dashboard and clearly labeled evaluation charts.
- 🧾 Document which components are original contributions and which are adapted from other sources.

## 👤 About This Project

This repository is presented as a Python, data engineering, and machine-learning project. Before using it in a job portfolio, make sure you can explain the data pipeline, target construction, feature engineering, evaluation method, and limitations—and clearly state which parts you personally implemented.

---

<div align="center">

**Built for learning, experimentation, and responsible model evaluation.** 🐍

</div>
