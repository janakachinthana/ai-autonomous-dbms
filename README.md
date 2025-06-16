# AI-Driven Autonomous Database Management System (ADBMS)

This project implements an AI-driven autonomous database management system with self-tuning, predictive query optimization, and intelligent indexing. See `docs/architecture.md` for details.

## Project Structure

```
├── docs/
│   └── architecture.md
├── requirements.txt
├── src/
│   ├── config.py
│   ├── intelligent_indexing/
│   │   ├── index_manager.py
│   │   └── main.py
│   ├── query_optimization/
│   │   ├── main.py
│   │   └── query_optimizer.py
│   ├── security/
│   │   ├── anomaly_detector.py
│   │   └── main.py
│   └── self_tuning/
│       ├── main.py
│       ├── parameter_tuner.py
│       └── workload_monitor.py
├── tests/
│   └── integration/
│       ├── test_intelligent_indexing.py
│       ├── test_placeholder.py
│       ├── test_query_optimization.py
│       ├── test_security.py
│       └── test_self_tuning.py
└── README.md
```

## Project Setup

1. **Clone the repository:**
   ```powershell
   git clone https://github.com/janakachinthana/ai-autonomous-dbms.git
   cd ai-autonomous-dbms
   ```
2. **(Optional) Create and activate a virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

## How to Run Each Module

Run the following commands in sequence from the project root directory:

1. **Intelligent Indexing Module**
   ```powershell
   python src/intelligent_indexing/main.py
   ```
2. **Predictive Query Optimizer**
   ```powershell
   python src/query_optimization/main.py
   ```
3. **Security & Compliance Layer**
   ```powershell
   python src/security/main.py
   ```
4. **Self-Tuning Engine**
   ```powershell
   python src/self_tuning/main.py
   ```
