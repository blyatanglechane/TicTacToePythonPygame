import pygame
pygame.init()

class TicTacToe:

    def __check_win(self, mas, sign):
        zeroes = 0
        for row in mas:
            zeroes += row.count(0)
            if row.count(sign) == 3:
                return sign
        for col in range(3):
            if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
                return sign
        if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
            return sign
        if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
            return sign
        if zeroes == 0:
            return "Draw"
        return False


    def StartGame (self):
        # Делает инициализацию экрана
        size_block = 150
        margin = 20
        query = 0
        width = height = (margin * 4) + (size_block * 3)

        # Created a display. Enter the values of the height and width of the screen
        screen = pygame.display.set_mode((width, height))

        mas = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        # Window name
        pygame.display.set_caption("Tic Tac Toe Game")

        # Picture variable for the window
        img = pygame.image.load(r"C:\Users\Admin\Downloads\Скриншот 04-04-2023 211508.jpg")

        # Pass the picture variable
        pygame.display.set_icon(img)
        game_over = False
        # Делает инициализацию экрана
        pygame.init()
        size_block = 150
        margin = 20
        query = 0
        width = height = (margin * 4) + (size_block * 3)

        # Created a display. Enter the values of the height and width of the screen
        screen = pygame.display.set_mode((width, height))

        mas = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        # Window name
        pygame.display.set_caption("Tic Tac Toe Game")

        # Picture variable for the window
        img = pygame.image.load(r"C:\Users\Admin\Downloads\Скриншот 04-04-2023 211508.jpg")

        # Pass the picture variable
        pygame.display.set_icon(img)
        while True:
            # Intercept all events related to the window
            for event in pygame.event.get():

                # If we touch the cross
                if event.type == pygame.QUIT:
                    # Closing the window
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    col = x_mouse // (size_block + margin)
                    row = y_mouse // (size_block + margin)
                    if mas[row][col] == 0:
                        if query % 2 == 0:
                            mas[row][col] = 'x'
                        else:
                            mas[row][col] = 'o'
                        query += 1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_over = False
                    mas = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                    query = 0
                    screen.fill((0, 0, 0))

                for row in range(3):
                    for col in range(3):
                        if mas[row][col] == 'x':
                            color = (255, 0, 0)
                        elif mas[row][col] == 'o':
                            color = (0, 255, 0)
                        else:
                            color = (255, 255, 255)
                        x = col * size_block + (col + 1) * margin
                        y = row * size_block + (row + 1) * margin
                        pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                        if color == (255, 0, 0):
                            pygame.draw.line(screen, (255, 255, 255), (x + 5, y + 5),
                                            (x + size_block - 5, y + size_block - 5),
                                            3)
                            pygame.draw.line(screen, (255, 255, 255), (x + size_block - 5, y + 5),
                                            (x + 5, y + size_block - 5),
                                            3)
                        elif color == (0, 255, 0):
                            pygame.draw.circle(screen, (255, 255, 255), (x + size_block // 2, y + size_block // 2),
                                            size_block // 2 - 3, 3)

                if (query - 1) % 2 == 0:
                    game_over = self.__check_win(mas, 'x')
                else:
                    game_over = self.__check_win(mas, 'o')

                if game_over:
                    screen.fill((0, 0, 0))
                    font = pygame.font.SysFont('stxingkai', 80)
                    text1 = font.render(game_over, True, (255, 255, 255))
                    text_rect = text1.get_rect()
                    text_x = screen.get_width() / 2 - text_rect.width / 2
                    text_y = screen.get_height() / 2 - text_rect.height / 2
                    screen.blit(text1, [text_x, text_y])

                # обновляем экран
                pygame.display.update()

Game1 = TicTacToe()
Game1.StartGame()