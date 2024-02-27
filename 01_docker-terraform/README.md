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

## Advantages of Docker Compose
- Simplifies the management of multiple configurations.
- Facilitates local experiments and integration testing.