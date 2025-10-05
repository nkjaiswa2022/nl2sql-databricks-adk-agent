# 🚀 Terraform Project: Infrastructure as Code (IaC)

This directory holds the Terraform configuration (`.tf`) files for managing infrastructure resources.

## Prerequisites

Ensure the following are installed before proceeding:

1.  **Terraform CLI:** Installed from the [official Terraform website](https://www.terraform.io/downloads).
2.  **Configuration Files:** All necessary `*.tf` files must be present in this directory.

---

## 🏗️ Core Terraform Workflow

The standard process uses three commands to initialize, review, and deploy infrastructure changes.

### 1. Initialization (`terraform init`)

This must be run first. It prepares the working directory by **downloading necessary provider plugins** and configuring the state management backend.

```bash
terraform init
```

### 2. Planning (`terraform plan`)

This command creates an execution plan, showing a detailed summary of proposed actions (Add +, Change ~, Destroy -) without making any real changes. Use this for review.

```bash
terraform plan
```

### 3. Application (`terraform apply`)

This executes the plan, making the actual modifications to your infrastructure. By default, it requires manual confirmation (yes).

```bash
terraform apply
```