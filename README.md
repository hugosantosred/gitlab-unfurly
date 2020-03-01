# GitLab Unfurly (Flask Edition)

Flask Slack bot for unfurling GitLab URLs.

[![Python: 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://python.org) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) 
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/kiwicom/gitlab-unfurly/blob/master/LICENSE)

## Example

![GitLab Unfurly example](/docs/gitlab-unfurly.png)

## Usage

Clone to any server

Create a .env file in the same directory and provide these environment variables
(Copy env.example to .env):

- `GITLAB_URL`
- `GITLAB_TOKEN`
- `SLACK_TOKEN`
- `SLACK_CLIENT_ID`
- `SLACK_CLIENT_SECRET`

Run with docker-compose up -d --build

## Contributing

Bug reports and fixes are always welcome!

Tests are run with [pytest](https://pytest.org). Install into virtual environment 
`requirements.txt` and `test-requirements.txt` and run in shell command `pytest`

Code is formatted by [Black](https://github.com/ambv/black).

## License

[MIT](https://github.com/kiwicom/gitlab-unfurly/blob/master/LICENSE)

## FAQ

1. **How to make unfurly ignore my urls (= not create previews)?**  
Append `?no_unfurl` to the url.

2. **Is there a way to disable unfurly for the whole post?**  
Unfortunately no. Unfurly receives links from slack 1-by-1. Therefore it has no knowledge about
links being part of the same post.
