# YouTube Tutorials

Create a personalized learning plan based on YouTube tutorials.

More often than not, I have always felt overwhelmed by endless YouTube tutorials. You find a great playlist, but then struggle to fit the videos into your schedule.  YouTube Tutorials is here to help!  This web app empowers you to create a personalized learning plan based on your favorite YouTube playlists.

## Learn at Your Pace: Build a Personalized Learning Plan from YouTube

**Imagine this:** you discover a fantastic YouTube playlist packed with valuable tutorials. With YouTube Tutorials, you can simply:

- Connect your YouTube playlist or use a pre-existing one.
- Set your learning preferences: Choose your available study times and desired pace.
- Generate a personalized learning plan: The app creates a structured schedule based on your playlist and preferences.
- Integrate with your calendar: Seamlessly export your plan to Google Calendar or Outlook Calendar, ensuring your learning stays organized.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Contributing](#contributing)
- [Benefits](#benefits)
- [License](#license)

## Introduction

YouTube_Tutorials is a Flask web app designed to help you create a personalized learning plan based on YouTube playlists. 

It helps you to schedule your learning sessions using a self-curated or pre-exisiting playlist to generate calendar files for integration with Google Calendar or Outlook Calendar,

It makes it easy to schedule your learning sessions.

## Features

- **Playlist Integration:** Connect your YouTube playlist to create a tailored playlist to suit your learning plan.
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

## Benefits:

- **Effortless Playlist Integration:** No need to manually organize videos. Simply provide the playlist URL and let the app do the work.
- **Customizable Scheduling:** Craft a learning plan that fits your busy life.
- **Calendar Integration:** Stay on track by integrating your plan with your existing calendar tools.
- **Free and Accessible:** Available online and easy to use.

Ready to take control of your learning? Head over to YouTube Tutorials App and start building your personalized learning plan today!

**Looking for more?**  The project is open-source and welcomes contributions! If you're a developer, you can find the code on GitHub and help make YouTube Tutorials even better.

**Let's make learning on YouTube a breeze!**


## Contributing

If you'd like to contribute to this project, Please submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


