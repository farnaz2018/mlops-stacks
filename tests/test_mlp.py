from utils import (
    databricks_cli,
    generated_project_dir,
    parametrize_by_project_generation_params,
)
import pytest
import os


@parametrize_by_project_generation_params
def test_project_structure(generated_project_dir):
    # Test that the project structure is generated correctly
    project_dir = generated_project_dir / "my-mlops-project"
    assert project_dir.exists()
    
    # Check that training notebook exists
    training_notebook = project_dir / "my_mlops_project" / "training" / "notebooks" / "Train.py"
    assert training_notebook.exists()
