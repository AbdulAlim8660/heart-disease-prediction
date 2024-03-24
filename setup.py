import setuptools

with open ("Readme.md",'r',encoding='utf-8') as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME='heart-disease-prediction'
AUTHOR_USERNAME='AbdulAlim8660'
SRC_REPO='heart_disease_project'
AUTHOR_EMAIL='aabaig14@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for ML app',
    long_description=long_description,
    url=f'https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}',
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
)