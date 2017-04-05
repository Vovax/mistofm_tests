from .general_part import GeneralPart
import config
import time


class AddListener(GeneralPart):

    def __init__(self, driver=None, testing_page=config.MISTOFM_URL):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page

    def __call__(self, *args, **kwargs):
        print('AddListener')
        self.test_add_listener()

    @classmethod
    def __repr__(cls):
        return 'add_listener'

    def test_add_listener(self):
        # self.driver.get(self.testing_page)
        print('test_add_listener')


        # self.click_news_or_mark_or_subs(news_or_mark_or_subs='UserNews')

        add_listener = self.driver.find_elements_by_css_selector("*[id='play']")
        add_listener[0].click()
        time.sleep(3)

        # for count_listener in range(0, int(add_listener[0].text)):
        #     print(count_listener)
        #
        #     assert count_listener + 1 or count_listener - 1

        self.driver.get(self.testing_page)
        time.sleep(3)

