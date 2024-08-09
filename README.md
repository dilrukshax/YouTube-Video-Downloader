
# YouTube Video Downloader

A powerful, easy-to-use YouTube Video Downloader built using `customtkinter` for a modern, sleek UI. This application allows users to download YouTube videos in various resolutions, showing live progress, download speed, file size, and estimated time of completion.

![Screenshot (4)](https://github.com/user-attachments/assets/a2d1699d-15cc-4865-9bca-a3e8f13599b6)


![Screenshot 2024-08-09 204821](https://github.com/user-attachments/assets/33dda4e3-e945-4d73-9905-a487a0e05b24)


## Features

### 1. **Modern UI with `customtkinter`**
- The application leverages `customtkinter`, which provides a modern, customizable interface that adapts to your system's theme. The dark mode and theme integration give a contemporary look and feel.

### 2. **Resolution Selection**
- Automatically fetches available resolutions for the given YouTube URL.
- Allows users to choose their desired resolution before downloading the video.

### 3. **Thumbnail Preview**
- Displays the video thumbnail to give users a visual confirmation before downloading.

### 4. **Custom Save Location**
- Users can choose where to save the downloaded video using a simple file dialog.
- The application ensures that the video is saved with a user-friendly name based on the video title.

### 5. **Live Download Progress**
- Real-time progress bar showing how much of the video has been downloaded.
- Displays download speed in MB/s, percentage of download completed, and the estimated time remaining (ETA) until completion.

### 6. **Error Handling and Status Updates**
- Provides clear, user-friendly error messages if something goes wrong (e.g., issues with the YouTube URL or network problems).
- The status label at the bottom of the application keeps users informed about the current operation.

### 7. **Post-Download Actions**
- Automatically opens the folder containing the downloaded video once the download is complete.
- The application resets itself after a download, ready for the next task.

### 8. **Multi-threaded Downloading**
- The application uses a separate thread to handle the download process, ensuring that the UI remains responsive even during long downloads.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/youtube-video-downloader.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd youtube-video-downloader
   ```

3. **Install the required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

   - Ensure `yt-dlp`, `customtkinter`, `Pillow`, and `requests` are installed.

4. **Run the application:**

   ```bash
   python main.py
   ```

## Requirements

- **Python 3.10 or higher**
- `yt-dlp`
- `customtkinter`
- `Pillow`
- `requests`

## How to Use

1. **Enter the YouTube URL**: Paste the YouTube video URL in the provided entry box.
2. **Fetch Resolutions**: Click on the "Fetch Resolutions" button to get available download options.
3. **Select Resolution**: Choose your preferred resolution from the dropdown menu.
4. **Choose Save Location**: Browse and select the folder where you want to save the downloaded video.
5. **Start Download**: Click on "Download" and watch the progress bar update in real-time.

## Contributing

Contributions are welcome! If you have ideas for improvements or spot any issues, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

