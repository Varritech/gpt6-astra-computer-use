#!/usr/bin/env python3
"""GPT-6 Style Computer Use Agent - Main Entry Point"""

import argparse, base64, io, os, sys, json
from typing import Dict, Optional
import pyautogui
from PIL import Image
from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger(__name__)
console = Console()

class ComputerUseAgent:
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not set")
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        
    def capture_screenshot(self) -> str:
        screenshot = pyautogui.screenshot()
        buffer = io.BytesIO()
        screenshot.save(buffer, format="JPEG", quality=80)
        buffer.seek(0)
        return base64.b64encode(buffer.read()).decode('utf-8')
    
    def analyze_screen(self, screenshot_b64: str, task: str, step: int, max_steps: int) -> Dict:
        messages = [{
            "role": "user",
            "content": [
                {"type": "text", "text": f"You are a computer use agent. Task: {task}. Step {step}/{max_steps}. Available actions: click, type, press, scroll, double_click, done. Respond in JSON: {{action, x, y, text, key, direction, reasoning}}"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{screenshot_b64}"}}
            ]
        }]
        response = self.client.chat.completions.create(model=self.model, messages=messages, max_tokens=500, temperature=0.1)
        content = response.choices[0].message.content.strip()
        if "```json" in content: content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content: content = content.split("```")[1].split("```")[0].strip()
        try: return json.loads(content)
        except: return {"action": "done", "reasoning": "Parse error"}
    
    def execute_action(self, action: Dict) -> bool:
        action_type = action.get("action")
        try:
            if action_type == "click": pyautogui.click(action.get("x"), action.get("y"))
            elif action_type == "type": pyautogui.write(action.get("text", ""), interval=0.05)
            elif action_type == "press": pyautogui.press(action.get("key", ""))
            elif action_type == "scroll": pyautogui.scroll(3 if action.get("direction","down")=="down" else -3)
            elif action_type == "done": return True
            pyautogui.sleep(0.5)
            return True
        except Exception as e:
            log.error(f"Action failed: {e}")
            return False
    
    def run(self, task: str, max_steps: int = 20, demo_mode: bool = False) -> bool:
        console.print(Panel(f"[bold blue]Task:[/bold blue] {task}", title="🤖 Computer Use Agent"))
        for step in range(1, max_steps + 1):
            if demo_mode: console.print(f"\n[yellow]Step {step}/{max_steps}[/yellow]")
            screenshot_b64 = self.capture_screenshot()
            action = self.analyze_screen(screenshot_b64, task, step, max_steps)
            if demo_mode: console.print(f"[cyan]Action:[/cyan] {action.get('action')}")
            if self.execute_action(action) and action.get("action") == "done":
                console.print("[green]✓ Task completed![/green]")
                return True
        console.print("[yellow]⚠ Max steps reached[/yellow]")
        return False

def main():
    parser = argparse.ArgumentParser(description="Computer Use Agent")
    parser.add_argument("--task", type=str, help="Task description")
    parser.add_argument("--api-key", type=str)
    parser.add_argument("--model", type=str, default="gpt-4o")
    parser.add_argument("--max-steps", type=int, default=20)
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.task and not args.demo:
        parser.print_help()
        sys.exit(1)
    try:
        agent = ComputerUseAgent(api_key=args.api_key, model=args.model)
        if args.demo:
            console.print("[bold green]Demo mode. Type 'quit' to exit.[/bold green]")
            while True:
                task = input("\nEnter task: ").strip()
                if task.lower() in ['quit', 'exit', 'q']: break
                if task: agent.run(task, max_steps=args.max_steps, demo_mode=True)
        else:
            success = agent.run(args.task, max_steps=args.max_steps, demo_mode=args.demo)
            sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted[/yellow]")
        sys.exit(130)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    main()
