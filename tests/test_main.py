"""Test the framework"""

import os
from expreccs.core.expreccs import main


def test():
    """See configs/*.txt"""
    cwd = os.getcwd()
    os.chdir(f"{cwd}/tests/configs")
    main()
    os.chdir(f"{cwd}/tests/configs")
    os.system("expreccs -i wells.txt -m site -p no -r opm")
    os.chdir(f"{cwd}/tests/configs")
    os.system("expreccs -i interp.txt -m site -p no -r opm")
    os.chdir(f"{cwd}/tests/configs")
    os.system("expreccs -i flux.txt -m site -p yes -r opm")
    os.chdir(f"{cwd}/tests/configs")
    os.system("expreccs -c compare -r opm")
    assert os.path.exists("./compare/distance_from_border.png")
    os.chdir(cwd)
