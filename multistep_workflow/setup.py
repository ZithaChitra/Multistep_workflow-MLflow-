from setuptools import setup, find_packages
from codecs import open
from os import path


__version__ = "0.0.4"

here = path.abspath(path.dirname(__file__))

# get the dependencies and installs
with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")

install_requires = [x.strip() for x in all_reqs if "git+" not in x]
dependency_links = [x.strip().replace("git+", "") for x in all_reqs if x.startswith("git+")]



setup(
    name="Multistep-workflow",
    version=__version__,
    description="Multi step ML workflow using Mlflow",
    url="",
    download_url="",
    license="",
    packages=find_packages("mlproject", "mlproject*"),
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=[],
    dependency_links=dependency_links,
    author_email="email@gmail.com",


 )


