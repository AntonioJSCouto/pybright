Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

### Report Bugs

Report bugs at
<https://github.com/plavjanik/pybright/issues>.

If you are reporting a bug, please include:

-   Your operating system name and version.
-   Any details about your local setup that might be helpful in
    troubleshooting.
-   Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with \"bug\" is
open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
\"feature\" is open to whoever wants to implement it.

### Write Documentation

`pybright` could always use more documentation, whether as part
of the official pypright docs, in docstrings, or even on the
web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at
<https://github.com/plavjanik/pybright/issues>.

If you are proposing a feature:

-   Explain in detail how it would work.
-   Keep the scope as narrow as possible, to make it easier to
    implement.
-   Remember that this is a volunteer-driven project, and that
    contributions are welcome :)

Get Started!
------------

Ready to contribute? Here\'s how to set up pybright for local development.

1.  Fork the repo on GitHub Enterprise -
    <https://github.com/plavjanik/pybright>.

2.  Clone your fork locally (creates `pybright` directory):

        $ git clone https://github-isl-01.ca.com/your_name_here/pybright.git

3.  Install your local copy into a virtualenv. Assuming you have
    virtualenvwrapper installed, this is how you set up your fork for
    local development:

        $ cd pybright/
        $ pipenv install -e .[dev]

4.  Create a branch for local development:

        $ git checkout -b name-of-your-bugfix-or-feature

    Now you can make your changes locally.

5.  When you're done making changes, check that your changes pass pep8
    and the tests, including testing other Python versions with tox:

        $ pipenv run pytest

6.  Test on other Python releases:

        $ pip3 install tox tox-pyenv pyenv
        $ pyenv install -s 3.5.5 
        $ pyenv install -s 3.6.6
        $ pyenv local 
        $ tox

7.  Commit your changes and push your branch to GitHub:

        $ git add .
        $ git commit -m "Your detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature

8.  Submit a pull request through the GitHub Enterprise website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2.  If the pull request adds functionality, the docs should be updated.
    Put your new functionality into a function with a docstring, and add
    the feature to the list in README.rst.
3.  The pull request should work for Python 3.5 and 3.6. Use tox and
    make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests:

    $ pipenv run pytest tests/path/to/test_file.py

Core Development Team
---------------------

Members of core development team
(<https://github-isl-01.ca.com/orgs/MFaaS/teams/hard-boiled>) are
allowed to create branches in the repository.

1.  Clone the repository locally (creates `pybright` directory):

        $ git clone https://github.com/plavjanik/pybright.git

2.  Other instructions are same above.

Releasing New Version
---------------------

This section is for core development team.

1.  Test and commit all changes without push.
2.  
3.  Use bumpversion to update version numbers:

        pipenv run bumpversion patch

4.  Commit and push the change.

        git push

5. Deploy to PyPI:

        pipenv run python3 setup.py sdist upload

    *Note:* You need to define ``pypi`` repository in ``~./.pypirc`` with your account
