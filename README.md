# Concordia Grades

Web crawler built with Selenium, running a headless Chrome browser. It checks for your grades for a given semester at Concordia and sends you a text message once one is out.

## Getting Started

First, clone the repository and run the following:

```
cp .env-example .env
```

Then assign appropriate values to the environment variables defined in the `.env` file.

### Prerequisites

The following Python packages are required to run the program:

- [selenium](https://pypi.org/project/selenium/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [twilio](https://pypi.org/project/twilio/)
- [requests](https://pypi.org/project/requests/)
- [wget](https://pypi.org/project/wget/)

Click [here](requirements.txt) for the specific versions of the packages used for this project.

## Authors

- **Vartan Benohanian**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
