PQC Toolkit — Post‑Quantum Cryptography Migration Tool

A modular, practical toolkit designed to help developers and organizations identify, analyze, and migrate away from classical cryptography toward post‑quantum‑safe algorithms.

Built with Python, Streamlit, and a structured scanning engine.



🚀 Features

🔍 Cryptography Scanner

Detects RSA, ECC, SHA‑1, weak key sizes



Flags non‑PQC‑safe algorithms



Scans entire codebases or specific directories



Outputs structured JSON results



📊 Streamlit Dashboard

Clean UI for viewing scan results



Visual summaries of findings



Easy navigation for non‑technical users



Launch with one command:



bash

streamlit run dashboard/app.py

📚 Knowledge Base

Contains PQC algorithm references



Migration recommendations



Notes from NIST PQC standardization



🖥️ CLI Tool

Run scans directly from the terminal:



bash

python pqc\_cli.py --path <target\_folder>

📂 Project Structure

Code

pqc\_toolkit/

│

├── dashboard/          # Streamlit UI

│   └── app.py

│

├── engine/             # Core scanning engine

├── scanner/            # Detection logic

├── knowledge\_base/     # PQC references

├── data/               # Sample data

├── tests/              # Unit tests

│

├── pqc\_cli.py          # Command-line interface

├── generate\_sample.py  # Sample data generator

└── README.md

▶️ Running the Dashboard

bash

streamlit run dashboard/app.py

🧪 Running a Scan

bash

python pqc\_cli.py --path ./your\_project

📦 Installation

Install dependencies:



bash

pip install -r requirements.txt

🛡️ Why Post‑Quantum Migration Matters

Classical cryptography (RSA, ECC) will be breakable by future quantum computers.

This toolkit helps developers:



Identify vulnerable cryptographic usage



Understand PQC‑safe alternatives



Begin migration early



Reduce “harvest‑now, decrypt‑later” risk



📜 License

MIT License.

