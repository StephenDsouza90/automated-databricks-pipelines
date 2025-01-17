# Automated Databricks Pipelines

This repository provides a robust and automated solution for managing Databricks pipelines, including the creation, updating, and orchestration of data workflows. It integrates seamlessly with GitHub Actions to enable CI/CD, automating the deployment of Python packages and managing job configurations on Databricks.

## Features
- **Automated Pipeline Management**: Automatically create or update Databricks workflows from JSON configurations.
- **Python Package Deployment**: Build and deploy Python wheels directly to Databricks File System (DBFS).
- **Workflow Chaining**: Configure task dependencies for complex workflows, ensuring seamless execution from preprocessing to training.
- **GitHub Actions Integration**: Streamline your CI/CD process for Databricks workflows and code changes.
- **Environment-Specific Configuration**: Use secrets and environment variables for secure and flexible setups.

## Workflow Automation with GitHub Actions
The pipeline.yaml workflow automates the following steps:
- Checks out the repository.
- Installs Python 3.10 and necessary dependencies.
- Builds a Python wheel package from the project.
- Deploys the wheel package to DBFS.
- Syncs GitHub repository changes with Databricks Repos.
- Creates or updates Databricks workflows using JSON configurations.

**Triggering the Workflow**

The pipeline runs automatically when you:
- Push changes to the <branch_name> branch.
## Repository Structure
```
├── .github/
│   └── workflows/
│       └── pipeline.yaml   # GitHub Actions workflow for managing Databricks jobs
├── services/
│   └── databricks/
│       ├── workflow_1.json # Configuration for Workflow 1
│       ├── workflow_2.json # Configuration for Workflow 2
├── submodel/
│   ├── constants/          # Constant files
│   ├── utils/              # Utils files
├── setup.py                # Python package setup
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```


