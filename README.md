# python-starter

A `uv` workspace based Python starter project: a root project with accompanying libraries.

Includes ruff, pyright (strict), pytest with coverage, pre-commit, GitHub Actions CI, and Dependabot.

```text
├── pyproject.toml    # app, workspace members, dev dependencies, tool config
├── src/app/
├── tests/
└── packages/
    └── lib/
        ├── pyproject.toml
        ├── src/lib/
        └── tests/
```

## Start a project

Click **Use this template** on GitHub and clone the new repo, then:

```sh
uv sync --all-packages
uv run pre-commit install
```

Commit the generated `uv.lock`. CI enforces it from then on. This template deliberately doesn't commit one, so each new project resolves the latest versions.

## Commands

```sh
uv run ruff check --fix
uv run ruff format
uv run pyright
uv run pytest
```

## Add a library

```sh
uv init --lib packages/foo
uv add foo                  # optional: make app depend on foo
uv sync --all-packages
```

## Rename `app`

```sh
git mv src/app src/foo
git mv tests/test_app.py tests/test_foo.py
perl -pi -e 's/\bapp\b/foo/g' pyproject.toml tests/test_foo.py
uv sync --all-packages
```

## Rename `lib`

```sh
git mv packages/lib packages/foo
git mv packages/foo/src/lib packages/foo/src/foo
git mv packages/foo/tests/test_lib.py packages/foo/tests/test_foo.py
perl -pi -e 's/\blib\b/foo/g' pyproject.toml packages/foo/pyproject.toml packages/foo/tests/test_foo.py src/*/__init__.py
uv sync --all-packages
```

Rename before publishing to PyPI: package names there must be unique.
