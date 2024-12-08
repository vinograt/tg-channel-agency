from agency_swarm import Agent

class ContentManager(Agent):
    def __init__(self):
        super().__init__(
            name="Content Manager",
            description="Manages content creation process and coordinates with other agents",
            instructions="./instructions.md",
            tools_folder="./tools",
            temperature=0.7
        ) 