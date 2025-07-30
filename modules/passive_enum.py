# modules/passive_enum.py

import requests

class PassiveEnum:
    def __init__(self, domain):
        self.domain = domain

    def enumerate(self):
        """
        Enumerates subdomains using crt.sh (certificate transparency logs).
        Returns a list of unique subdomains.
        """
        url = f"https://crt.sh/?q=%25.{self.domain}&output=json"
        try:
            res = requests.get(url, timeout=10)
            if res.status_code != 200:
                print(f"[-] Failed to fetch data from crt.sh: {res.status_code}")
                return []
            data = res.json()
        except Exception as e:
            print(f"[-] Exception occurred: {e}")
            return []

        subdomains = set()
        for entry in data:
            name = entry.get("name_value", "")
            for sub in name.splitlines():
                if sub.endswith(self.domain):
                    subdomains.add(sub.strip())

        return sorted(subdomains)
