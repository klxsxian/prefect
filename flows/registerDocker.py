import prefect
from prefect import task, Flow
from prefect.run_configs import DockerRun
from prefect.executors import LocalDaskExecutor
from prefect.storage import GitHub

# prefect.context.setdefault("secrets", {}) # to make sure context has a secrets attribute
# prefect.context.secrets["GITLAB_ACCESS_TOKEN"] = "H9VCeBpnf7z7kTD7HA2K"

STORAGE = GitHub(
    # host="https://github.com/",
    repo="klxsxian/prefect",
    path=f"flows/registerDocker.py",
    # access_token_secret="GITHUB_ACCESS_TOKEN",
    access_token_secret="GITHUB_ACCESS_TOKEN",
)
@task
def my_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")

with Flow(name="test-prefectDocker",
          run_config=DockerRun(),
          storage=STORAGE,
          executor=LocalDaskExecutor()) as flow:
    my_task()
