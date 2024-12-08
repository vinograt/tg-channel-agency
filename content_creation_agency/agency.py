from agency_swarm import Agency
from content_manager.ContentManager import ContentManager
from trends_analyzer.TrendsAnalyzer import TrendsAnalyzer
from telegram_worker.TelegramWorker import TelegramWorker

content_manager = ContentManager()
trends_analyzer = TrendsAnalyzer()
telegram_worker = TelegramWorker()

agency = Agency(
    [
        content_manager,  # Content Manager is the entry point
        [content_manager, trends_analyzer],  # Content Manager can communicate with Trends Analyzer
        [content_manager, telegram_worker],  # Content Manager can communicate with Telegram Worker
    ],
    shared_instructions="agency_manifesto.md",
    temperature=0.7,
    max_completion_tokens=25000
)

if __name__ == "__main__":
    agency.run_demo()