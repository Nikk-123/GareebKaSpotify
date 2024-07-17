from flask import Flask, request, jsonify, send_file, render_template
from pymongo import MongoClient
import os
import yt_dlp as youtube_dl

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client.music
songs_collection = db.songs

UPLOAD_FOLDER = 'uploads'  # Directory to store uploaded songs
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_song():
    if 'audio' not in request.files:
        return "No file part", 400

    file = request.files['audio']
    if file.filename == '':
        return "No selected file", 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Save metadata to MongoDB
    songs_collection.insert_one({
        'title': file.filename,
        'path': file_path
    })

    return jsonify({"message": "File uploaded successfully!"}), 201

@app.route('/stream/<filename>', methods=['GET'])
def stream_song(filename):
    song = songs_collection.find_one({'title': filename})
    if song:
        return send_file(song['path'], as_attachment=False)
    return "File not found", 404

@app.route('/search', methods=['GET'])
def search_song():
    query = request.args.get('query')
    results = []

    ydl_opts = {
        'format': 'bestaudio',
        'noplaylist': True,
        'quiet': True,
        'extract_flat': 'in_playlist',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch10:{query}", download=False)
            for entry in info['entries']:
                results.append({
                    'title': entry['title'],
                    'url': entry['url']
                })
        except Exception as e:
            print(f"Error searching for song: {e}")

    return jsonify(results)

@app.route('/play_youtube', methods=['POST'])
def play_youtube():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(UPLOAD_FOLDER, '%(title)s.%(ext)s'),
        'quiet': True,
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            filename = filename.replace('.webm', '.mp3').replace('.m4a', '.mp3')  # Ensure the correct file extension
        return send_file(filename, as_attachment=False)
    except Exception as e:
        print(f"Error playing YouTube audio: {e}")
        return jsonify({"error": "Failed to play audio"}), 500

@app.route('/songs', methods=['GET'])
def list_songs():
    songs = list(songs_collection.find({}, {'_id': 0}))
    return jsonify(songs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
