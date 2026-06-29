from invoke import task


@task
def build(ctx):
    """Build the Docker image."""
    cmd = "docker build -t flask-app:latest ."
    ctx.run(cmd, pty=True)

@task
def stop(ctx):
    """Stop the Docker container."""
    cmd = "docker stop flask-app && docker rm flask-app"
    ctx.run(cmd, pty=True)

@task
def run(ctx):
    """Run the Docker container."""
    cmd = "docker run -p 5000:5000 --name flask-app flask-app"
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
