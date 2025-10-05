module "gcs_buckets_databricks_lab" {
  source     = "terraform-google-modules/cloud-storage/google//modules/simple_bucket"
  version    = "5.0"
  name       = "${var.gcp_project_id}-bucket"
  project_id = var.gcp_project_id
  location   = var.bucket_location
  versioning = false
  iam_members = [
  ]
}