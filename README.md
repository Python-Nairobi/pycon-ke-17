PyConKE 2017 Website Repo
==========

## INTRO
This repository contains the sources used to build the PyConKE 2017 Website.
We use [pelican](http://docs.getpelican.com) to build the contents of this repository
into the site you see at http://pycon.or.ke

## PREREQUIESITES
To contribute, we recommend you install:-

- [Python >= 2.7](https://www.python.org/download/releases/2.7)
- [PIP]("http://www.pip-installer.org/en/latest/installing.html)
- [virtualenv](http://www.virtualenv.org/en/latest/virtualenv.html)

## CLONING
1. <a href="https://github.com/Python-Nairobi/pyconke/fork" target="_blank">Click here to fork this Repo</a>.
2. Clone your fork and cd into it.
3. Create a virtualenv for your repo:- `mkvirtualenv -a . pyconke17web`.
4. Install the remaining dependencies:- `pip install -r requirements.txt`.
5. Initialize & update submodule dependencies (plugins, theme ..etc): `git submodule update --init --recursive`.
6. Then create a branch, naming it along the lines as your topic of contribution.

## EDITING
Start the development server:- `./develop_server.sh start`. Open http://127.0.0.1:8000 to view.
Any changes you make will automatically be reflected there.

1. Add, commit and push your changes.
2. Send us a pull request against [master](https://github.com/Python-Nairobi/pyconke/tree/master).

We'll review your contribution and maybe ask you to make further changes before we merge.
