

#sonidos:
EAT_SOUND = pygame.mixer.Sound(r"C:\Users\acost\OneDrive\Escritorio\snake\sound\coin.wav")
CRASH_SOUND = pygame.mixer.Sound(r"C:\Users\acost\OneDrive\Escritorio\snake\sound\lose.mp3")

#musica:
pygame.mixer.music.load(r"C:\Users\acost\OneDrive\Escritorio\snake\sound\musicBackground.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

#fuente:
SCORE_TEXT = pygame.font.SysFont("Russo One", 25)