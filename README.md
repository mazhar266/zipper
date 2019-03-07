## Zipper

This is an OpenSource REST API enabled file zipping MicroService.

### Requirements

- Python 3.6 or later
- Python Flask
- Linux server with `zip` and `wget` installed

### How to run

- Install Python 3 and pip 3
- Install dependencies like `python3 -m pip install -r requirements`
- Run `flask run`
- or run `FLASK_DEBUG=1 flask run` (this will reload on changes)
- or run `./run.sh`

### TODO

- Implement expiring token based auth
- Implement datastores

### Contribution Guideline

- Fork and submit a pull request
- Maintain PEP8 convension
- Check your code using pylint

## How to use

To get the zip file of `file_url1.png`, `file_url2.png` and `file_url3.png`, send a request like this:
`BASE_URL/api/v1/zip?file=file_url1.png&file=file_url2.png&file=file_url3.png`.
Example on my localhost:
`http://localhost:5000/api/v1/zip?file=file_url1.png&file=file_url2.png&file=file_url3.png`

### Credits

- Mazhar Ahmed - [github.com/mazhar266](https://github.com/mazhar266)
