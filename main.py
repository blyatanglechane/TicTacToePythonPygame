import pygame
pygame.init()


class TicTacToe:

    @staticmethod
    def __validate(mas, current):
        flag = 0
        for row in mas:
            flag += row.count(0)
            if row.count(current) == 3:
                if current == 'x':
                    return "Победили крестики! урааа"
                else:
                    return "Победили нолики! абалдеть"
        for col in range(3):
            if mas[0][col] == current and mas[1][col] == current and mas[2][col] == current:
                if current == 'x':
                    return "Победили крестики! урааа"
                else:
                    return "Победили нолики! абалдеть"
        if mas[0][0] == current and mas[1][1] == current and mas[2][2] == current:
            if current == 'x':
                return "Победили крестики! урааа"
            else:
                return "Победили нолики! абалдеть"
        if mas[0][2] == current and mas[1][1] == current and mas[2][0] == current:
            if current == 'x':
                return "Победили крестики! урааа"
            else:
                return "Победили нолики! абалдеть"
        if flag == 0:
            return "Ничья"
        return False

    def start_game(self):
        # Window name
        pygame.display.set_caption("Tic Tac Toe Funny Game")
        # Picture variable for the window
        icon = pygame.image.load(r"C:\Users\Admin\Downloads\Скриншот 04-04-2023 211508.jpg")

        # Pass the picture variable
        pygame.display.set_icon(icon)
        check = False
        cell = 180
        between = 30
        index = 0
        width = height = (between * 4) + (cell * 3)

        # Created a display. Enter the values of the height and width of the screen
        screen = pygame.display.set_mode((width, height))
        playing_area = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        # Window name
        pygame.display.set_caption("Tic Tac Toe Cool Game")
        # Picture variable for the window
        img = pygame.image.load(r"C:\Users\Admin\Downloads\Скриншот 04-04-2023 211508.jpg")
        # Pass the picture variable
        pygame.display.set_icon(img)

        pygame.mixer.music.load("ound.mp3")
        pygame.mixer.music.play(-1)

        touch_sound = pygame.mixer.Sound("touch.wav")

        while True:
            image = pygame.image.load('fon.png').convert_alpha()
            screen.blit(image, (0, 0))
            i_cross = pygame.image.load('cross.png').convert_alpha()
            i_zero = pygame.image.load('zero.png').convert_alpha()
            i_cross = pygame.transform.scale(i_cross, (cell, cell))
            i_zero = pygame.transform.scale(i_zero, (cell, cell))
            # Intercept all events related to the window
            for event in pygame.event.get():

                # If we touch the cross
                if event.type == pygame.QUIT:
                    # Closing the window
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and not check:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    col = x_mouse // (cell + between)
                    row = y_mouse // (cell + between)
                    if playing_area[row][col] == 0:
                        if index % 2 == 0:
                            playing_area[row][col] = 'x'
                            touch_sound.play()
                        else:
                            playing_area[row][col] = 'o'
                            touch_sound.play()
                        index += 1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    playing_area = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                    index = 0
                    screen.fill((0, 0, 0))

                for row in range(3):
                    for col in range(3):
                        if playing_area[row][col] == 'x':
                            color = (255, 0, 0)
                        elif playing_area[row][col] == 'o':
                            color = (0, 255, 0)
                        else:
                            color = (255, 255, 255)
                        x = col * cell + (col + 1) * between
                        y = row * cell + (row + 1) * between
                        pygame.draw.rect(screen, color, (x, y, cell, cell))
                        if color == (255, 0, 0):
                            screen.blit(i_cross, (x, y))
                        elif color == (0, 255, 0):
                            screen.blit(i_zero, (x, y))
                if (index - 1) % 2 == 0:
                    check = self.__validate(playing_area, 'x')
                else:
                    check = self.__validate(playing_area, 'o')

                if check:
                    screen.fill((200, 0, 245))
                    font = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuilight', 65)
                    text1 = font.render(check, True, (228, 228, 228))
                    text_rect = text1.get_rect()
                    text_x = screen.get_width() / 2 - text_rect.width / 2
                    text_y = screen.get_height() / 2 - text_rect.height / 2
                    screen.blit(text1, [text_x, text_y])

                # обновляем экран
                pygame.display.update()


Game1 = TicTacToe()
Game1.start_game()
