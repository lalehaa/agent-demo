from google.adk.agents import Agent
from google.adk.agents import llm_agent

from adk_short_bot.prompt import ROOT_AGENT_INSTRUCTION
from adk_short_bot.tools import count_characters

APP_NAME="adk_short_bot"


root_agent = Agent(
    name="adk_short_bot",
    model="gemini-2.5-flash-preview-04-17",
    description="A bot that shortens messages while maintaining their core meaning",
    instruction=ROOT_AGENT_INSTRUCTION,
    tools=[count_characters],
)
