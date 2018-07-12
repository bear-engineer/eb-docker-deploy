# EB Docker Deploy

## Requirements

- python(3.6)
- pipenv
- Django(2.x)

### Secrets

#### '.secrets.base.json'

```json
{
    "SECRET_KEY":"<Django Secret key">
}

```

## Running

```zsh
# Move project's dirctory
pipenv install
pipenv shell
cd app
export DJANGO_SETTINGS_MODULE=config.settings.local
```