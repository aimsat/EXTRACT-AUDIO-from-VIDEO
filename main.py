from moviepy.editor import VideoFileClip

# Define the path to your video file and the output audio file
video_path = "F:/aim/Projects/video.mp4"  # Replace with the path to your video file
audio_path = "output_audio.mp3"  # Specify the desired output audio file name

# Load the video file
video = VideoFileClip(video_path)

# Extract the audio and save it
video.audio.write_audiofile(audio_path)

print("Audio has been extracted and saved as", audio_path)
