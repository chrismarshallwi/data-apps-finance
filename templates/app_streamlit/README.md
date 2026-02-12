# 📊 Project Name
Demo of best practices for apps.

## 🚀 Overview
Refer to the app [README](src/app_streamlit/README.md).

## 🏗️ Architecture

- **Data Sources**: mostly syntatic data
- **Visualization**: Tables and charts


## 🛠️ Tech Stack

- Language: Python
- Frameworks: Streamlit
- Deployment: DAB

## 📦 Setup Local Environment
Dependencies:
- Python 3.10+
- uv

```powershell
# Clone the repo
git clone REPO_URL
cd REPO_NAME
# Create a virtual environment
cd project-templates/app_streamlit/src/app_streamlit
uv venv .venv
# vscode will automatically detect the virtual environment
# If not, you can manually select it in the bottom left corner of VSCode
# If you are using PowerShell, you may need to set the execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Activate the virtual environment
.\.venv\Scripts\activate.ps1
# Install dependencies
uv pip install -r requirements.txt
```

## 📈 Run App
```bash
# Assuming you have the profile CORE_D setup already
databricks apps run-local -p CORE_D
```
