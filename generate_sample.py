import json

sample_results = [
    {
        "location": "prod-web-server:443",
        "type": "tls_endpoint",
        "algorithm": "RSA-2048",
        "status": "quantum-vulnerable",
        "risk_score": 9.0,
        "recommendation": "Replace with ML-KEM (Kyber) and ML-DSA (Dilithium)"
    },
    {
        "location": "api-gateway:443",
        "type": "tls_endpoint",
        "algorithm": "ECDSA-P256",
        "status": "quantum-vulnerable",
        "risk_score": 9.0,
        "recommendation": "Replace with ML-KEM (Kyber) and ML-DSA (Dilithium)"
    },
    {
        "location": "ssh-jump-box:22",
        "type": "ssh_endpoint",
        "algorithm": "Diffie-Hellman",
        "status": "quantum-vulnerable",
        "risk_score": 8.5,
        "recommendation": "Migrate to SSH-PQC hybrid Kyber"
    },
    {
        "location": "root-ca.crt",
        "type": "x509_cert",
        "algorithm": "RSA-4096",
        "status": "quantum-vulnerable",
        "risk_score": 9.0,
        "recommendation": "Replace with ML-DSA (Dilithium)"
    },
    {
        "location": "pqc-experimental-node:443",
        "type": "tls_endpoint",
        "algorithm": "ML-KEM",
        "status": "quantum-safe",
        "risk_score": 1.0,
        "recommendation": "None"
    },
    {
        "location": "backup-vault:443",
        "type": "tls_endpoint",
        "algorithm": "RSA-1024",
        "status": "quantum-vulnerable",
        "risk_score": 10.0,
        "recommendation": "CRITICAL: Immediate replacement with ML-DSA required"
    }
]

with open("full_results.json", "w") as f:
    json.dump({"assets": sample_results}, f, indent=2)

print("✅ Created 'full_results.json'. Upload this in dashboard!")
