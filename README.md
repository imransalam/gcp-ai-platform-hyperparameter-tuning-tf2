# gcp-ai-platform-hyperparameter-tuning-tf2
Perform Hyperparameter tuning on a small Regression problem using TensorFlow 2

### Run with Docker image on Vertex AI
* Setup environment variables

```
export REGION=us-central1
export PROJECT_ID=$(gcloud config list project --format "value(core.project)")
export IMAGE_REPO_NAME=gcp_vertex_ai_hyperparameter_tuning_tf
export IMAGE_TAG=latest
export IMAGE_URI=us-central1-docker.pkg.dev/$PROJECT_ID/$IMAGE_REPO_NAME:$IMAGE_TAG
gcloud auth configure-docker $REGION-docker.pkg.dev
```

* Build Docker image

<pre><code>docker build -f Dockerfile -t $IMAGE_URI ./</code></pre>

* Push the Docker image to GCP artifacts registry

<pre><code>docker push $IMAGE_URI</code></pre>

* Prepare hyperparameter tuning config file

In the `hptuning_config.yaml` you add the parameters to optimize with your hyperparameter tuning and provide arguments to your code as hyperparameters that will be used to optimize. You can also specify the job submission details like parallel jobs to run and how many jobs to run.

* Training with hyperparameter tuning on the Vertex AI platform from Docker image

Initialize input variables
```
export JOB_NAME=gcp_vertex_ai_hyperparameter_tuning_tf
```
Submit the jobs
<pre><code>
gcloud ai hp-tuning-jobs create --region $REGION --config hptuning_config.yaml --project=$PROJECT_ID --display-name=$JOB_NAME
</code></pre>
