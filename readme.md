<p align="center">

  <h3 align="center">Fake News Classifier</h3>

  <p align="center">
    project_description
    </br>
	A simple python app to classify fake vs real news
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
	<li><a href="#docker">Docker</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<p>
    This is a simple pyhton app that can predict fake news and real news. This project uses a simple Logistic Regression algorithm to classify real news from fake news. The algorithm is trained on the kaggle "Fake News" competition dataset. <b>Do note that this dataset is old and outdated and this wont be reliable for current news articles.</b> The application is build with python using fast-api.

    The application has a web GUI as well as an API to which the news article can be provided and the output will be returned. The application is capable of automatically cleaning the text from special characters and stopwords using the NLTK toolkit. The user need not preprocess the text. The vectorization of the text is performed by the count vectorizer present in the sklearn library.

    The app can be deployed to the Heroku platform or can be made into a docker container. The associated files are present in the repo. Do note that the app exceeds the memory limit set by Heroku for free-tier during startup.

</p>
### Built With

- [Pyhton](https://www.python.org/)
- [Fast-API](https://fastapi.tiangolo.com/)
- [NLTK](https://www.nltk.org/)
- [sklearn](https://scikit-learn.org/stable/)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Make sure that python is install in your system. If it is not installed, head over to [python](https://www.python.org/downloads/) and download the appropriate version for your OS and set it up.

### Installation

1. Clone the repo
   ```sh
   https://github.com/pauljoe775/fake-news-prediction.git
   ```
2. Install the required packages
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application. It will take couple of minutes to fully load.
   ```sh
   uvicorn app:app --host 0.0.0.0 --port 5000
   ```
4. Open your browser and head over to the following link:
   http://0.0.0.0:5000
   You should now be able to see a webpage.

<!-- USAGE EXAMPLES -->

## Usage

- Using the webpage:

  1.  Fill in the input box in the webpage with the news you would like to verify

      ![alt text](https://raw.githubusercontent.com/pauljoe775/fake-news-prediction/main/screenshots/image1.jpg)

  2.  Once you click the submit button, you will recieve an alert showing whether the news is fake or not.

      ![alt text](https://raw.githubusercontent.com/pauljoe775/fake-news-prediction/main/screenshots/image2.jpg)

- Using the API:

  - The app has an endpoint at `/predict` which accepts a JSON request body in the following format:

  ```sh
  {
  	"news_text":"your news text"
  }
  ```

  - The api returns a response in the following format:

  ```sh
  {
  	"prediction":"1"
  }
  ```

  The prediction value can be 1 or 0 of type int. 1 implying it is fake.

  ![alt text](https://raw.githubusercontent.com/pauljoe775/fake-news-prediction/main/screenshots/image3.jpg)

## Docker

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [Krish Naik](https://www.youtube.com/watch?v=MO5n5JaRotc)
- [HTML & CSS used in this project](https://codepen.io/krisantuswanandi/pen/KxrgeZ)
