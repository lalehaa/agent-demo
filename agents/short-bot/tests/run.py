import dotenv
dotenv.load_dotenv()  # May skip if you have exported environment variables.
from vertexai import agent_engines

agent_engine_id = "3381860272527376384" #Remember to update the ID here. 
user_input = "Hello, can you help me find a summer dress? I want something flowy and floral."

agent_engine = agent_engines.get(agent_engine_id)
session = agent_engine.create_session(user_id="new_user")
for event in agent_engine.stream_query(
    user_id=session["user_id"], session_id=session["id"], message=user_input
):
    for part in event["content"]["parts"]:
        print(part["text"])