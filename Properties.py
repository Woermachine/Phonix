# Default property values
DEFAULT_SCROLL_SPEED = 1.0
DEFAULT_THRESHOLD = 1.0
DEFAULT_HEADPHONES_ON = False
DEFAULT_EA_ON = True
DEFAULT_SHOTGUN_ON = True

scrollSpeed = DEFAULT_SCROLL_SPEED
threshold = DEFAULT_THRESHOLD
headphonesOn = DEFAULT_HEADPHONES_ON
EAOn = DEFAULT_EA_ON # Variable may not be necessary - Woermachine
shotgunOn = DEFAULT_SHOTGUN_ON  # Variable may not be necessary - Woermachine

class Properties:
    def __init__(self, scrollspeed, volume, threshold, headphones, ea):
        self.s = scrollspeed
        self.v = volume
        self.t = threshold
        self.h = headphones
        self.e = ea


# TODO: getters and setters for each property