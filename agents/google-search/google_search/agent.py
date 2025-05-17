from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types
from google_search.prompt import ROOT_AGENT_INSTRUCTION


APP_NAME="google_search"

root_agent = Agent(
    name="google_search",
    model="gemini-2.5-flash-preview-04-17",
    description="Agent to answer questions using Google Search.",
    instruction="I can answer your questions by searching the internet. Just ask me anything!",
       tools=[google_search]
)
