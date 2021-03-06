# gcp-ai-platform-hyperparameter-tuning-tf2
Perform Hyperparameter tuning on a small Regression problem using TensorFlow 2

### Run on Docker using AI platform
* Setup environment variables

```
export PROJECT_ID=$(gcloud config list project --format "value(core.project)")
export IMAGE_REPO_NAME=gcp_ai_platform_hyperparameter_tuning_tf2
export IMAGE_TAG=gcp_ai_platform_hyperparameter_tuning_tf2_image
export IMAGE_URI=us.gcr.io/$PROJECT_ID/$IMAGE_REPO_NAME:$IMAGE_TAG
```

* Build Docker image

<pre><code>docker build -f Dockerfile -t $IMAGE_URI ./</code></pre>

* Push the Docker image to GCP container registry

<pre><code>docker push $IMAGE_URI</code></pre>

* Prepare hyperparameter tuning config file

In the `hptuning_config.yaml` you add the parameters to optimize with your hyperparameter tuning, and provide arguments to your code as hyperparameters that will be used to optimize. You can also specifiy the job submission details like parallel jobs to run and how many jobs to run.

* Training with hyperparameter tuning on AI platform using Docker

Initialize input variabless
```
export REGION=us-central1
export JOB_NAME=gcp_ai_platform_hyperparameter_tuning_tf2_$(date +%Y%m%d_%H%M%S)
```
Submit the jobs
<pre><code>
gcloud ai-platform jobs submit training $JOB_NAME --scale-tier BASIC --region $REGION --master-image-uri $IMAGE_URI --config hptuning_config.yaml
</code></pre>
