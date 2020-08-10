# FastAPI RFC3339 Problem

OpenAPI strings with format `date-time` must be RFC3339 compliant.

https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md#data-types

FastAPI specifies `date-time` as format but it is only ISO8601 not RFC3339

```
poetry install
poetry run pytest tests
```