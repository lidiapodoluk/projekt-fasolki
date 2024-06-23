from zmienne import *
import pygame
import sys



class Scene:
    def __init__(self, screen):
        self.screen = screen

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class SceneManager:
    def __init__(self, screen):
        self.screen = screen
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def set_scene(self, name):
        self.current_scene = self.scenes.get(name)

    def handle_events(self, events):
        next_scene = self.current_scene.handle_events(events)
        if next_scene:
            self.set_scene(next_scene)

    def update(self):
        if self.current_scene:
            self.current_scene.update()

    def draw(self):
        if self.current_scene:
            self.current_scene.draw()
