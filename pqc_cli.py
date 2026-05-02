import argparse
import json
from engine.scanner import PQCScanner

def main():
    parser = argparse.ArgumentParser(description="PQC Migration Toolkit CLI")
    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser("scan")
    scan_parser.add_argument("--tls", nargs="*", help="TLS hosts")
    scan_parser.add_argument("-o", "--output", default="results.json")

    report_parser = subparsers.add_parser("report")
    report_parser.add_argument("-i", "--input", required=True)

    args = parser.parse_args()

    if args.command == "scan":
        scanner = PQCScanner()
        results = []

        if args.tls:
            for host in args.tls:
                results.append(scanner.scan_tls(host))

        with open(args.output, "w") as f:
            json.dump({"assets": results}, f, indent=2)

        print(f"Scan saved to {args.output}")

    elif args.command == "report":
        with open(args.input) as f:
            data = json.load(f)

        for asset in data["assets"]:
            print(f"{asset['location']} -> {asset['algorithm']} ({asset['status']})")

if __name__ == "__main__":
    main()
