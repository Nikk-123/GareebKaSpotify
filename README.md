# Gareeb ka Spotify

## Overview
Gareeb ka Spotify is a simple music streaming application that allows users to upload their music and search for songs on YouTube. It provides a user-friendly interface to stream songs without interruptions from ads.

## Features
- **Upload Music**: Users can upload their own audio files.
- **Search YouTube**: Search for songs on YouTube and play them directly.
- **Playlists**: Create and manage your own playlists.
- **Responsive Design**: Works well on various screen sizes.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Database**: MongoDB
- **YouTube Integration**: `yt-dlp` for fetching audio from YouTube.

## Installation

### Prerequisites
- Python 3.x
- Flask
- MongoDB
- yt-dlp

### Steps to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nikk-123/GareebKaSpotify.git
   cd GareebKaSpotify
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start MongoDB** (if not already running).

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and go to `http://127.0.0.1:5000/`.

## Usage
- Use the upload section to add your own music files.
- Search for your favorite songs using the search bar, and play them directly from YouTube.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for YouTube audio extraction.
- [MongoDB](https://www.mongodb.com/) for database management.

