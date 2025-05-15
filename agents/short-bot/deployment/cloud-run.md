# Set your Google Cloud Project ID
export GOOGLE_CLOUD_PROJECT="agent-project-459312"

export PROJECT_NUMBER=69108108581

# Set your desired Google Cloud Location
export GOOGLE_CLOUD_LOCATION="us-central1" # Example location

# Set the path to your agent code directory
export AGENT_PATH="adk_short_bot"


# Set a name for your Cloud Run service (optional)
export SERVICE_NAME="short-bot-service"


# Set an application name (optional)
export APP_NAME="adk_short_bot"

# update service account permission 
gcloud projects add-iam-policy-binding agent-project-459312 \
    --member=serviceAccount:691081085814-compute@developer.gserviceaccount.com \
    --role=roles/storage.objectViewer

    # Grant the required role (replace [PROJECT_NUMBER] with the number):
gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
  --member="serviceAccount:691081085814@cloudbuild.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser"

# Deploy to cloud run
adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
--service_name=$SERVICE_NAME \
--app_name=$APP_NAME \
--with_ui \
$AGENT_PATH