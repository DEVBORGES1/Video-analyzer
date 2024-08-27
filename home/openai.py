import moviepy.editor as mp
from django.conf import settings
from pathlib import Path
from .openai import Transcricao

class Transcricao:
    def __init__(self, path_video):
        self.path_video = path_video
        self.video = mp.VideoFileClip(path_video)

    @property
    def path_audio(self):
        return f'{settings.BASE_DIR / "audio_file" / Path(self.path_video).stem}.mp3'
    def save_tempfile(self):
        self.video.audio.write_audiofile(self.path_audio)

    def transcrever(self):
        self.save_tempfile()
