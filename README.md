# Simple Python Route Implementation

produce a simple Python implementation of the type of server-side route you would see in a Node.js Express app. The focus is just on the route—there is no authentication, and there is no middleware.

## Installation
1. Clone this repository to your local machine.
2. Install  dependencies :
`pip install -r requirements.txt`

## Running the App
You can run this app in test mode using one of the following commands:
- Using Hypercorn:
`hypercorn -b 127.0.0.1:5001  main:app`

- Using FastAPI:
`fastapi dev --port 5001 --reload main.py`

## Example Usage
Call the service from an HTTP client such as curl:

`curl http://localhost:5001/script?body=Week%201%20commanded%20our%20attention%20even%20before%20the%20games%20kicked%20off%20Sunday.%20%3Ca%20class%3D%22ath_autolink%22%20data-id%3D%221NrLfCowWevnKYEe`


Alternatively, you can paste the URL above into a browser.

## Functionality
This service renders a block of native HTML scraped from some web page elsewhere on the internet and presents it in an easily readable format. It can also be useful for accessing content that may be restricted by paywalls.

# Skeleton structure for a new python project

I've developed this bare-bones new project structure after developing and distributing several python applications. 
I found it to work best for the later deployment of a python project either with local sdist or deployed to PyPi.
For other ways to create a project template, see Cookiecutter open source project: 
https://cookiecutter.readthedocs.io/en/latest/readme.html

## To use:
Just copy it, rename the obviously named keywords and start coding.

## To deploy
Create 2 distributions:
- Source Distribution or sdist (contains source code)
- Build distribution or Wheel (platform dependent build, i.e. need one for each platform if code is not platform-independent)

To upload to PyPi, will need install twine:
> pip install twine
(Also this command: python -m pip install --user --upgrade twine)

#### Create local distributions (source and wheel):
python setup.py sdist bdist_wheel

#### Install and test local source distribution
Copy app.tar.gz from created dist directory to some test directory
In testdirectory, create and source new venv, deploy your package there:

> virtualenv venv

> source venv/bin/activate

> pip install app.tar.gz

If yaml files were distributed with the app, they will be in venv/lib/python3.6/site-packages/app-package (so will be the code)

Uninstall: just delete the venv and your test directory

#### Deploy to PyPi test package manager
http://devarea.com/deploying-a-new-python-package-to-pypi/

Create and place in a home directory a .pypirc file. - This did not work for me: need to enter passwd anyways.

Upload an existing dist to PyPi
> twine upload --repository-url https://test.pypi.org/legacy/ dist/*

WARNING: PyPI does not allow for a filename to be reused, even once a project has been deleted and recreated. If things don't work, you can change the version number and re-upload, but not re-upload same project and same version.

##### Install from PyPi test
In a test venv do:

> pip install -i https://testpypi.python.org/pypi myapp

> python -m pip install --index-url https://test.pypi.org/simple/ brdm


#### Deploy to real PyPi

twine upload dist/*

###### Install from PyPi
In a test venv do:

> pip install -i https://pypi.org/pypi myapp

> pip install 'myapp'

> pip install 'myapp==0.1'


## To create and deploy Wheel