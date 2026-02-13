import pygame
import os

class MusicManager:
    def __init__(self):
        self.currentMusic = {}
        self.musicCollection = {
            "base_loop": {
                "duration": 1,
                "loop": True,
            }
        }
        self.load_musics()


    def play_music(self, id:str, settings:dict, interrupt:bool=False):
        if "player" in self.currentMusic:
            if interrupt:
                self.currentMusic["player"].stop()
            else:
                print("Skipped music", self.currentMusic["id"], "because another was already playing")
                return
        
        self.currentMusic = self.musicCollection[id]
        self.currentMusic["id"] = id
        self.currentMusic["player"].set_volume(settings["volume"]/100)
        self.currentMusic["player"].play(-1, 0, 1000)
        print("Playing music", self.currentMusic["id"])

    def updateVolume(self, settings):
        self.currentMusic["player"].set_volume(settings["volume"]/100)

    def load_musics(self):
        for musicId in self.musicCollection:
            self.musicCollection[musicId]["player"] = pygame.mixer.Sound(os.path.join('./assets/musics', musicId+'.mp3'))
