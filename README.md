# YouTube Video Downloader

A Windows desktop GUI (built with `customtkinter`) that downloads YouTube videos at a chosen resolution, with thumbnail preview, live progress bar, download speed, file size, and ETA. Downloading is handled by `yt-dlp` on a background thread to keep the UI responsive.

> **Legal / ToS notice:** Downloading videos from YouTube may violate YouTube's Terms of Service and/or local copyright law depending on the content and your jurisdiction. Use this tool only with content you have the right to download. The author of this tool is not responsible for misuse.

## Project Status

Small personal/portfolio desktop app. The download flow works on Windows with a locally installed `ffmpeg`. Not actively maintained.

## Key Features

- Modern `customtkinter` UI with desktop theme integration
- Resolution selection fetched for the provided YouTube URL
- Thumbnail preview before downloading
- Choose a custom save location via file dialog
- Live download progress bar with speed, percentage, and ETA
- Background-thread download so the UI stays responsive
- Opens the destination folder on completion, then resets for the next download
- Status/error messages for bad URLs or network problems

## Technology Stack

- **Language**: Python 3
- **GUI**: `customtkinter`, `tkinter`
- **Download**: `yt-dlp` (with `ffmpeg` for merging/converting)
- **Image**: `Pillow`, `requests` (thumbnail fetch)

## Repository Structure

```
.
├── main.py             # Single-file application (GUI + download logic)
├── requirements.txt    # Python dependencies
├── LICENSE
└── README.md
```

## Prerequisites

- Python 3.10+
- `ffmpeg` installed and on `PATH`, **or** set the `ffmpeg_location` path in `main.py` to your `ffmpeg.exe` location. The committed copy of `main.py` hardcodes a Windows-specific `ffmpeg.exe` path under the author's user profile; update it to your own install.

  > **Platform note:** As-is, `main.py` uses a Windows-only `ffmpeg.exe` path and `os.startfile` to open the output folder, so it runs on Windows out of the box. On macOS/Linux, replace the `ffmpeg_location` and `os.startfile` calls.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/dilrukshax/YouTube-Video-Downloader
   cd YouTube-Video-Downloader
   ```

2. Create and activate a virtual environment, then install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Install `ffmpeg` if you don't already have it. On Windows, use Winget:

   ```bash
   winget install Gyan.FFmpeg
   ```

   Otherwise download it from https://ffmpeg.org and add `ffmpeg.exe` to your `PATH` (or update `ffmpeg_location` in `main.py`).

4. Run the application:

   ```bash
   python main.py
   ```

## Configuration

There is no separate configuration file. The `ffmpeg_location` is set inline in `main.py`; update it to match your local `ffmpeg.exe` if it is not on your `PATH`.

## Usage

1. Paste a YouTube video URL into the entry box.
2. Click "Fetch Resolutions" to populate the resolution dropdown.
3. Choose a resolution.
4. Browse for a save location.
5. Click "Download" and watch the progress bar. The destination folder opens when the download completes.

## Testing

There is no automated test suite. Tests were not executed.

## Deployment

This is a desktop application; "deployment" means installing the Python dependencies and `ffmpeg`, then running `python main.py`.

## Limitations

- The committed `ffmpeg_location` hardcodes a Windows user-specific path; update it for your environment.
- Windows-specific calls (`os.startfile`) mean macOS/Linux need small code changes.
- No automated tests.

## Contributing

This is a personal project. If you'd like to suggest improvements, please open an issue first to discuss the change.

## License

Licensed under the [MIT License](LICENSE). Note that this license covers only the author's code; downloading YouTube content may be governed by YouTube's Terms of Service and copyright law.

## Author

Dilan Dilruksha  
Software Engineer | Backend & Full-Stack Development  
Portfolio: https://dilandilruksha.dev  
LinkedIn: https://www.linkedin.com/in/dilan-dilruksha  
GitHub: https://github.com/dilrukshax
