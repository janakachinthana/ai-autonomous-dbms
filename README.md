# AI-Driven Autonomous Database Management System (ADBMS)

This project implements an AI-driven autonomous database management system that leverages machine learning, predictive analytics, and automation to optimize database performance, reduce administrative overhead, and enhance scalability in enterprise IT environments.

---

## Project Overview

ADBMS includes:
- **Self-Tuning Engine**: Monitors workloads and dynamically adjusts system parameters.
- **Predictive Query Optimizer**: Uses ML to enhance query execution plans and reduce latency.
- **Intelligent Indexing**: Automates index selection, adaptation, and maintenance.
- **Security & Compliance**: AI-driven anomaly detection and automated threat mitigation.

---

## Project Structure

```
ai-autonomous-dbms/
├── README.md
├── requirements.txt
├── Setup.bat
├── import sys.txt
├── auto_run_all_tables.py
├── docs/
│   ├── ADBMS_Research_Document.docx
│   ├── architecture.md
│   ├── architecture_diagram.png
│   ├── comparison_chart.png
│   └── generate_research_doc.ipynb
├── logs/
│   └── 20250620_113941/
│       ├── anomaly_detector.json
│       ├── index_manager.json
│       ├── parameter_tuner.json
│       ├── query_optimizer.json
│       └── workload_monitor.json
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
```

---

## Getting Started

### Prerequisites
- Python 3.8 or later
- Jupyter Notebook (for running `docs/generate_research_doc.ipynb`)
- Machine learning libraries: scikit-learn, matplotlib, (optionally TensorFlow, PyTorch)
- `python-docx` (for Word export)
- Internet access (for literature review and citation fetching)
- Database system (e.g., SQL Server, PostgreSQL, MySQL, MongoDB)
- Docker (optional)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/janakachinthana/ai-autonomous-dbms.git
   cd ai-autonomous-dbms
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your database connection in `src/config.py`.

---

## Usage

- Run the main automation script for all tables:
  ```bash
  python auto_run_all_tables.py
  ```
- Start the self-tuning engine:
  ```bash
  python src/self_tuning/main.py
  ```
- Run the predictive query optimizer:
  ```bash
  python src/query_optimization/main.py
  ```
- Enable intelligent indexing:
  ```bash
  python src/intelligent_indexing/main.py
  ```

---

## Documentation
- **Architecture**: See `docs/architecture.md` for a detailed overview.
- **Architecture Diagrams**: ![Architecture Diagram](docs/architecture_diagram.png) ![Comparison Chart](docs/comparison_chart.png)
- **Additional Notebooks**: See `docs/` for Jupyter notebooks and more.

---

## Best Practices
- Regularly update ML models with new data.
- Monitor logs and analytics for performance and security.
- Ensure compliance and data governance.

---

## References
[1] Oloruntoba, O. (2025). AI-Driven Autonomous Database Management: Self-tuning, Predictive Query Optimization, and Intelligent Indexing in Enterprise IT Environments. *World Journal of Advanced Research and Reviews*, 25(02), 1558-1580.
[2] https://journalwjarr.com/sites/default/files/fulltext_pdf/WJARR-2025-0534.pdf
[3] https://www.oracle.com/autonomous-database/
[4] https://www.microsoft.com/en-us/research/publication/ai-meets-ai-leveraging-query-executions-to-improve-index-recommendations/
[5] Oracle, "Autonomous Database," Oracle, 2025. [Online]. Available: https://www.oracle.com/autonomous-database/
[6] R. Shwartz-Ziv and A. Armon, "Tabular Data: Deep Learning is Not All You Need," arXiv preprint arXiv:2106.03253, 2021. [Online]. Available: https://arxiv.org/abs/2106.03253
[7] T. Kraska, A. Beutel, E. H. Chi, J. Dean, and N. Polyzotis, "The Case for Learned Index Structures," in Proc. ACM SIGMOD, 2018, pp. 489–504. [Online]. Available: https://dl.acm.org/doi/10.1145/3183713.3196909
[8] A. Pavlo, A. Agrawal, G. Angulo, et al., "Self-Driving Database Management Systems," in Proc. CIDR, 2017. [Online]. Available: http://cidrdb.org/cidr2017/papers/p42-pavlo-cidr17.pdf
[9] S. Chaudhuri and V. Narasayya, "Self-tuning Database Systems: A Decade of Progress," in Proc. VLDB, 2007. [Online]. Available: https://www.vldb.org/conf/2007/papers/tutorials/tut1.chaudhuri.pdf
[10] A. Fekete, D. Lomet, A. Weikum, and G. Weikum, "Making Databases Self-Managing: A Survey," VLDB Journal, vol. 16, no. 4, pp. 419–437, 2007. [Online]. Available: https://link.springer.com/article/10.1007/s00778-007-0045-2

---

**Keywords:** Autonomous database management, AI-driven self-tuning, Predictive query optimization, Intelligent indexing, Enterprise IT, Machine learning for databases.
