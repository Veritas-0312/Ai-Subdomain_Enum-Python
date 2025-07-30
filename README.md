AI-Powered Subdomain Enumerator
An intelligent reconnaissance tool that discovers and prioritizes high-value subdomains for CTF challenges and bug bounty hunting.

📌 Features
Passive Enumeration using certificate transparency logs (crt.sh)

Live Probing of subdomains (HTTP/HTTPS reachability, titles, headers)

Sensitive Path Scanning (/admin, /login, /config, etc.)

AI-Inspired Ranking to prioritize interesting targets based on heuristics

Formatted Reports with priority labels (HIGH / MEDIUM / LOW)

🗂️ Project Structure
Ai-Subdomain_Enum-Python/
│
├── ai_subdomain_enumerator.py      # Main entry point
└── modules/
    ├── __init__.py                 # Empty package marker
    ├── passive_enum.py             # Passive subdomain collection
    ├── prober.py                   # Probes subdomains for data
    ├── ranker.py                   # AI/heuristic-based scoring
    └── report_gen.py               # Report generation

⚡ Installation
# Clone the repository
git clone https://github.com/yourusername/Ai-Subdomain_Enum-Python.git
cd Ai-Subdomain_Enum-Python

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install requests

🚀 Usage
python ai_subdomain_enumerator.py -d example.com

Example Output:
[+] Starting AI Subdomain Enumeration for: example.com
[+] Found 8 subdomains
[>] Probing www.example.com ...
[>] Probing admin.example.com ...

[+] AI-Powered Subdomain Report
============================================================
admin.example.com              | Score: 0.95 | Priority: HIGH
  [+] Live    | Title: Admin Login
  [+] Suspicious paths: /admin, /login
------------------------------------------------------------
www.example.com                 | Score: 0.60 | Priority: MEDIUM
  [+] Live    | Title: Example Domain
------------------------------------------------------------
