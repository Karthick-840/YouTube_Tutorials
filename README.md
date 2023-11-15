# YouTube Tutorials

Create a personalized learning plan based on YouTube tutorials.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

YouTube_Tutorials is a Flask web app designed to help you create a personalized learning plan based on YouTube playlists. 

It helps you to schedule your learning sessions using a self-curated or pre-exisiting playlist to generate calendar files for integration with Google Calendar or Outlook Calendar,

It makes it easy to schedule your learning sessions.

## Features

- **Playlist Integration:** Connect your YouTube playlist to create a tailored learning plan.
- **Custom Scheduling:** Plan your learning sessions based on your availability and preferences.
- **Calendar Export:** Generate calendar files compatible with Google Calendar or Outlook Calendar.

## Usage

1. **Create Playlist:** in youtube or use a pre-existing playlist.
2. **Visit the App Online:** at [YouTube Tutorials App](https://your-youtube-tutorials-app-name.herokuapp.com/)  and input the playlist URL into the search bar.
3. **Explore Scheduling options:** by provide general information about when you plan to study.
4. **Follow On-Screen Instructions:** to generate a learning plan.
5. **Integrate with Google/Outlook:** by following the prompts to connect to Google Calendar or Outlook Calendar via API (option available to download the .ics file) .


## Installation

Follow these steps to set up and run the YouTube_Tutorials app locally:

1. **Clone the Repository:**
    ```bash
    $ git clone https://github.com/yourusername/Your_Tutorials.git
    $ cd Your_Tutorials

    import youtube_tutorial

2. **Set Up a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask App:**

    ```bash
    export FLASK_APP=app
    export FLASK_ENV=development
    flask run
    ```

    Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser to access the app locally.

## Contributing

If you'd like to contribute to this project, Please submit a pull request.

## License

This project is licensed under the [Your License] License - see the [LICENSE.md](LICENSE.md) file for details.

