# ai_subdomain_enumerator.py

import argparse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from modules.passive_enum import PassiveEnum
from modules.prober import SubdomainProber
from modules.ranker import SubdomainRanker
from modules.report_gen import ReportGenerator

def main(domain):
    print(f"[+] Starting ScopeHawk enumeration for: {domain}")

    # Step 1: Passive Enumeration
    enum = PassiveEnum(domain)
    subdomains = enum.enumerate()
    print(f"[+] Found {len(subdomains)} subdomains")

    if not subdomains:
        print("[-] No subdomains found. Exiting.")
        return

    # Step 2: Probing
    prober = SubdomainProber()
    results = []
    for sub in subdomains:
        print(f"[>] Probing {sub} ...")
        results.append(prober.probe(sub))

    # Step 3: Ranking
    ranker = SubdomainRanker()
    ranked = ranker.rank(results)

    # Step 4: Reporting
    reporter = ReportGenerator()
    reporter.generate(ranked)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ScopeHawk - AI-powered Subdomain Enumerator")
    parser.add_argument("-d", "--domain", required=True, help="Target domain to enumerate")
    args = parser.parse_args()

    main(args.domain)
