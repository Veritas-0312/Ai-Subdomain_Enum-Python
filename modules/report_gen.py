# modules/report_gen.py

class ReportGenerator:
    def generate(self, ranked_subdomains):
        """
        Prints a formatted report of subdomains with their scores and statuses.
        """
        print("\n[+] AI-Powered Subdomain Report")
        print("=" * 60)

        for data, score in ranked_subdomains:
            # Priority label
            if score >= 0.8:
                label = "HIGH"
            elif score >= 0.5:
                label = "MEDIUM"
            else:
                label = "LOW"

            print(f"{data['subdomain']:<30} | Score: {score:.2f} | Priority: {label}")

            if data.get("live"):
                print(f"  [+] Live    | Title: {data.get('title') or 'N/A'}")
                if data.get("suspicious_paths"):
                    print(f"  [+] Suspicious paths: {', '.join(data['suspicious_paths'])}")
            else:
                print("  [-] Not reachable")

            print("-" * 60)
