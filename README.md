# KMS-test

### Tests installation and run
- Instal chrome and chromedriver
- Clone the repository from github
- Install python3
```
https://www.python.org/downloads/
```
- Go to test project
```
cd ~path\to\KMS-test
```
- Create and activate Python Virtual ENV
```shell script
python3 -m venv --clear venv

source venv/bin/activate
```
- Install dependencies
```shell script
pip install -r requirements.txt
```
- Run the tests for landing page
```shell script
pytest -m landing
```
