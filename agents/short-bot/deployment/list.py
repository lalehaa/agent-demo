import vertexai
from vertexai.preview import reasoning_engines
from dotenv import load_dotenv
import os

load_dotenv()

cloud_project = os.getenv("GOOGLE_CLOUD_PROJECT")
cloud_location = os.getenv("GOOGLE_CLOUD_LOCATION")
storage_bucket = os.getenv("GOOGLE_CLOUD_STAGING_BUCKET")


vertexai.init(project=cloud_project, location=cloud_location)

reasoning_engine_list = reasoning_engines.ReasoningEngine.list()
print(reasoning_engine_list)