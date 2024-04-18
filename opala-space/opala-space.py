import pygame, random
try:
    #inicia o pygame
    pygame.init()

except:
    print('Erro em algum módulo do PyGame. Reinicie a aplicação.')
    pygame.quit()

largura = 1280
altura = 720

# Set initial values for variables
vidas = 5  # Assuming you start with 3 lives
pontos = 0
velocidade_alien = 1


#som do jogo
# pygame.mixer.music.set_volume(0.5)
# musica_fundo = pygame.mixer.music.load('sons/sons_Star Wars - The Imperial March.mp3')
# pygame.mixer.music.play(-1)

# barulho_disparo_torpedo = pygame.mixer.Sound('sons/star-wars-blaster.mp3')
# barulho_disparo_torpedo.set_volume(0.1)

# barulho_colisao_torpedo = pygame.mixer.Sound('sons/sons_smw_thunder.wav')
# barulho_colisao_torpedo.set_volume(2)

# barulho_colisao_alien = pygame.mixer.Sound('sons/blaster.mp3')
# barulho_colisao_alien.set_volume(2)


screen = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo Opala Space')

img_fundo = pygame.image.load('opala-space/images/fundo.jpg').convert_alpha()
img_fundo = pygame.transform.scale(img_fundo, (largura,altura))

img_alien = pygame.image.load('opala-space/images/allien.png').convert_alpha()
img_alien = pygame.transform.scale(img_alien, (200,200))
img_alien = pygame.transform.rotate(img_alien, +90)

#img da explosao
img_explosion = pygame.image.load('opala-space/images/explosao.png').convert_alpha()
img_explosion = pygame.transform.scale(img_explosion, (210, 210))

img_aviao = pygame.image.load('opala-space/images/nave.png').convert_alpha()
img_aviao = pygame.transform.scale(img_aviao, (150,150))
img_aviao = pygame.transform.rotate(img_aviao, -90)

img_missil = pygame.image.load('opala-space/images/missil.png')
img_missil = pygame.transform.scale(img_missil,(100,45))

x_alien = 1350
y_alien = 360

#explosao
x_explosion = 1350
y_explosion = 360


x_aviao = 200 
y_aviao = 300

velocidade_missil = 0
x_missil = 200
y_missil = 355

executar = True
velocidade_alien = 1
fogo = False

#cria objetos retangulo na tela em torno das figuras
aviao_rect = img_aviao.get_rect()
alien_rect = img_alien.get_rect()
missil_rect = img_missil.get_rect()

pontuacao = pygame.font.SysFont('fonts/PixelGameFont.tff', 50)
total_vidas = pygame.font.SysFont('fonts/PixelGameFont.tff', 50)

#função para detectar as colisões
def colisoes(x_alien, y_alien):
    global pontos, velocidade_alien, vidas
    if aviao_rect.colliderect(alien_rect) or alien_rect.x <= 60:

        #carrega a img do alien explodindo
        screen.blit(img_explosion, (x_alien, y_alien))

        velocidade_alien -= 0.1
        vidas = vidas -1
        return True
    
    elif missil_rect.colliderect(alien_rect):
        #carrega a img do alien explodindo
        screen.blit(img_explosion, (x_alien, y_alien))


        velocidade_alien += 0.1
        pontos = pontos + 1
        return True
    else:
        return False



def ressurgir_na_tela():
    x = 1350
    y = random.randint(1,640)
    return [x,y]

def recarregar_missil():
    novo_fogo = False
    novo_x_missil = x_aviao
    novo_y_missil = y_aviao + 55
    nova_velocidade_missil = 0
    return [novo_x_missil, novo_y_missil, novo_fogo, nova_velocidade_missil]


while executar:
     screen.blit(img_fundo,(0,0))
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executar = False
     
     x_rel = largura % img_fundo.get_rect().width
     screen.blit(img_fundo, (x_rel - img_fundo.get_rect().width,0))
     if x_rel < 1280:
        screen.blit(img_fundo, (x_rel, 0))

     tecla = pygame.key.get_pressed()
     if tecla[pygame.K_UP] and y_aviao > 1:
        y_aviao = y_aviao - 5
        if not fogo:
            y_missil = y_missil - 5
            
     if tecla[pygame.K_DOWN] and y_aviao < 665:
        y_aviao = y_aviao + 5
        if not fogo:
            y_missil = y_missil + 5

     if tecla[pygame.K_SPACE]:
        fogo = True
        velocidade_missil = 10

     if x_missil == 1300:
        x_missil, y_missil, fogo, velocidade_missil = recarregar_missil()

     if x_alien == 50 or colisoes(x_alien, y_alien):
        x_alien = ressurgir_na_tela()[0]
        y_alien = ressurgir_na_tela()[1]

     if vidas == 0:
        #carrega a img do aviao explodindo
        aux = (x_aviao, y_aviao)
        # screen.blit(img_explosion, (x_aviao, y_aviao))
        #troca a img do aviao pela explosao
        img_aviao = pygame.image.load('opala-space/images/explosao.png').convert_alpha()
        img_aviao = pygame.transform.scale(img_aviao, (210, 210))
        screen.blit(img_aviao, aux)
        executar = False


     largura = largura - 1
     x_missil = velocidade_missil + x_missil 
     x_alien = x_alien - velocidade_alien

     #adequando posição dos rect às imagens
     aviao_rect.y = y_aviao
     aviao_rect.x = x_aviao
   
     missil_rect.y = y_missil
     missil_rect.x = x_missil

     alien_rect.y = y_alien
     alien_rect.x = x_alien

     #exibir os pontos na tela
     score = pontuacao.render(f'Pontos: {int(pontos)}', True, (255,255,255))
     life = total_vidas.render(f'Vidas: {int(vidas)}', True, (255,255,255))

     #carrega as imagens na tela
     screen.blit(score, (50,50))
     screen.blit(life, (50,100))


     screen.blit(img_alien, (x_alien, y_alien))
     screen.blit(img_missil, (x_missil, y_missil))
     screen.blit(img_aviao, (x_aviao, y_aviao))
     pygame.display.update()


