from enum import Enum


class TilesetName(Enum):
    FallingPlatform = "FallingPlatform"
    Platform = "Platform"
    SandMudIce = 'SandMudIce'
    Terrain = 'Terrain'


class DynamicTileStatus(Enum):
    On = "On"
    Off = "Off"
