# Default property values
DEFAULT_SCROLL_SPEED = 1.5
DEFAULT_THRESHOLD = 1.0
DEFAULT_HEADPHONES_ON = False
DEFAULT_EA_ON = True
DEFAULT_SHOTGUN_ON = True

#These can all be accessed directly after importing Properties
scrollSpeed = DEFAULT_SCROLL_SPEED
threshold = DEFAULT_THRESHOLD
headphonesOn = DEFAULT_HEADPHONES_ON
EAOn = DEFAULT_EA_ON # Variable may not be necessary - Woermachine
shotgunOn = DEFAULT_SHOTGUN_ON  # Variable may not be necessary - Woermachine

def resetToDefault():
    scrollSpeed = DEFAULT_SCROLL_SPEED
    threshold = DEFAULT_THRESHOLD
    headphonesOn = DEFAULT_HEADPHONES_ON
    EAOn = DEFAULT_EA_ON  # Variable may not be necessary - Woermachine
    shotgunOn = DEFAULT_SHOTGUN_ON  # Variable may not be necessary - Woermachine
