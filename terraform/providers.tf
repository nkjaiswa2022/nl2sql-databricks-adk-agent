/*
terraform {
  required_providers {
    google = {
      version = "3.90.1"
    }
    google-beta = {
      version = "3.90.1"
    }
  }
}
*/

provider "google" {
  project = var.gcp_project_id
  region  = var.bucket_location
}

provider "google-beta" {
  project = var.gcp_project_id
  region  = var.bucket_location
}
