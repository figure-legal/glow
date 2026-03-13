import json
import os.path
from sys import exit, argv

class glow:
    def init(self):
        version = "beta 1.0"
        name = "glow"
        commands = json.load("config.json")