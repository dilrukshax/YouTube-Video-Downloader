import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading
import os
import yt_dlp
import time

# Initialize customtkinter
ctk.set_appearance_mode("Dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (default), "green", "dark-blue"

def fetch_resolutions():
    url = url_entry.get()
    if not url:
        status_label.configure(text="Please enter a URL.")
        return []

    ydl_opts = {
        'format': 'best'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            global video_info
            video_info = info_dict
    except Exception as e:
        status_label.configure(text=f"Error fetching resolutions: {str(e)}")
        return []

    resolutions = set()
    for fmt in formats:
        resolution = fmt.get('height')
        if resolution:
            resolutions.add(str(resolution))

    return sorted(resolutions, key=lambda x: int(x))

def update_resolutions():
    download_btn.configure(state='disabled')
    resolutions = fetch_resolutions()
    if resolutions:
        resolution_combobox.configure(values=resolutions)
        resolution_combobox.set(resolutions[0])  # Set the first resolution as default
        download_btn.configure(state='normal')
        update_thumbnail()
    else:
        resolution_combobox.configure(values=[])
        status_label.configure(text="No resolutions found or error occurred.")

def update_thumbnail():
    thumbnail_url = video_info.get('thumbnail')
    response = requests.get(thumbnail_url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    img.thumbnail((160, 90))
    img = ImageTk.PhotoImage(img)
    thumbnail_label.configure(image=img)
    thumbnail_label.image = img

def download_video():
    url = url_entry.get()
    save_path = save_path_var.get()
    selected_resolution = resolution_combobox.get()

    ydl_opts = {
        'format': f'bestvideo[height<={selected_resolution}]+bestaudio/best[height<={selected_resolution}]',
        'outtmpl': os.path.join(save_path, f"{video_info['title']}.mp4"),
        'progress_hooks': [progress_hook],
        'ffmpeg_location': 'C:/Users/dilan/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg.Essentials_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-7.0.1-essentials_build/bin/ffmpeg.exe'  # Specify ffmpeg location if not in PATH
    }

    def download_with_progress():
        try:
            start_time = time.time()
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            end_time = time.time()
            total_time = end_time - start_time
            status_label.configure(text=f"Video downloaded successfully in {total_time:.2f} seconds!")
            os.startfile(save_path)  # Open the download folder after completion
        except Exception as e:
            status_label.configure(text=f"Error downloading video: {str(e)}")
        finally:
            download_btn.configure(state='normal')  # Re-enable download button after download completion
            download_progress.set(0)  # Reset progress bar after download completion

    download_btn.configure(state='disabled')
    download_thread = threading.Thread(target=download_with_progress)
    download_thread.start()

def progress_hook(d):
    if d['status'] == 'downloading':
        total_size = d.get('total_bytes')
        downloaded_size = d.get('downloaded_bytes')
        if total_size:
            progress = downloaded_size / total_size
            download_progress.set(progress)  # Update progress bar
            
            # Calculate download speed, percentage, and remaining time
            elapsed_time = d.get('elapsed')
            download_speed = (downloaded_size / (elapsed_time + 1)) / (1024 * 1024)  # MB/s
            remaining_time = (total_size - downloaded_size) / (download_speed * (1024 * 1024)) if download_speed > 0 else 0
            
            percentage = progress * 100
            download_speed_label.configure(text=f"Speed: {download_speed:.2f} MB/s")
            download_percentage_label.configure(text=f"Percentage: {percentage:.2f}%")
            estimated_time_label.configure(text=f"ETA: {remaining_time:.2f} seconds")
            file_size_label.configure(text=f"File Size: {total_size / (1024 * 1024):.2f} MB")
    elif d['status'] == 'finished':
        download_progress.set(1.0)  # Set progress bar to full

# GUI setup using customtkinter
root = ctk.CTk()
root.title("YouTube Video Downloader")
root.geometry("800x600")

# Title
title = ctk.CTkLabel(root, text="YouTube Video Downloader", font=ctk.CTkFont(size=24))
title.pack(pady=10)

# URL Entry
url_frame = ctk.CTkFrame(root)
url_frame.pack(pady=10, fill='x')

url_label = ctk.CTkLabel(url_frame, text="Enter YouTube URL:")
url_label.pack(side='left', padx=5)

url_entry = ctk.CTkEntry(url_frame, width=400)
url_entry.pack(side='left', padx=5)

fetch_button = ctk.CTkButton(url_frame, text="Fetch Resolutions", command=update_resolutions)
fetch_button.pack(side='left', padx=5)

# Save Path
save_path_frame = ctk.CTkFrame(root)
save_path_frame.pack(pady=10, fill='x')

save_path_label = ctk.CTkLabel(save_path_frame, text="Save to:")
save_path_label.pack(side='left', padx=5)

save_path_var = ctk.StringVar()
save_path_entry = ctk.CTkEntry(save_path_frame, textvariable=save_path_var, width=400)
save_path_entry.pack(side='left', padx=5)

browse_button = ctk.CTkButton(save_path_frame, text="Browse", command=lambda: save_path_var.set(filedialog.askdirectory()))
browse_button.pack(side='left', padx=5)

# Resolution
resolution_frame = ctk.CTkFrame(root)
resolution_frame.pack(pady=10, fill='x')

resolution_label = ctk.CTkLabel(resolution_frame, text="Select Resolution:")
resolution_label.pack(side='left', padx=5)

resolution_combobox = ctk.CTkComboBox(resolution_frame)
resolution_combobox.pack(side='left', padx=5)

# Download Button
download_btn = ctk.CTkButton(root, text="Download", command=download_video)
download_btn.pack(pady=10)

# Progress
progress_frame = ctk.CTkFrame(root)
progress_frame.pack(pady=10, fill='x')

download_progress = ctk.CTkProgressBar(progress_frame)
download_progress.pack(fill='x')

# Status and Additional Information
info_frame = ctk.CTkFrame(root)
info_frame.pack(pady=10, fill='x')

thumbnail_label = ctk.CTkLabel(info_frame, text="")
thumbnail_label.pack(pady=10)

download_speed_label = ctk.CTkLabel(info_frame, text="Speed: 0.00 MB/s")
download_speed_label.pack(pady=5)

download_percentage_label = ctk.CTkLabel(info_frame, text="Percentage: 0.00%")
download_percentage_label.pack(pady=5)

estimated_time_label = ctk.CTkLabel(info_frame, text="ETA: 0.00 seconds")
estimated_time_label.pack(pady=5)

file_size_label = ctk.CTkLabel(info_frame, text="File Size: 0.00 MB")
file_size_label.pack(pady=5)

status_label = ctk.CTkLabel(root, text="")
status_label.pack(pady=10)

root.mainloop()
