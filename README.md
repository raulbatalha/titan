# Titan

[![PIP Version][pypi-image]][pypi-url] [![Downloads Stats][pypi-downloads]][pypi-url]

### This is a project for course conclusion of the course IARTES - AI Specialization for Software Test Engineering

<p align="center" width="100%">
<img width="20%" src='https://user-images.githubusercontent.com/12941167/232917960-4861fb8a-ed55-436c-82ab-61cd3fd00c0b.png' /img>
</p>

### Table of Contents

- [TITAN-Automatic Test Case Generator](#automatic-test-case-generator)
  - [Table of Contents](#table-of-contents)
  - [About Project](#about-project)
  - [Installation](#installation)
  - [Development setup](#development-setup)
  - [Release History](#release-history)
  - [Contributing](#contributing)
  - [License](#license)
  - [Meta](#meta)

## About Project

- The idea is create automation test case generator using machine learning with artificial intelligence;
- The project was create using OpenCV, OCR Tesseract, and Pytesseract with Python for read and interpretation of screen;
- For screenshot and reconing identifiers of screen of mobile device must be using ADB Command and for trainnig of the database was used Neuro-linguisticprogramming (NLP);

## Installation

- ##### Linux:

1. Open up your terminal by pressing **< Ctrl + Alt + T >**.
2. Update your local system's repository list by entering the following command:

```sh
    sudo apt update
```

3. Download the latest version of Python:

```sh
    sudo apt install python3
```

- ##### Windows:

1. Install Python 3.x.x _(current version)_

```sh
    https://www.python.org/downloads/
```

2. Update pip to ensure latest version:

```sh
    pip install -U pip
```

## Development setup

How to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

1. Git global Setup

```sh
    git config --global user.name "Your Name"
    git config --global user.email "your_nickname@eldorado.org.br"
```

2. Clone the project

```sh
    HTTP: git clone https://github.com/raulbatalha/titan.git
========================================================================================================
    SSH: git clone git@github.com:raulbatalha/titan.git
```

3. Open project folder where the was cloned repository using [VSCode IDE](https://code.visualstudio.com/);

```sh
    File > Open Folder (Ctrl+K Ctrl+O)
```

4. Open terminal
   <br>

   - Use the <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>`</kbd> keyboard shortcut with the backtick character
     </br>

5. Install all project dependencies in project folder and run be done as follow:

- Open the terminal in the root directory of your project.
  - After command press Enter.

```sh
    env/bin/activate
```

- This will activate the virtual environment, and you'll see the name of the virtual environment appear in the terminal prompt, indicating that the virtual environment is active. Now you can install the necessary Python libraries for your project using the pip package manager.

```sh
    pip install -r requirements.txt
```

- To install OCR Tesseract, type the command after press Enter:

```sh
    Ubuntu / Debian: sudo apt-get install tesseract-ocr
```

- After installing the necessary libraries, you can run your project by typing the command python

```sh

    run_titan.py,
```

> When you're done working on your project, you can deactivate the virtual environment by typing the command deactivate in the terminal and pressing Enter.

6. Go to **results** folder to get the (TestCase.xls) file.

## Release History

- 0.1.0

  - The first proper release
  - CHANGE: Update docs (module code)

- 0.0.1
  - Work in progress

## Contributing

1. Make a project Fork (`https://github.com/raulbatalha/titan/forks`)
2. Create a branch for your feature (`git checkout -b developer/newbranch`)
3. Insert your changes (`git add .`)
4. Commit your changes (`git commit -am 'Add comment'`)
5. Push to the branch (`git push origin developer/newbranch`)
6. Create a new Pull Request

## License

Distributed under the [MIT license](https://choosealicense.com/licenses/mit/) . See LICENSE for more information.

## Meta

André Santos - santos.andre7@outlook.com;
Kelen Lima - kelenrlima@gmail.com;
Raul Batalha – raulbatalh@gmail.com;

<!-- Markdown link & img dfn's -->

[pypi-image]: https://img.shields.io/pypi/v/https://opencv.org.svg
[pypi-url]: https://pypi.org/tesseract-ocr/tesseract
[pypi-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
