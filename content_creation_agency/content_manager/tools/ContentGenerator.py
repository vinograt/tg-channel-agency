from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv
import openai

load_dotenv()

class ContentGenerator(BaseTool):
    """
    A tool to generate content ideas and scripts using OpenAI's GPT-4 model.
    """
    prompt: str = Field(
        ..., description="The prompt to send to GPT-4 for content generation"
    )
    
    def run(self):
        """
        Generate content using OpenAI's GPT-4 model.
        """
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        response = client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": "You are a creative content writer."},
                {"role": "user", "content": self.prompt}
            ]
        )
        
        return response.choices[0].message.content

if __name__ == "__main__":
    generator = ContentGenerator(prompt="Generate 5 content ideas about AI trends")
    print(generator.run()) 