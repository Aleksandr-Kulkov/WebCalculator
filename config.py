import os
import yaml
from pathlib import Path

DIR_PREFIX = Path(__file__).parent


# Чтение yaml
def yaml_file_type(yaml_file_path):
    with open(yaml_file_path) as f:
        return yaml.load(f.read(), Loader=yaml.Loader)


CONFIG = yaml_file_type('config.yaml')