🛡️ PQC Toolkit — Post-Quantum Cryptography Migration Tool

A modular cybersecurity toolkit designed to help developers and organizations detect, analyze, and migrate from classical cryptographic algorithms (RSA, ECC, SHA-1, etc.) to post-quantum safe alternatives.

Built using Python, Streamlit, and a structured scanning engine.

🚀 Features
🔍 Cryptography Scanner
Detects vulnerable classical algorithms:
RSA (weak key sizes)
ECC (elliptic curve usage)
SHA-1 hashing
Flags non post-quantum-safe implementations
📊 Security Dashboard
Interactive Streamlit dashboard
Visual breakdown of cryptographic risks
Highlights quantum-unsafe components
🧠 Migration Suggestions

Recommends modern Post-Quantum Cryptography (PQC) algorithms:

Kyber (ML-KEM) → Key Encapsulation
Dilithium → Digital Signatures
Falcon → Compact Signatures
📁 Report Generation
Generates structured vulnerability reports
Summarizes cryptographic risks in scanned systems
🏗️ Tech Stack
Python 🐍
Streamlit 📊
Pandas 📑
JSON Configuration ⚙️
Plotly 📈
📂 Project Structure
pqc_toolkit/
│
├── dashboard/
│   └── app.py              # Streamlit dashboard
│
├── scanner/
│   └── crypto_scanner.py   # Detection engine
│
├── data/
│   └── mappings.json       # PQC migration mappings
│
├── reports/
│   └── output_reports/     # Generated scan reports
│
└── README.md

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/yourusername/pqc-toolkit.git
cd pqc-toolkit

2. Install dependencies
pip install -r requirements.txt

3. Run the dashboard
streamlit run dashboard/app.py

📸 Screenshots
Dashboard Overview
<img width="1362" height="608" alt="image" src="https://github.com/user-attachments/assets/143af58d-23c3-4543-8a1e-93e9cac3c289" />
Metrics View
<img width="1030" height="573" alt="image" src="https://github.com/user-attachments/assets/30e50cb6-2109-47d8-896a-35d40c03b360" />


🎯 Use Cases
Cybersecurity students & interns
Organizations preparing for post-quantum migration
Security audits of cryptographic systems
Academic research in PQC
🧪 Example Output
[WARNING] RSA-2048 detected → Vulnerable to quantum attacks
[SUGGESTION] Replace with ML-KEM (Kyber)

🔐 Future Improvements
Automated TLS certificate scanning
Real-time system monitoring
CI/CD pipeline security integration
Expanded PQC algorithm database
👩‍💻 Author

Thirishaa
Cybersecurity Enthusiast | Developer | Future Security Engineer

📌 Disclaimer

This tool is intended for educational and research purposes only.
It does not guarantee production-grade cryptographic security validation.

⭐ Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.
