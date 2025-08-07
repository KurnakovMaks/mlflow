#!/bin/bash

python3 create_s3_bucket.py

mlflow server \
       --backend-store-uri $MLFLOW_TRACKING_URI \
       --default-artifact-root s3://$BUCKET_NAME/ \
       --host 0.0.0.0 \
       --port 5000