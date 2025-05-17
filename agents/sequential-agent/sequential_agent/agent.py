from google.adk.agents import Agent , sequential_agent
from google.adk.agents import llm_agent
from .prompt import ROOT_AGENT_INSTRUCTION
from .sub_agents.agent import core_agent
model = "gemini-2.5-flash-preview-04-17"



research_agent= Agent(
    name="research_agent",
    instruction="You will research on a provided topic and share the output of research",
    model=model_abstraction,
    output_key="research_content"
)

reviewer_agent= Agent(
    name="reviewer_agent",
    instruction="""You are an expert reviewer.
    You will review the below provided content and make changes to make 
    the content more engaging and impactful
    
    **Content to review**
    {research_content}
    
    """,
    model=model,
    output_key="reviewed_content"
)

linkedin_poster = Agent(
    name="linkedin_agent",
    instruction="""You are an expert writer of articles in LinkedIn.
    You will be provided with a research content. You will need to create 
    an impactful title for the content. You will also format the content 
    aligning it to LinkedIn article format. The final title and content output 
    muat be ready to be posted in LinkedIn 

    **Content to review**
    {reviewed_content}

    """,
    model=model_abstraction,
    output_key="linkedin_content"
)

research_pipeline_agent = SequentialAgent(
    name="LinkedInPostPipelineAgent",
    sub_agents=[research_agent, reviewer_agent,linkedin_poster],
    description="Executes a sequence of research and research review activity.",
    # The agents will run in the order provided: Writer -> Reviewer -> Refactorer
)

root_agent = research_pipeline_agent
