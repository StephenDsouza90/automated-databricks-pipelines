import os
from setuptools import find_packages, setup


here = os.path.abspath(os.path.dirname(__file__))

packages = list(
    find_packages(
        exclude=[] # Add any package name that you want to exclude
    )
)

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="project_name",
    version="0.0.0",
    description="Project Description",
    long_description="Project Description",
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    packages=packages,
    package_dir={"project_name": "project_name"},
    package_data={
        "project_name": [
            "constants/*.json",
            "*.cer",
            "*.crt",
            "*.pem",
            # Add any other file that you want to include in the package
        ]
    },
    install_requires=required,
)

"""
NOTE: This is a basic setup.py file.
      You can add more configurations as per your project requirements.
      The setup.py is used to create a package of your project.
      The project that I worked on had a git submodule and since databricks does not support git submodules,
      I had to create a package of the project and then upload it to the databricks file system.
"""