from setuptools import setup, find_packages

try:
    with open('README.md') as file:
        long_description = file.read()
except UnicodeDecodeError:
    long_description = ''
except FileNotFoundError:
    long_description = ''

requirements = [
    'fastapi == 0.60.1',
    'loguru == 0.5.3',
    'gunicorn == 20.0.4',
    'uvicorn == 0.10.3',
    'Jinja2 == 2.10.1',
    'pymongo == 3.11.1',
    'pymongo[srv] == 3.11.1',
    'aiofiles == 0.5.0',
    'SQLAlchemy == 1.3.19'
]

setup(
    name='Fast API Project',
    version='1.0.0',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements
)
