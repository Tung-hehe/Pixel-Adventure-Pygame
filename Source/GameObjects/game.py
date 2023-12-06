import random
import sys

from pathlib import Path

import numpy as np
import pygame

from .map import Map
from Source.Utils import GameData

from Source.enums import (
    CharacterName,
    TilesetName,
    BackgroundName
)


class Game:

    def __init__(self) -> None:
        self.rootPath = Path(__file__).absolute().parents[2]

        map = np.loadtxt(self.rootPath/"Data/Maps/Map_01/Terrain.csv", delimiter=",", dtype=int)
        tileSize = (16, 16)
        screenWidth = map.shape[1] * tileSize[0]
        screenHeight = map.shape[0] * tileSize[1]

        pygame.init()
        self.screen = pygame.display.set_mode((screenWidth,screenHeight))
        self.data = GameData(self.rootPath)

        # characterName = random.choice(list(CharacterName))
        characterName = CharacterName.PinkMan
        playerData = self.data.characters[characterName]
        backgroundName = random.choice(list(BackgroundName))
        backgroundData = self.data.backgrounds[backgroundName]

        self.map = Map(
            map=map, playerData=playerData,
            tilesetData=self.data.tilesets[TilesetName.Terrain],
            backgroundData=backgroundData
        )
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.map.update(self.screen)

            pygame.display.update()
            self.clock.tick(60)
