from invoke import task

from config.variables import (
    REGISTRY_USER,
    IMAGE_NAME,
    CONTAINER_NAME,
    REMOTE_HOST,
    REMOTE_PATH,
    SSH_KEY_PATH,
    SSH_USER,
)


@task
def build(ctx):
    """Build the Docker image."""
    cmd = f"docker build -t {IMAGE_NAME}:latest ."
    ctx.run(cmd, pty=True)


@task
def push(ctx):
    """Push the Docker image to a registry."""
    cmd = f"docker tag {IMAGE_NAME}:latest {REGISTRY_USER}/{IMAGE_NAME}:latest"
    ctx.run(cmd, pty=True)
    cmd = f"docker push {REGISTRY_USER}/{IMAGE_NAME}:latest"
    ctx.run(cmd, pty=True)


@task
def stop(ctx):
    """Stop the Docker container."""
    cmd = f"docker stop {CONTAINER_NAME} && docker rm {CONTAINER_NAME}"
    ctx.run(cmd, pty=True)


@task
def run(ctx):
    """Run the Docker container."""
    cmd = f"docker run -p 5000:5000 --name {CONTAINER_NAME} {IMAGE_NAME}"
    ctx.run(cmd, pty=True)


@task
def up(ctx):
    """
    Start the Docker containers defined in the docker-compose file.
    """
    cmd = "docker compose up -d"
    ctx.run(cmd, pty=True)


@task
def down(ctx):
    """
    Stop the Docker containers defined in the docker-compose file.
    """
    cmd = "docker compose down"
    ctx.run(cmd, pty=True)


@task
def scp(ctx):
    """
    Copy files to a remote host using SCP.
    """

    cmd = f"scp -i {SSH_KEY_PATH} -r docker-compose.yml migrations {SSH_USER}@{REMOTE_HOST}:{REMOTE_PATH}"
    ctx.run(cmd, pty=True)

@task
def deploy(ctx):
    """
    Deploy the application to a remote host.
    """
    cmd = f"ssh -i {SSH_KEY_PATH} {SSH_USER}@{REMOTE_HOST} 'cd {REMOTE_PATH} && docker compose down && docker compose up -d'"
    ctx.run(cmd, pty=True)
