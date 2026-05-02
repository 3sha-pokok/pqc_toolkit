import ssl
import socket
import json
import os
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa, ec, dsa
import paramiko


class PQCScanner:

    def __init__(self, kb_path="knowledge_base/pqc_map.json"):
        try:
            with open(kb_path, 'r') as f:
                self.kb = json.load(f)
        except FileNotFoundError:
            print(f"Warning: Knowledge base not found at {kb_path}. Using default fallbacks.")
            self.kb = {
                "mappings": {},
                "risk_scores": {"Critical": 9.0, "Low": 1.0}
            }

    def _get_risk_score(self, algo_type):
        risk_level = self.kb.get("mappings", {}).get(algo_type, {}).get("risk_level", "Low")
        return self.kb.get("risk_scores", {}).get(risk_level, 1.0)

    def _get_recommendation(self, algo_type):
        mapping = self.kb.get("mappings", {}).get(algo_type, {})
        if not mapping:
            return "Manual review required"

        kx = mapping.get("replacement_kx", "N/A")
        sig = mapping.get("replacement_sig", "N/A")
        return f"Replace with {kx} and {sig}"

    def scan_tls(self, host, port=443):
        try:
            context = ssl.create_default_context()
            with socket.create_connection((host, port), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    cert_bin = ssock.getpeercert(binary_form=True)
                    cert = x509.load_der_x509_certificate(cert_bin)
                    pubkey = cert.public_key()

                    algo_type = "Unknown"

                    if isinstance(pubkey, rsa.RSAPublicKey):
                        algo_type = "RSA"
                    elif isinstance(pubkey, ec.EllipticCurvePublicKey):
                        algo_type = "ECDSA"
                    elif isinstance(pubkey, dsa.DSAPublicKey):
                        algo_type = "DSA"

                    key_size = getattr(pubkey, 'key_size', 'unknown')

                    return {
                        "location": f"{host}:{port}",
                        "type": "tls_endpoint",
                        "algorithm": f"{algo_type}-{key_size}",
                        "status": "quantum-vulnerable" if algo_type in self.kb.get("mappings", {}) else "quantum-safe",
                        "risk_score": self._get_risk_score(algo_type),
                        "recommendation": self._get_recommendation(algo_type)
                    }

        except Exception as e:
            return {"location": f"{host}:{port}", "error": str(e)}

    def scan_ssh(self, host, port=22):
        try:
            transport = paramiko.Transport((host, port))
            transport.connect()

            kex = transport.get_security_options().kex

            vulnerable = any("diffie-hellman" in k.lower() for k in kex)

            return {
                "location": f"{host}:{port}",
                "type": "ssh_endpoint",
                "algorithm": "SSH-KEX",
                "status": "quantum-vulnerable" if vulnerable else "quantum-safe",
                "risk_score": 9.0 if vulnerable else 1.0,
                "recommendation": "Use hybrid PQC SSH"
            }

        except Exception as e:
            return {"location": f"{host}:{port}", "error": str(e)}

        finally:
            try:
                transport.close()
            except:
                pass

    def scan_local_cert(self, path):
        try:
            if not os.path.exists(path):
                return {"location": path, "error": "File not found"}

            with open(path, "rb") as f:
                data = f.read()

            try:
                cert = x509.load_pem_x509_certificate(data)
            except:
                cert = x509.load_der_x509_certificate(data)

            pubkey = cert.public_key()

            algo_type = "Unknown"
            if isinstance(pubkey, rsa.RSAPublicKey):
                algo_type = "RSA"
            elif isinstance(pubkey, ec.EllipticCurvePublicKey):
                algo_type = "ECDSA"

            return {
                "location": path,
                "type": "x509_cert",
                "algorithm": algo_type,
                "status": "quantum-vulnerable" if algo_type in self.kb.get("mappings", {}) else "quantum-safe",
                "risk_score": self._get_risk_score(algo_type),
                "recommendation": self._get_recommendation(algo_type)
            }

        except Exception as e:
            return {"location": path, "error": str(e)}
