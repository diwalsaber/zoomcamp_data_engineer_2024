# Docker and PostGreSQL

## Introduction to Docker Compose
- Docker Compose is used for configuring multiple containers within a single YAML file, simplifying the management of shared networks and configurations.
- Benefit: reduces the complexity of Docker commands required to run multiple services.

## Installing Docker Compose
- **Mac and Windows**: Docker Compose is included with Docker Desktop.
- **Linux**: Requires manual installation.

## Configuration with Docker Compose
- Creating a `docker-compose.yaml` file to configure PostgreSQL and pgAdmin.
- **Configured Services**:
  - **PostgreSQL**: Definition of image, environment variables, volume mappings, and port mappings.
  - **pgAdmin**: Definition of image, environment variables, and port mappings.

## Execution with Docker Compose
- Launching services with the `docker-compose up` command.
- Accessing pgAdmin through a browser to connect to the PostgreSQL database.

## Useful Docker Management Commands
- **List running containers**: `docker ps`
- **List all containers (running and stopped)**: `docker ps -a`
- **Stop a running container**: `docker stop [container_id or names]`
- **Remove a container**: `docker rm [container_id or names]`
- **Pull a Docker image**: `docker pull [image_name]`
- **Build a Docker image**: `docker build -t [image_name] .`
- **View local Docker images**: `docker images`
- **Remove a Docker image**: `docker rmi [image_name]`

## Important Commands
- **Start Docker Compose**: `docker-compose up`
- **Stop Docker Compose**: `docker-compose down`
- **Detached mode**: Add the `-d` option to run in the background.

## Additional Docker Compose Command

### Executing Commands Inside Containers
- **Command**: `docker-compose exec -it ingest_data sh`
- **Purpose**: This command is used to execute a command inside a running container. In this case, it opens an interactive shell (`sh`) inside the container named `ingest_data`.
- **Components**:
  - `docker-compose exec`: This command allows the user to execute arbitrary commands in running containers managed by Docker Compose.
  - `-it`: This flag combo makes the execution interactive (`-i`) and allocates a pseudo-TTY (`-t`), which is essential for interactive shells.
  - `ingest_data`: The name of the service as defined in the `docker-compose.yaml` file. This should match the service you wish to access.
  - `sh`: The command executed inside the container. In this case, it's `sh`, a command interpreter or shell, which provides an interface for the user to interact with the operating system.

### Use Case
This command is particularly useful when you need to debug, modify, or interact with processes within your container. For example, you might use it to:
- View or edit files directly within the container's file system.
- Install temporary debugging tools or packages.
- Manually trigger scripts or applications within the container for testing purposes.

### Example Scenario
Imagine you've deployed a data ingestion service (`ingest_data`) using Docker Compose, and you need to inspect the environment or run a manual data import. Using `docker-compose exec -it ingest_data sh`, you can drop into the container's shell and execute the necessary commands directly, facilitating real-time debugging and interaction without stopping or restarting the container.

## Advantages of Docker Compose
- Simplifies the management of multiple configurations.
- Facilitates local experiments and integration testing.

# Terraform
- Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently.

## Key Terraform Commands
`init` - Get me the providers I need
`plan` - What am I about to do?
`apply` - Do what is in the tf files
`destroy` - Remove everything defined in the tf files


The transcription you've provided is a detailed walkthrough of using Terraform to manage resources on Google Cloud Platform (GCP). Below is a summary of the video content, formatted in Markdown, focusing on the Terraform commands and concepts discussed.

# Terraform on GCP - A Comprehensive Guide

## Setting Up Service Account for Terraform
**Description:** To interact with GCP, Terraform needs a service account with appropriate permissions.

**Commands:**
- Navigate to IAM & Admin > Service Accounts in GCP console.
- Create a new service account, e.g., terraformRunner.
- Assign roles such as Cloud Storage Admin and BigQuery Admin. For finer control, specific permissions can be granted based on the resources Terraform will manage.

## Generating and Handling Credentials
**Important:** Never expose your service account credentials. The video demonstrates creating a JSON key for the service account and emphasizes the security implications of mishandling such credentials.

## Terraform Configuration
**Initialization:**
- `terraform init` to initialize the working directory with required provider plugins.

**Creating a .tf file:**
- Use a `main.tf` file for Terraform configuration. This file includes the provider configuration and declares the resources to be managed.

**Provider Setup:**
- Example snippet for Google provider configuration:

```hcl
provider "google" {
  credentials = file("<PATH_TO_YOUR_SERVICE_ACCOUNT_JSON>")
  project     = "<YOUR_PROJECT_ID>"
  region      = "<DEFAULT_REGION>"
}
```

**Creating Resources:**
Example of creating a Google Cloud Storage (GCS) bucket:
```hcl
resource "google_storage_bucket" "demo_bucket" {
  name          = "terraform-demo-bucket"
  location      = "US"
  force_destroy = true
}
```
`terraform plan` and `apply` commands are used to preview and apply changes respectively.

## Terraform Commands Highlighted
- `terraform fmt` to format your .tf files for better readability.
- `terraform plan` to preview the changes Terraform will make.
- `terraform apply` to apply the changes defined in your Terraform configuration.
- `terraform destroy` to remove the resources defined in the Terraform configuration.

## Security and Best Practices
Sensitive Data Handling: The video underscores the importance of carefully managing sensitive information, such as service account keys, to avoid security breaches.
Version Control: Recommendations for using .gitignore with Terraform to prevent sensitive data from being pushed to version control systems like GitHub.


