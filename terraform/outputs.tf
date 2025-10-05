# outputs.tf

# 1. Output the final, globally unique bucket name
output "bucket_name" {
  description = "The globally unique name of the created GCS bucket."
  value       = module.gcs_buckets_databricks_lab.name
}
