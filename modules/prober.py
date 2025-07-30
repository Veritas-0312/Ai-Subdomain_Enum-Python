# modules/prober.py

import requests
from urllib.parse import urljoin

# Common sensitive or interesting paths often targeted in bug bounty/CTF scenarios
COMMON_PATHS = ["/admin", "/login", "/config", "/dashboard", "/debug"]

class SubdomainProber:
    def __init__(self, timeout=5):
        self.timeout = timeout

    def probe(self, subdomain):
        """
        Probe a subdomain for:
        - Live status (via HTTP/HTTPS)
        - Page title
        - HTTP headers
        - Presence of common sensitive paths
        """
        result = {
            "subdomain": subdomain,
            "live": False,
            "title": None,
            "headers": {},
            "suspicious_paths": []
        }

        for scheme in ["https://", "http://"]:
            url = scheme + subdomain
            try:
                res = requests.get(url, timeout=self.timeout, verify=False)
                result["live"] = True
                result["headers"] = dict(res.headers)
                result["title"] = self.extract_title(res.text)

                # Check common sensitive paths
                for path in COMMON_PATHS:
                    test_url = urljoin(url, path)
                    test_res = requests.get(test_url, timeout=self.timeout, verify=False)
                    if test_res.status_code == 200:
                        result["suspicious_paths"].append(path)

                break  # Stop if one scheme worked

            except requests.RequestException:
                continue

        return result

    def extract_title(self, html):
        """Extract the <title> tag content from HTML."""
        start = html.lower().find("<title>")
        end = html.lower().find("</title>")
        if start != -1 and end != -1:
            return html[start + 7:end].strip()
        return None
