from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

class TavilySearch(BaseTool):
    """
    A tool to search the web using Tavily API.
    """
    query: str = Field(..., description="The search query")
    
    def run(self):
        """
        Search the web using Tavily API.
        """
        client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        response = client.search(self.query)
        return response

if __name__ == "__main__":
    searcher = TavilySearch(query="Latest AI trends 2024")
    print(searcher.run()) 