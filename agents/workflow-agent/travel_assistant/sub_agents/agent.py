from google.adk.agents import Agent
from google.adk.agents import llm_agent
from google.adk.tools import google_search
from .prompt import Core_AGENT_INSTR
from google.adk.tools.agent_tool import AgentTool



event_agent = Agent(
    model="gemini-2.5-flash-preview-04-17",
    name="event_agent",
    description="This agent suggests key events and news given some user preferences",
    instruction="This agent suggests key events and news given some user preferences.You can answer your questions by searching the internet.",
    tools=[google_search],
)
core_agent = Agent(
    name="core_agent",
    model="gemini-2.5-flash-preview-04-17",
    description="A Travel A travel guid agent who help users, and discover their next vacations; Provide information about places, weather , events , news, activities and interests,",
    instruction=Core_AGENT_INSTR,
    tools=[AgentTool(agent=event_agent)]
   
)
