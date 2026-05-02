# 🛡️ PQC Toolkit — Post-Quantum Cryptography Migration Tool

A modular cybersecurity toolkit designed to help developers and organizations detect, analyze, and migrate from classical cryptographic algorithms (RSA, ECC, SHA-1, etc.) to post-quantum safe alternatives.

Built using **Python**, **Streamlit**, and a structured scanning engine.

---

## 🚀 Features

### 🔍 Cryptography Scanner
- Detects vulnerable classical algorithms such as:
  - RSA (weak key sizes)
  - ECC (elliptic curve usage)
  - SHA-1 hashing
- Identifies non-post-quantum safe implementations

### 📊 Security Dashboard
- Interactive Streamlit dashboard
- Visual breakdown of cryptographic risks
- Highlights “quantum-unsafe” components

### 🧠 Migration Suggestions
- Recommends PQC alternatives such as:
  - Kyber (ML-KEM) → Key Encapsulation
  - Dilithium → Digital Signatures
  - Falcon → Compact signatures

### 📁 Report Generation
- Generates structured reports of vulnerabilities
- Summarizes crypto risks in scanned systems

---

## 🏗️ Tech Stack

- Python 🐍
- Streamlit 📊
- Pandas 📑
- JSON Configuration System ⚙️
- Plotly (for visualizations) 📈

---

## 📂 Project Structure

pqc_toolkit/
│
├── dashboard/
│ └── app.py # Streamlit dashboard
│
├── scanner/
│ └── crypto_scanner.py # Detection engine
│
├── data/
│ └── mappings.json # PQC migration mappings
│
├── reports/
│ └── output_reports/ # Generated scan reports
│
└── README.md


---

## ⚙️ Installation & Setup

### 1. Clone the repository
git clone https://github.com/yourusername/pqc-toolkit.git
cd pqc-toolkit
2. Install dependencies
pip install -r requirements.txt
3. Run the dashboard
streamlit run dashboard/app.py

📸 Screenshots

![Post-Quantum Migration Dashboard](<img width="1353" height="492" alt="image" src="https://github.com/user-attachments/assets/e8ec64d3-4c7e-4f33-b803-56741be86e84" />
)
![PQC Dashboard Metrics](<img width="1028" height="547" alt="image" src="https://github.com/user-attachments/assets/49de36a4-b9ee-47fd-8feb-1faaeea2fbcc" />
)


🎯 Use Case

This tool is useful for:

Cybersecurity interns & students
Organizations preparing for post-quantum transition
Security audits of cryptographic systems
Academic research on PQC migration
🧪 Example Output
[WARNING] RSA-2048 detected → Vulnerable to quantum attacks
[SUGGESTION] Replace with ML-KEM (Kyber)
🔐 Future Improvements
Automated TLS certificate scanning
Real-time system integration
CI/CD pipeline security checks
Expanded PQC algorithm database
👩‍💻 Author

Thirishaa
Cybersecurity Enthusiast | Developer | Future Security Engineer

📌 Disclaimer

This tool is for educational and research purposes only. It does not guarantee full production-grade cryptographic security validation.


---

If you want, I can also:
✔ :contentReference[oaicite:0]{index=0}  
✔ :contentReference[oaicite:1]{index=1}  
✔ or :contentReference[oaicite:2]{index=2}
