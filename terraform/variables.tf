# variables.tf

# 1. Google Cloud Project ID
variable "gcp_project_id" {
  description = "The ID of the Google Cloud Project to deploy resources into."
  type        = string
  default     = "arj-poc-0905" 
}

# 2. Bucket Location/Region
variable "bucket_location" {
  description = "The region or multi-region location for the GCS bucket (e.g., US, EU, asia-south1)."
  type        = string
  default     = "us-central1" 
}