import pygame
import hero_class
import enemy_class

pygame.init()  # предварительный запуск зависимостей
clock = pygame.time.Clock()  # создание экземпляра класса слок
GREEN = (0, 255, 0)  # задаём цвета для ужобной работы
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

kill_enemy_hero1 = 0
kill_enemy_hero2 = 0

screen_size = wight, height = 800, 800  # задаём ширину высоту для удобной работы
screen = pygame.display.set_mode(screen_size)  # задаём размер экрана
pygame.display.set_caption('Моя игра')  # название окна

hero1 = hero_class.Player(wight, height)  # создание экземпляра класса
hero2 = hero_class.Player(
    wight, height, 2, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_l, size_image=0.09
)

all_enemy = pygame.sprite.Group()

for i in range(1, 10):  # создать 10 врагов
    mob = enemy_class.Enemy()
    all_enemy.add(mob)

running = True  # игровой цикл

while running:  # запуск игрового цикла
    if len(all_enemy) < 10:  # если врагов меньше 10 , то создать новый эеземпляр класса врага
        mob = enemy_class.Enemy()
        all_enemy.add(mob)

    screen.fill(BLACK)
    clock.tick(60)  # устанавливаем количество игровыйх фреймов в секунду ( повторений while)
    for event in pygame.event.get():  # перебераем все события
        if event.type == pygame.QUIT:  # если нажали на крестик
            running = False

    hero1.update()  # обновление расположения коробля
    hero2.update()

    # отрисовка врагов
    all_enemy.update()
    all_enemy.draw(screen)

    hero1.all_bullet.update()
    hero2.all_bullet.update()
    hero1.all_bullet.draw(screen)
    hero2.all_bullet.draw(screen)

    if pygame.sprite.spritecollide(hero1, all_enemy, False):  # остоновка
        running = False
    if pygame.sprite.spritecollide(hero2, all_enemy, False):
        running = False

    if pygame.sprite.groupcollide(hero1.all_bullet, all_enemy, True, True):
        kill_enemy_hero1 += 1
        print('убито 1 игроком =',kill_enemy_hero1)


    if pygame.sprite.groupcollide(hero2.all_bullet, all_enemy, True, True):
        kill_enemy_hero2 += 1
        print('убито 2 игроком =', kill_enemy_hero2)

    screen.blit(hero1.image, hero1.rect)  # отрисовка кораблика
    screen.blit(hero2.image, hero2.rect)  # отрисовка кораблика
    pygame.display.update()  # обновляем наш дисплей

pygame.quit()  # завершаем все зависимости pygame
