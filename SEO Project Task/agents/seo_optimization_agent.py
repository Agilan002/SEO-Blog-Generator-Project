import re

class SEOOptimizationAgent:
    def __init__(self, keywords):
        self.keywords = keywords
    
    def optimize_content(self, content):
        for keyword in self.keywords:
            content = re.sub(rf"\b({keyword})\b", r"**\1**", content, flags=re.IGNORECASE)
        return content
