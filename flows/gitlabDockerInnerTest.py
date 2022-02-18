import prefect
# import time
from prefect import task, Flow
from prefect.executors import LocalDaskExecutor
from prefect.storage import GitHub
from prefect.run_configs import DockerRun


prefect.context.setdefault("secrets", {})
# prefect.context.secrets["GITLAB_ACCESS_TOKEN"] = "wEWa254yEAx8xpnd9NK2"
prefect.context.secrets["GITHUB_ACCESS_TOKEN"] = "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"


# def myDockerRun():
#     logger = prefect.context.get("logger")
#     logger.info("myDockerRun start")
#
#     time.sleep(5)
#     logger.info(prefect.context.secrets)
#
#     logger.info(prefect.context.secrets["GITLAB_ACCESS_TOKEN"])
#
#     logger.info("myDockerRun start")

#    return DockerRun()

# https://github.com/klxsxian/prefect.git

STORAGE = GitHub(
    # host="https://github.com/",
    repo="klxsxian/prefect",
    path=f"flows/gitlabDockerInnerTest.py",
    # access_token_secret="GITHUB_ACCESS_TOKEN",
    # access_token_secret="GITHUB_ACCESS_TOKEN",
)

@task
def test_task():
    logger = prefect.context.get("logger")
    logger.info("Hello gitlabDockerInnerTest!")

with Flow(name="gitlabDockerInnerTest",
          # run_config=DockerRun(env={"GITLAB_ACCESS_TOKEN": "wEWa254yEAx8xpnd9NK2"}),
          run_config=DockerRun(),
          #run_config=myDockerRun(),
          storage=STORAGE,
          executor=LocalDaskExecutor()) as flow:
    # myDockerRun()
    test_task()