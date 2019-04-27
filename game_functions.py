import sys
import pygame
from bullet import Bullet
from thano import Thano


def check_keydown_events(event, first_settings, screen, ship, bullets):  # 响应按键
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:  # 向右移动钢铁侠
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:  # 创建一颗子弹并且将其加入到编组bullets中
            fire_bullet(first_settings, screen, ship, bullets)
        elif event.key == pygame.K_q:
            sys.exit()
            '''if len(bullets) < first_settings.bullets_allowed:
                new_bullet = Bullet(first_settings,screen,ship)
           
                bullets.add(new_bullet)'''


def fire_bullet(first_settings, screen, ship, bullets):  # 如果未达到极限就发射一个子弹
    if len(bullets) < first_settings.bullets_allowed:  # 创建新子弹、并将其加入到编组bullets中
        new_bullet = Bullet(first_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):  # 响应松开
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def check_events(first_settings, screen, ship, bullets):  # 相应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, first_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(first_settings, screen, ship, thanos, bullets):  # 更新屏幕什么的图像，同时切换到新的屏幕
    screen.fill(first_settings.bg_color)  # 每次循环都重新绘制屏幕
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    thanos.draw(screen)
    # thano.blitme()
    pygame.display.flip()  # 让最近绘制的屏幕可见


def update_bullets(thanos, screen, ship, first_settings, bullets):  # 更新子弹的位置，并且删除已经消失的子弹
    bullets.update()  # 更新子弹的位置
    for bullet in bullets.copy():  # 删除已经消失的子弹
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_thano_collisions(first_settings, screen, ship, thanos, bullets)


def check_bullets_thano_collisions(thanos, screen, ship, first_settings, bullets):
    collisions = pygame.sprite.groupcollide(bullets, thanos, True, True)
    if(len(thanos)) == 0:  # 删除现有子弹并且重新创建一波泰坦飞船
        bullets.empty()
        create_fleet(first_settings, screen, ship, thanos)


def update_thanos(first_settings, thanos):  # 更新所有外星人的位置
    check_fleet_edges(first_settings, thanos)
    thanos.update()


def create_fleet(first_settings, screen, ship, thanos):  # 创建外星人群
    thano = Thano(first_settings, screen)
    number_thanos_x = get_number_thanos_x(first_settings, thano.rect.width)
    number_rows = get_number_rows(first_settings, ship.rect.height, thano.rect.height)
    for row_number in range(number_rows):
        for thano_number in range(number_thanos_x):
            create_thano(first_settings, screen, thanos, thano_number, row_number)


def get_number_thanos_x(first_settings,thano_width):  # 计算每行可以容纳多少泰坦飞船，间距为泰坦飞船宽度
    available_space_x = first_settings.screen_width - 2 * thano_width
    number_thanos_x = int(available_space_x / (2 * thano_width))
    return number_thanos_x


def create_thano(first_settings,screen,thanos,thano_number,row_number): # 创建一个泰坦飞船并且将其加入当前行
    thano = Thano(first_settings,screen)
    thano_width = thano.rect.width
    thano.x = thano_width + 2 * thano_width * thano_number
    thano.rect.x = thano.x
    thano.rect.y = thano.rect.height + 2 * thano.rect.height * row_number
    thanos.add(thano)


def get_number_rows(first_settings, ship_height, thano_height):  # 计算屏幕可容纳多少行外星人
    available_space_y = (first_settings.screen_height - (3 * thano_height - ship_height))
    number_rows = int(available_space_y / (2 * thano_height))
    return number_rows


def check_fleet_edges(first_settings, thanos):  # 外星人到达边缘以后采取的措施
    for thano in thanos.sprites():
        if thano.check_edges():
            change_fleet_direction(first_settings, thanos)
            break


def change_fleet_direction(first_settings, thanos):
    for thano in thanos.sprites():
        thano.rect.y += first_settings.fleet_drop_speed  # 将整群泰坦飞船向下移，并且改变它们移动的方向
    first_settings.fleet_direction *= -1


