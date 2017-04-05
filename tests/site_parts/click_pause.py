from .general_part import GeneralPart
import config
import time


class ClickPause(GeneralPart):

    def __init__(self, driver=None, testing_page=config.MISTOFM_URL):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page

    def __call__(self, *args, **kwargs):
        print('ClickPause')
        self.test_click_pause()

    @classmethod
    def __repr__(cls):
        return 'click_pause'

    def test_click_pause(self):
        # self.driver.get(self.testing_page)
        print('test_click_pause')


        # self.click_news_or_mark_or_subs(news_or_mark_or_subs='UserNews')

        click_pause = self.driver.find_elements_by_css_selector("*[id='pause']")
        print('click_pause')
        click_pause[0].click()
        time.sleep(3)

        self.driver.get(self.testing_page)
        time.sleep(3)

