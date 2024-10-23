import tkinter
from tkinter import filedialog
from media_detection import snap_track

tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
video_extensions = "*.mp4 *.mov *.avi *.wmv *.avchd *.webm *.flv *.mkv"
image_extensions = "*.jpg *.jpeg *.png"
all_extensions = video_extensions + " " + image_extensions
file_path = filedialog.askopenfilename(initialdir="./media", title="Select A File", filetypes=(("all files", all_extensions), ("video files", video_extensions), ("image files", image_extensions)))
if file_path == "":
    print("No file chosen")
else:
    snap_track(file_path)