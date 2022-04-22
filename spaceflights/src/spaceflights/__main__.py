"""spaceflights file for ensuring the package is executable
as `spaceflights` and `python -m spaceflights`
"""
import sys
from pathlib import Path
from typing import Optional, List

from kedro.framework.project import configure_project, run

# used by databricks and console_scripts
# note databricks just does ['--pipeline=ds'] for kwargs
# and ['-p', 'dp'] for args
# always use list of strings for args
def main(args: Optional[List[str]] = None, **kwargs) -> None:
    package_name = Path(__file__).parent.name
    configure_project(package_name)
    run(args or sys.argv[1:], **kwargs)


if __name__ == "__main__":
    sys.exit(main())

# Allows run(["--pipeline", "ds"]) - non-breaking and needed for databricks
# In Ipython, use `from kedro.framework.project import run`
# In other scripts, need to call `configure_project` first
# In future could alias in __init__.py if wanted to expose `from spaceflights import run` there or change entrypoint

# shouldn't need to pip install before call main function
# note do click multiple arguments as tag=["blah", "blah2"]


# This version allows run (["--pipeline", "ds"]) but we don't have to
# Overloading main so it works in script and as main entry point for Python API. Ugly import, weird name (main rather than run, but could change this), system exit code problem.
# Instead use main as entry point for computer, run for humans.
