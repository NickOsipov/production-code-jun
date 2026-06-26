from invoke import task


@task
def build(ctx):
    """Build the Docker image."""
    cmd = "docker build -t flask-app ."
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
