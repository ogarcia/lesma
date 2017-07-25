# lesma 

(c) 2017 Óscar García Amor

Redistribution, modifications and pull requests are welcomed under the terms
of GPLv3 license.

lesma is a simple paste app friendly with command line and browser with
files as storage backend. You can see in action in
https://paste.connectical.com.

## Install

To install lesma follow this steps.

```sh
git clone https://github.com/ogarcia/lesma.git
virtualenv3 ./lesma-venv
source ./lesma-venv/bin/activate
cd lesma
python setup.py install
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
