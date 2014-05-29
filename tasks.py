from invoke import run, task

@task
def publish():
   run('rm -f MANIFEST')
   run('./setup.py sdist upload')

