import pygame

mapa = [
    "pppppppppppppppppppppppppppppppppppppppp",
    "p                                      p",
    "p        f                             p",
    "p              f                       p",
    "p                                      p",
    "p       f                 pppppp   f   p",
    "p                         p            p",
    "p           f             p            p",
    "p                 ppppppppp  f         p",
    "p                 p                    p",
    "p                 p                    p",
    "p                 p    f               p",
    "p        f        p                    p",
    "p                 p      f             p",
    "p                 p                    p",
    "p                 p                    p",
    "p        pppppppppp                    p",
    "p        f                             p",
    "p                               f      p",
    "pppppppppppppppppppppppppppppppppppppppp",
]

mapa_objts = [
    "                                        ",
    "     gbg                             gv ",
    "     v  v                               ",
    "                        b               ",
    "                                        ",
    "              v                         ",
    "                                        ",
    "                                        ",
    "                                        ",
    "       v                                ",
    "                                        ",
    "                                        ",
    "                   g                 v  ",
    "  b                                     ",
    "                                        ",
    "                           bg           ",
    "                                        ",
    "     b                         v        ",
    "       gv     b                         ",
    "                                        ",
]


TELA_WIDTH = 800
TELA_HEIGHT = 600
BLK_WIDTH = TELA_WIDTH // 40
BLK_HEIGHT = TELA_HEIGHT // 20

def load_image(img_set, col, lin):
    img_orig = img_set.subsurface((col, lin), (16, 16))
    img_scaled = pygame.transform.scale(img_orig, (BLK_WIDTH, BLK_HEIGHT))
    return img_scaled
