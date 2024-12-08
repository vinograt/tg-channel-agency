from agency_swarm.tools import BaseTool
from pydantic import Field
import os

class ScriptEditor(BaseTool):
    """
    A tool to write and edit scripts in Markdown format.
    """
    content: str = Field(..., description="The content to write/edit")
    filename: str = Field(..., description="The filename to save the script to")
    
    def run(self):
        """
        Save or edit a script file in Markdown format.
        """
        script_path = f"scripts/{self.filename}.md"
        os.makedirs("scripts", exist_ok=True)
        
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(self.content)
            
        return f"Script saved to {script_path}"

if __name__ == "__main__":
    editor = ScriptEditor(
        content="# Test Script\nThis is a test script.",
        filename="test_script"
    )
    print(editor.run()) 