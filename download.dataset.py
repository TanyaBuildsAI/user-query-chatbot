import kagglehub

# Download the latest version of the dataset
path = kagglehub.dataset_download("PromptCloudHQ/all-jc-penny-products")

print("Path to dataset files:", path)
