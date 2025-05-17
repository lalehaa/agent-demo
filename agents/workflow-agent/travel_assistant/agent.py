from google.adk.agents import Agent
from google.adk.agents import llm_agent
from .prompt import ROOT_AGENT_INSTRUCTION
from .sub_agents.agent import core_agent

APP_NAME="travel-assistant"

root_agent = Agent(
    name="travel_assistant",
    model="gemini-2.5-flash-preview-04-17",
    description="A Travel concierge",
    instruction=ROOT_AGENT_INSTRUCTION,
    sub_agents=[
        core_agent
    ],
)
