from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

if '-e .' in install_requires:
    install_requires.remove('-e .')

__version__ = '0.0.1'

NAME = 'housing_price_prediction'
REPO_NAME = 'Housing-Price-Prediction'
AUTHOR_USER_NAME = 'shaderblade'
AUTHOR_EMAIL = 'shubhampandey140602@gmail.com'

setup(
    name=NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A machine learning model to predict Housing Prices in Bangalore",
    Long_description=long_description,
    Long_description_content='text/markdown',
    uri=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires
)