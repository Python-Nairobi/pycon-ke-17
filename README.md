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
5. Initialize & update submodule dependencies (plugins, theme & skulpt interpreter): `git submodule update --init --recursive`.
6. Then create a branch, naming it along the lines as your topic of contribution.

## EDITING
Start the development server:- `./develop_server.sh start`. Open http://127.0.0.1:8000 to view.
Any changes you make will automatically be reflected there.


### MARKDOWN
![Markdown, do you speak it?](content/img/markdown!%20do%20you%20speak%20it%3F.jpg)
The ["recent developments"](http://localhost:8000/#developments) articles/posts are
written in [MarkDown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
from the [`content`](content/) folder.
Your markdown files should end with a `.md`, `.markdown`, or `.mkd` file extension.
You should also include some metadata at the top of your markdown files.
Checkout the example bellow and adapt appropriately:-

```
Title: Blog post title
Date: YYYY-MM-DD HH:MM
Tags: tag1, tag2
Category: Relevant_Category
Slug: short_descriptive_article_name
Author: Your Name (github_handle)
Summary: A summary of your blog post content
about_author: A brief summary about you
email: used to display your [gravar](https://gravatar.com/) in the article.

Blog Post Content Goes Here.
```
You can also `cp content/article.md.template content/new_article.md` and `vi content/new_article.md` appropriately.
Feel free to write portions of your article in html to compensate for where markdown falls short
e.g. opening links in new tabs. (Jules is ok with this)

## FINALLY
1. Add, commit and push your changes.
2. Send us a pull request against [master](https://github.com/Python-Nairobi/pynbo-blog/tree/master).

We'll review your contribution and maybe ask you to make further changes before we merge.
