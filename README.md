# python-star-wars-api-client

<div align="center">

[![Build status](https://github.com/marcslopz/python-star-wars-api-client/workflows/build/badge.svg?branch=master&event=push)](https://github.com/marcslopz/python-star-wars-api-client/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/python-star-wars-api-client.svg)](https://pypi.org/project/python-star-wars-api-client/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/marcslopz/python-star-wars-api-client/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/marcslopz/python-star-wars-api-client/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/marcslopz/python-star-wars-api-client/releases)
[![License](https://img.shields.io/github/license/marcslopz/python-star-wars-api-client)](https://github.com/marcslopz/python-star-wars-api-client/blob/master/LICENSE)

Star Wars API Client

</div>


### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions](https://semver.org/) standard.
- Make a commit to `GitHub`.
- Create a `GitHub release`.
- And... publish 🙂 `poetry publish --build`

## 🚀 Features

### Development features

- Supports for `Python 3.9` and higher.
- [`Poetry`](https://python-poetry.org/) as the dependencies manager. See configuration in [`pyproject.toml`](https://github.com/marcslopz/python-star-wars-api-client/blob/master/pyproject.toml) and [`setup.cfg`](https://github.com/marcslopz/python-star-wars-api-client/blob/master/setup.cfg).
- Automatic codestyle with [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort) and [`pyupgrade`](https://github.com/asottile/pyupgrade).
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with code-formatting.
- Type checks with [`mypy`](https://mypy.readthedocs.io); docstring checks with [`darglint`](https://github.com/terrencepreilly/darglint); security checks with [`safety`](https://github.com/pyupio/safety) and [`bandit`](https://github.com/PyCQA/bandit)
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).
- Ready-to-use [`.editorconfig`](https://github.com/marcslopz/python-star-wars-api-client/blob/master/.editorconfig), [`.dockerignore`](https://github.com/marcslopz/python-star-wars-api-client/blob/master/.dockerignore), and [`.gitignore`](https://github.com/marcslopz/python-star-wars-api-client/blob/master/.gitignore). You don't have to worry about those things.

### Deployment features

- `GitHub` integration: issue and pr templates.
- `Github Actions` with predefined [build workflow](https://github.com/marcslopz/python-star-wars-api-client/blob/master/.github/workflows/build.yml) as the default CI/CD.
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc with [`Makefile`](https://github.com/marcslopz/python-star-wars-api-client/blob/master/Makefile#L89). More details in [makefile-usage](#makefile-usage).
- [Dockerfile](https://github.com/marcslopz/python-star-wars-api-client/blob/master/docker/Dockerfile) for your package.
- Always up-to-date dependencies with [`@dependabot`](https://dependabot.com/). You will only [enable it](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates).
- Automatic drafts of new releases with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). You may see the list of labels in [`release-drafter.yml`](https://github.com/marcslopz/python-star-wars-api-client/blob/master/.github/release-drafter.yml). Works perfectly with [Semantic Versions](https://semver.org/) specification.

### Open source community features

- Ready-to-use [Pull Requests templates](https://github.com/marcslopz/python-star-wars-api-client/blob/master/.github/PULL_REQUEST_TEMPLATE.md) and several [Issue templates](https://github.com/marcslopz/python-star-wars-api-client/tree/master/.github/ISSUE_TEMPLATE).
- Files such as: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically.
- [`Stale bot`](https://github.com/apps/stale) that closes abandoned issues after a period of inactivity. (You will only [need to setup free plan](https://github.com/marketplace/stale)). Configuration is [here](https://github.com/marcslopz/python-star-wars-api-client/blob/master/.github/.stale.yml).
- [Semantic Versions](https://semver.org/) specification with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter).


### Makefile usage

[`Makefile`](https://github.com/marcslopz/python-star-wars-api-client/blob/master/Makefile) contains a lot of functions for faster development.

#### Local development with Poetry
> Note: `Poetry` and `pre-commit` packages will be installed using your `python` current binary. If you want to
avoid modifying your local system, use Docker development in the next section.
<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry run:

```bash
make poetry-download
```

To uninstall

```bash
make poetry-remove
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort` and `black`.

```bash
make codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black` and `darglint` library

<details>
<summary>4. Code security</summary>
<p>

```bash
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

</p>
</details>

<details>
<summary>5. Type checks</summary>
<p>

Run `mypy` static type checker

```bash
make mypy
```

</p>
</details>

<details>
<summary>6. Tests</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>7. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint
```

the same as:

```bash
make test && make check-codestyle && make mypy && make check-safety
```

</p>
</details>

<details>
<summary>8. Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Or to remove pycache, build and docker image run:

```bash
make clean-all
```

</p>
</details>

#### Local development using Docker images

<details>
<summary>1. Build</summary>
<p>

Build dev image (with dev dependencies)
```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```
</p>
</details>

<details>
<summary>2. Run the application in a container</summary>
<p>

```bash
make docker-run
```

</p>
</details>

<details>
<summary>3. Run shell (bash) into the container</summary>

> Note: You will be able to run all make targets inside the container from the previous section

<p>

```bash
make docker-run-bash
```
</p>
</details>

<details>
<summary>4. Run tests</summary>
<p>

```bash
make docker-run-test
```
</p>
</details>

<details>
<summary>5. Run all linter tools</summary>
<p>

```bash
make docker-run-lint
```
</p>
</details>

<details>
<summary>6. Remove docker images </summary>
<p>
Remove docker image with

```bash
make docker-remove
```

More information [about docker](https://github.com/marcslopz/python-star-wars-api-client/tree/master/docker).

</p>
</details>

<details>
<summary>7. Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Or to remove pycache, build and docker image run:

```bash
make clean-all
```

</p>
</details>

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/marcslopz/python-star-wars-api-client/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/marcslopz/python-star-wars-api-client/blob/master/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

## 🛡 License

[![License](https://img.shields.io/github/license/marcslopz/python-star-wars-api-client)](https://github.com/marcslopz/python-star-wars-api-client/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/marcslopz/python-star-wars-api-client/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{python-star-wars-api-client,
  author = {marcslopz},
  title = {Star Wars API Client},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/marcslopz/python-star-wars-api-client}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)
