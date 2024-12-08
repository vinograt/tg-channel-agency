from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv
import requests

load_dotenv()

class TelegramBot(BaseTool):
    """
    A tool to manage and publish content to Telegram channel.
    """
    action: str = Field(..., description="Action to perform (send_message, edit_message, delete_message, publish_script)")
    message: str = Field(None, description="Message text or content (not required for publish_script)")
    message_id: int = Field(None, description="Message ID for editing/deleting")
    script_path: str = Field(None, description="Path to the markdown script file (required for publish_script)")
    
    def run(self):
        """
        Perform actions with Telegram channel using Bot API.
        """
        bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        channel_name = "abbggg_room"
        base_url = f"https://api.telegram.org/bot{bot_token}"
        
        if self.action == "publish_script":
            if not self.script_path:
                return {"error": "Script path is required for publish_script action"}
            
            try:
                # Read the script content
                with open(self.script_path, 'r', encoding='utf-8') as file:
                    script_content = file.read().strip()
                
                # Format the content for Telegram
                formatted_content = (
                    f"📝 *New Content*\n\n"
                    f"{script_content}"
                )
                
                # Send the content to Telegram
                url = f"{base_url}/sendMessage"
                data = {
                    "chat_id": f"@{channel_name}",
                    "text": formatted_content,
                    "parse_mode": "Markdown"
                }
                response = requests.post(url, json=data)
                return response.json()
                
            except FileNotFoundError:
                return {"error": f"Script not found: {self.script_path}"}
            except Exception as e:
                return {"error": f"Error publishing script: {str(e)}"}
        
        elif self.action == "send_message":
            url = f"{base_url}/sendMessage"
            data = {
                "chat_id": f"@{channel_name}",
                "text": self.message,
                "parse_mode": "Markdown"
            }
        elif self.action == "edit_message":
            url = f"{base_url}/editMessageText"
            data = {
                "chat_id": f"@{channel_name}",
                "message_id": self.message_id,
                "text": self.message,
                "parse_mode": "Markdown"
            }
        elif self.action == "delete_message":
            url = f"{base_url}/deleteMessage"
            data = {
                "chat_id": f"@{channel_name}",
                "message_id": self.message_id
            }
        else:
            return {"error": "Invalid action specified"}
            
        response = requests.post(url, json=data)
        return response.json()

if __name__ == "__main__":
    # Test sending a message
    bot = TelegramBot(
        action="send_message",
        message="Test message from Content Creation Agency"
    )
    print("Test 1 - Send message:", bot.run())
    
    # Test publishing a script
    test_script_path = "scripts/test_script.md"
    # Create a test script if it doesn't exist
    if not os.path.exists("scripts"):
        os.makedirs("scripts")
    with open(test_script_path, "w", encoding="utf-8") as f:
        f.write("# Test Article\n\nThis is a test article content.\n\nIt includes multiple paragraphs.")
    
    bot = TelegramBot(
        action="publish_script",
        script_path=test_script_path
    )
    print("Test 2 - Publish script:", bot.run()) 