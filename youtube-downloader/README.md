# Youtube to MP3 Converter

## About 

Sample web tests that use [320youtube](https://www.320youtube.com/) site to convert videos to high quality mp3 files.

Technologies:
- [pytest](https://pypi.org/project/pytest/) as unit testing framework.
- [pytest-xdist](https://pypi.org/project/pytest-xdist/) to run tests in parallel.
- [selenium](https://pypi.org/project/selenium/) to drive browsers.
- [webdrivermanager](https://pypi.org/project/webdrivermanager/) to handle browser drivers.

## Requirements

- [Python 3.8](https://www.python.org/downloads/) 
- [pipenv](https://pipenv-fork.readthedocs.io/en/latest/)

## Usage

- Add links to videos you want to download in `<project>/data/playlist.json`
- Open terminal and go to project home
- Run `pipenv install` to ensure all dependencies are available 
- Run `pipenv run pytest -s -n <number-of-parallel-downloads>`
- Get your `mp3` files from `<project>/out` folder
