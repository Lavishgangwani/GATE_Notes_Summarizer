import os

import argparse

from pathlib import Path

from typing import Dict, Union, Any

import yaml
 
class ProjectTemplate:

    def __init__(self, project_name: str, output_dir: str):

        self.project_name = project_name

        self.output_dir = output_dir

        self.base_path = Path(output_dir).resolve()
 
    def get_template_config(self) -> Dict[str, Any]:

        """Load project structure and files from a YAML configuration"""

        return {

            "directories": [

                "app",

                "app/api/v1/endpoints",

                "app/api/v1/models",

                "app/core",

                "app/services/ai_clients",

                "app/services/costings",

                "app/utils",

                "tests/test_api",

                "tests/test_services"

            ],

            "files": self._get_file_templates()

        }
 
    def _get_file_templates(self) -> Dict[str, str]:

        """Define file contents in a structured way"""

        return {

            ".env": self._get_env_template(),

            "requirements.txt": self._get_requirements_template(),

            "Dockerfile": self._get_dockerfile_template(),

            "README.md": self._get_readme_template(),

            "app/main.py": self._get_main_template(),

            # Add other file templates...

        }
 
    def create(self) -> Path:

        """Create the project structure"""

        config = self.get_template_config()

        project_root = self.base_path / self.project_name
 
        # Create directories

        for directory in config["directories"]:

            (project_root / directory).mkdir(parents=True, exist_ok=True)
 
        # Create files

        for file_path, content in config["files"].items():

            full_path = project_root / file_path

            full_path.parent.mkdir(parents=True, exist_ok=True)

            full_path.write_text(content)
 
        # Create empty __init__.py files

        self._create_init_files(project_root)

        return project_root
 
    def _create_init_files(self, root_path: Path):

        """Create empty __init__.py files in all Python packages"""

        for path in root_path.rglob("**/"):

            if any(path.glob("*.py")):

                init_file = path / "__init__.py"

                init_file.touch(exist_ok=True)
 
 
    # Template methods

    def _get_env_template(self) -> str:

        return f'''# Environment variables

PROJECT_NAME="{self.project_name}"

VERSION="1.0.0"

'''
 
    def _get_requirements_template(self) -> str:

        return '''fastapi

uvicorn

pydantic

python-dotenv

pydantic-settings

'''
 
    def _get_dockerfile_template(self) -> str:

        return '''# Use an official Python runtime as a parent image

FROM python:3.9-slim
 
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
 
COPY . .

EXPOSE 80
 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

'''
 
    def _get_readme_template(self) -> str:

        return f'''# {self.project_name}
 
This is a Python-based API for Generative AI Agents.

'''
 
    def _get_main_template(self) -> str:

        return f'''from fastapi import FastAPI

from app.api.v1.endpoints import chat, generate

from app.core.config import settings
 
app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
 
app.include_router(chat.router, prefix="/api/v1/chat", tags=["chat"])

app.include_router(generate.router, prefix="/api/v1/generate", tags=["generate"])
 
@app.get("/")

def read_root():

    return {{"message": "Welcome to {self.project_name}"}}

'''
 
def setup_args() -> argparse.Namespace:

    """Set up command-line arguments"""

    parser = argparse.ArgumentParser(

        description="Create Generative AI API project structure"

    )

    parser.add_argument(

        "-n",

        "--project-name",

        help="Name of the project",

        required=True,

    )

    parser.add_argument(

        "-d",

        "--output-dir",

        default=".",

        required=True,

        help="Output directory for the project (default: current directory)",

    )

    return parser.parse_args()
 
def main():

    args = setup_args()

    template = ProjectTemplate(args.project_name, args.output_dir)

    project_path = template.create()

    print(f"Project '{args.project_name}' created at: {project_path}")
 
if __name__ == "__main__":

    main()
 