from moviepy.editor import AudioFileClip, ColorClip

audio = AudioFileClip("lyria_20260202_123522.wav")
video = ColorClip(size=(640, 480), color=(0, 0, 0), duration=audio.duration)
video = video.set_audio(audio)

video.write_videofile("lyria_jazz.mp4", fps=1)