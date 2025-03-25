import openai

class ContentGenerationAgent:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def generate_content(self, outline):
        openai.api_key = self.api_key
        content = f"# {outline['title']}\n\n"

        for section in outline['sections']:
            prompt = f"Write a detailed section on {section['heading']} about {outline['title']}. {section['description']}"
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "system", "content": prompt}]
            )
            content += f"## {section['heading']}\n{response['choices'][0]['message']['content']}\n\n"
        
        return content
