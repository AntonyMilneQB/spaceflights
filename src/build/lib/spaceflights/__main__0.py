"""spaceflights file for ensuring the package is executable
as `spaceflights` and `python -m spaceflights`
"""
import sys

from kedro.framework.project import (
    run,
)  # or from . import  run and then no need to call configure_project


def main():
    configure_project("spaceflights")
    run(sys.argv[1:])


if __name__ == "__main__":
    main()
    # sys.exit()

# This method you would do from kedro.framework.project import run in ipython since `configure_project` has been called already
# You don't get nice signature for main this way (not so important).
# Test for this solution and for configure_project in __init__.py (solution with no number).
# Test against all entrypoint including databricks with kwargs.

# shouldn't need to pip install before call main function
# note do click multiple arguments as tag=["blah", "blah2"]


# This version allows run (["--pipeline", "ds"]) but we don't have to
# Overloading main so it works in script and as main entry point for Python API. Ugly import, weird name (main rather than run, but could change this), system exit code problem.
# Instead use main as entry point for computer, run for humans.
# Can fix by putting in __init__.py as run instead. This is solution 1. from spaceflights import run
# End up with lots of weird code in __init__.py. Move as much of it framework side as possible but docstrings will remain.
# Could move to framework.project.__init__. This is current solution. from kedro.framework.project import run. Need to do configure_project first or embed in run command.
# Could keep spaceflights.run pointing to this.


# kedro.framework.project.run as configurable class makes sense with project-level CLI command. But cli.py isn't central component in same way that settings, pipelines is - might not exist.
# Potentially confusing with cli.py run command if leave in project __init__.py? But most people won't have cli.py.
