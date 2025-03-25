class ContentPlanningAgent:
    def generate_outline(self, topic):
        return {
            "title": topic,
            "sections": [
                {"heading": "Introduction", "description": "Overview of the topic"},
                {"heading": "Why This Matters", "description": "Importance in HR industry"},
                {"heading": "Key Strategies", "description": "Practical implementation"},
                {"heading": "Challenges", "description": "Common obstacles and solutions"},
                {"heading": "Conclusion", "description": "Final thoughts and takeaways"}
            ]
        }
