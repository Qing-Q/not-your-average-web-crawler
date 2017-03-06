<p align="center">
    <img src="https://i.imgur.com/ONCi3C2.png" width="300" height="300" alt="NYAWC">
    <br/>
    <a href="https://travis-ci.org/tijme/not-your-average-web-crawler">
        <img src="https://travis-ci.org/tijme/not-your-average-web-crawler.svg?branch=master" alt="Build Status">
    </a>
    <a href="LICENSE.md">
        <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
    </a>
</p>

## Not Your Average Web Crawler
A very useful web crawler for vulnerability scanning. Not Your Average Web Crawler (N.Y.A.W.C) is a Python application that enables you to crawl web applications for requests instead of URLs. It crawls every GET and POST request on the specified domain and keeps track of the request and response data. It's main purpose is to be used in web application vulnerability scanners like [Angular CSTI scanner](https://github.com/tijme/angular-csti-scanner).

**Crawls:**

- **Links:** URLs in HTML attributes, JSON, etc.
- **Forms:** GET & POST forms and their request data.

**Current limitations:**
- Only works on Python 3.6 or higher.
- Multiprocessing is not yet working.
- Maximum recursion depth exception when crawling too much resources.

**Future development:**

- Fix current limitations.
- Performance improvements.
- Support XHR crawling.
- Support XML & Open XML crawling.
- Support custom cookies.
- Support custom user agents.
- Support rate limiting.

## Installation
First make sure you're on [Python 3.6](https://www.python.org/) or higher. Then run the command below to install the dependencies.

`pip install nyawc`

## Usage

ToDo: explain how to use this module.

## Testing

The testing can and will automatically be done by [Travis CI](https://travis-ci.com/) on every push to the master branch. If you want to manually run the unit tests, use the command below.

`python -m unittest discover -s tests`

## Issues

Issues or new features can be reported via the GitHub issue tracker. Please make sure your issue or feature has not yet been reported by anyone else before submitting a new one.

## License

Not Your Average Web Crawler (N.Y.A.W.C) is open-sourced software licensed under the [MIT license](LICENSE.md).
