# modules/ranker.py

class SubdomainRanker:
    def __init__(self):
        # Sensitive keywords and their weight for scoring
        self.keywords = {
            "admin": 0.9,
            "dev": 0.8,
            "test": 0.7,
            "stage": 0.6,
            "api": 0.75,
            "internal": 0.85,
            "secure": 0.65
        }

    def rank(self, probe_results):
        """
        Takes a list of probe result dicts and returns a list of tuples:
        (data_dict, score_float), sorted by score in descending order.
        """
        ranked = []
        for data in probe_results:
            score = self.estimate_score(data)
            ranked.append((data, score))
        ranked.sort(key=lambda x: x[1], reverse=True)
        return ranked

    def estimate_score(self, data):
        """
        Calculates a heuristic score for a subdomain based on:
        - Presence of sensitive keywords
        - Live status
        - Suspicious paths
        """
        sub = data["subdomain"]
        score = 0.1  # Base score

        if data.get("live", False):
            score += 0.2

        for key, weight in self.keywords.items():
            if key in sub:
                score += weight

        if data.get("suspicious_paths"):
            score += 0.2

        return round(min(score, 1.0), 2)
