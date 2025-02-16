# Moments

A photo sharing social networking app built with Python and Flask. The example application for the book *[Python Web Development with Flask (2nd edition)](https://helloflask.com/en/book/4)* (《[Flask Web 开发实战（第 2 版）](https://helloflask.com/book/4)》).

Demo: http://moments.helloflask.com

![Screenshot](demo.png)

## Installation

Clone the repo:

```
$ git clone https://github.com/greyli/moments
$ cd moments
```

Install dependencies with [PDM](https://pdm.fming.dev):

```
$ pdm install
```

> [!TIP]
> If you don't have PDM installed, you can create a virtual environment with `venv` and install dependencies with `pip install -r requirements.txt`.

To initialize the app, run the `flask init-app` command:

```
$ pdm run flask init-app
```

If you just want to try it out, generate fake data with `flask lorem` command then run the app:

```
$ pdm run flask lorem
```

It will create a test account:

* email: `admin@helloflask.com`
* password: `moments`

Now you can run the app:

```
$ pdm run flask run
* Running on http://127.0.0.1:5000/
```
## Setting up Microsoft Azure
This step is very crucial as we have used Azure's Computer Vision API for this Homework.
```
Step 1: Go to Microsoft Azure website (https://azure.microsoft.com/en-us/) and login.
Step 2: In the search bar above, type computer vision and click on the computer vision API.
Step 3: Create a computer vision service and get the Endpoint and Key.
Step 4: Place those credentials in an .env file and gitignore it to hide the credentials.
```
The credentials will be called in the folder ml_utils.py and will be used for the homework.

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
