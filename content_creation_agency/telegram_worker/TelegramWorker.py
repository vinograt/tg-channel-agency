from agency_swarm import Agent

class TelegramWorker(Agent):
    def __init__(self):
        super().__init__(
            name="Telegram Channel Worker",
            description="Manages and publishes content to Telegram channel",
            instructions="./instructions.md",
            tools_folder="./tools",
            temperature=0.3
        ) 