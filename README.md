# Custom Registration Fields for NELP

This is the registraion form extension app for NELP Open edX instance and is inspired and made around [custom-form-app](https://github.com/open-craft/custom-form-app).

## Development

This incorporates a test-setting file, this basically wraps around a Django app to generate migrations and translations.
And if needed in future to run tests.

For generating migrations you just need to make changes to the `model` and run:

```
python manage.py makemigrations
```

#### For generating translation messages

```
make extract_translations
```

#### For compiling translation messages

```
make compile_translations
```

## Installation

Clone this directory in your `DEVSTACK_ROOT/src` directory. You need to get to the lms-shell by `make dev.shell.lms`.
The `src` directory is generally mounted in `/edx/src`, so `cd /edx/src/custom-registration-fields`.

Activate the edxapp venv and install this package by `pip install -e .`

For hacking around custom registration form you need to add few varibles to `/edx/etc/lms.yml` file in your devstack(lms container).

Add below lines in `/edx/etc/lms.yml`

```
"ADDL_INSTALLED_APPS":
- "custom_reg_form"

"REGISTRATION_EXTENSION_FORM": "custom_reg_form.forms.ExtraInfoForm"
```

Now you need to do a `make lms-restart`

## Packaging Check

Just to make sure all the files that are introduced should be properly packed we need, after the changes that has been done
instead of running a ~~`pip install -e .`~~ run `pip install .` and check in ` {your virtual environment root}/lib/python3.5/site-packages/custom_reg_form/`
this should have all the files eg. Migrations, admin, form etc.
