from agency_swarm import Agent

class TrendsAnalyzer(Agent):
    def __init__(self):
        super().__init__(
            name="Trends Analyzer",
            description="Analyzes latest trends and identifies content opportunities",
            instructions="./instructions.md",
            tools_folder="./tools",
            temperature=0.5
        ) 