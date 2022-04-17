from estrutura import *
from random import uniform

jogar = 1

while jogar == 1:
    pygame.init()
    tela = pygame.display.set_mode((TELA_WIDTH, TELA_HEIGHT))

    tiles = pygame.image.load("./basictiles.png").convert_alpha()
    perso = pygame.image.load("./characters.png").convert_alpha()

    img_vaso = load_image(tiles, 48, 48)
    img_fogo = load_image(tiles, 64, 112)
    img_bau = load_image(tiles, 64, 64)
    img_grama = load_image(tiles, 16, 128)
    img_flor = load_image(tiles, 64, 16)
    img_parede = load_image(tiles, 48, 0)

    def desenha_mapa(mapas, caracter_imagem):
        for id_linha, linha in enumerate(mapas):
            for id_coluna, caracter in enumerate(linha):
                if caracter in caracter_imagem:
                    x = id_coluna * BLK_WIDTH
                    y = id_linha * BLK_HEIGHT
                    img = caracter_imagem[caracter]
                    tela.blit(img, (x, y))

    def teste_colisao_mapa(personagem, map, lista_caracteres):
        colisoes = []
        for id_l, l in enumerate(map):
            for id_c, carac in enumerate(l):
                if carac in lista_caracteres:
                    z = id_c * BLK_WIDTH
                    k = id_l * BLK_HEIGHT
                    r = pygame.Rect((z, k), (BLK_WIDTH, BLK_HEIGHT))
                    r2 = personagem.rect.copy()
                    r2.move_ip(personagem.vel_x, personagem.vel_y)
                    if r.colliderect(r2):
                        colisao = {"linha": id_l, "coluna": id_c, "caracter": carac}
                        colisoes.append(colisao)
        return colisoes

    class Personagem(pygame.sprite.Sprite):
        def __init__(self):
            self.vivo = True
            self.hp = 100.0
            self.score = 0
            pygame.sprite.Sprite.__init__(self)
            self.vel_x = 0.0
            self.vel_y = 0.0
            perso_1 = load_image(perso, 48, 0)
            perso_2 = load_image(perso, 64, 0)
            perso_3 = load_image(perso, 80, 0)
            self.lista_imagens = [perso_1, perso_2, perso_3]
            self.image_idx = 0
            self.image = perso_1
            self.rect = pygame.Rect((32, 32), (BLK_WIDTH, BLK_HEIGHT))

        def update(self):
            self.image = self.lista_imagens[self.image_idx]
            self.image_idx += 1
            if self.image_idx >= len(self.lista_imagens):
                self.image_idx = 0

            colisoes_movimento = teste_colisao_mapa(self, mapa, ["p"])
            colisao_vaso = teste_colisao_mapa(self, mapa_objts, ["v"])
            colisao_fogo = teste_colisao_mapa(self, mapa_objts, ["g"])
            if len(colisoes_movimento or colisao_vaso or colisao_fogo) == 0:
                self.rect.move_ip(self.vel_x, self.vel_y)


            if len(colisao_fogo) != 0:
                dano = uniform(0.02, 1.0)
                self.hp = self.hp - dano
                if self.hp <= 0:
                    self.kill()
                    self.vivo = False
                print('Dano: {:.2f}'.format(dano))
                print('HP: {:.2f}'.format(self.hp))


            colisao_bau = teste_colisao_mapa(self, mapa_objts, ["b"])
            for colisao in colisao_bau:
                ganha_score = 10
                self.score = self.score + ganha_score
                #Removendo bau
                linha = mapa_objts[colisao["linha"]]
                lista = list(linha)
                lista[colisao["coluna"]] = " "
                linha_texto = "".join(lista)
                mapa_objts[colisao["linha"]] = linha_texto
                print('Score: {}'.format(self.score))


        def processar_evento(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.vel_x = 1.0
                if event.key == pygame.K_a:
                    self.vel_x = -1.0
                if event.key == pygame.K_w:
                    self.vel_y = -1.0
                if event.key == pygame.K_s:
                    self.vel_y = 1.0
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_a, pygame.K_d]:
                    self.vel_x = 0.0
                if event.key in [pygame.K_w, pygame.K_s]:
                    self.vel_y = 0.0

    heroi = Personagem()
    grupo_heroi = pygame.sprite.Group(heroi)


    while True:
        desenha_mapa(mapa, {"p": img_parede, "f": img_flor, " ": img_grama})
        desenha_mapa(mapa_objts, {"v": img_vaso, "b": img_bau, "g": img_fogo})

        grupo_heroi.draw(tela)
        pygame.display.update()
        grupo_heroi.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            heroi.processar_evento(e)
