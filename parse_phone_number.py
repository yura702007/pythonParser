from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.avito.ru/moskva/telefony/samsung_galaxy_a52_8256gb_black_ru_2305099331'


class Bot:
    def __init__(self, url=URL):
        self.url = url
        self.path_to_screen = 'avito_screen.png'
        self.driver = webdriver.Firefox()
        self.image_pos = None

    def run(self):
        self.navigate()
        self.take_screen()
        self.get_num_pos()

    def get_num_pos(self):
        image = self.driver.find_element(By.XPATH, '//img[@class="contacts-phone-3KtSI"]')
        x1 = image.location['x']
        y1 = image.location['y']
        x2 = x1 + image.size['width']
        y2 = y1 + image.size['height']
        self.image_pos = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2}

    def take_screen(self):
        self.driver.save_screenshot('avito_screen.png')

    def navigate(self):
        self.driver.get(self.url)
        btn = self.driver.find_element(By.XPATH, '//button[@class="styles-item-phone-button_height-3SOiy'
                                                 ' button-button-2Fo5k button-size-l-3LVJf '
                                                 'button-success-1Tf-u width-width-12-2VZLz"]')
        btn.click()


def main():
    bot = Bot()
    bot.run()
    # TODO import pillow
    print(bot.image_pos)


if __name__ == '__main__':
    main()
