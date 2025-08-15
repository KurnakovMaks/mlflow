import mlflow
runs = mlflow.search_runs(experiment_ids="0")
def get_best_model(experiment_id, metric_name='accuracy'):
    runs = mlflow.search_runs(experiment_ids=experiment_id)
    best_accuracy = 0
    best_run_id = None
    for index, run in runs.iterrows():
        run_id = run['run_id']
        run_data = mlflow.get_run(run_id).data
        run_metrics = run_data.metrics

        if metric_name in run_metrics:
            accuracy = run_metrics[metric_name]
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_run_id = run_id

    return best_run_id, best_accuracy
best_run_id, best_accuracy = get_best_model("0")
if best_run_id:
    print(f"Best model found in experiment '{0}'")
    print(f"Best Run ID: {best_run_id}")
    print(f"Accuracy: {best_accuracy}")
else:
    print("No model with the specified metric found in the experiment.")