# Set your Google Cloud Project ID
export GOOGLE_CLOUD_PROJECT="agent-project-459312"

# Set your desired Google Cloud Location
export GOOGLE_CLOUD_LOCATION="europe-west1" # Example location

# Set the path to your agent code directory
export AGENT_PATH="adk_short_bot"

# Set a name for your Cloud Run service (optional)
export SERVICE_NAME="bot-agent-service"

# Set an application name (optional)
export APP_NAME="bot-agent-app"

# update service account permission 
gcloud projects add-iam-policy-binding agent-project-459312 \
    --member=serviceAccount:691081085814-compute@developer.gserviceaccount.com \
    --role=roles/storage.objectViewer

# Deploy to cloud run
adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
--service_name=$SERVICE_NAME \
--app_name=$APP_NAME \
--with_ui \
$AGENT_PATH