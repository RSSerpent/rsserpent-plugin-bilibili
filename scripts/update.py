#!/usr/bin/env python

import os
import shutil
import subprocess
from tempfile import gettempdir


basedir = gettempdir()
curdir = os.getcwd()
project = subprocess.run(
    ["poetry", "version"], capture_output=True, text=True  # type: ignore[call-overload]
).stdout.split()[0]
repo = os.path.join(basedir, project)

# create template
shutil.rmtree(repo, ignore_errors=True)
subprocess.run(["cookiecutter", "-f", "gh:rsserpent/template", "-o", basedir])
# initial commit
os.chdir(repo)
subprocess.run(["git", "checkout", "-b", "master"])
subprocess.run(["git", "add", "--all"])
subprocess.run(["git", "commit", "-m", "initial commit", "--no-verify"])
# merge update
os.chdir(curdir)
remote = "update-cookiecutter"
subprocess.run(["git", "remote", "rm", remote])
subprocess.run(["git", "remote", "add", remote, repo])
subprocess.run(["git", "remote", "update", remote])
subprocess.run(
    ["git", "merge", "--allow-unrelated-histories", "--squash", f"{remote}/master"]
)
