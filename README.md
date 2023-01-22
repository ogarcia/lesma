# The project has moved

lesma code is now hosted in [GitLab][lesma] and rewritten in [Rust][rust]

- New Git: https://gitlab.com/ogarcia/lesma
- New bugtracker: https://gitlab.com/ogarcia/lesma/-/issues
- New tag list: https://gitlab.com/ogarcia/lesma/-/tags

[lesma]: https://gitlab.com/ogarcia/lesma
[rust]: https://www.rust-lang.org

# lesma

(c) 2017-2023 Óscar García Amor

Redistribution, modifications and pull requests are welcomed under the terms
of GPLv3 license.

lesma is a simple paste app, friendly with browser and command line, with
files as storage backend. You can see in action in https://lesma.eu.

## Install

To install lesma follow this steps.

### From source

```sh
git clone https://github.com/ogarcia/lesma.git
virtualenv3 ./lesma-venv
source ./lesma-venv/bin/activate
cd lesma
python setup.py install
```

### From PyPI

```sh
virtualenv3 ./lesma-venv
source ./lesma-venv/bin/activate
pip install lesma
```

## Run

In your virtualenv run `lesma server`.

```sh
source ./lesma-venv/bin/activate
lesma server
```

Or without activate virtualenv.

```
./lesma-venv/bin/lesma server
```

Run `lesma` without parameters to see help.
