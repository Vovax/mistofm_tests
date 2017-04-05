from config import MISTOFM_URL, WINDOW_SIZE
from ..site_parts.add_listener import AddListener
from ..site_parts.click_pause import ClickPause



class General(object):

    dependences = ('add_listener', 'click_pause')

    def __init__(self, dependences=dependences, driver=None, device='PC', testing_page=MISTOFM_URL):
        print('general')
        self.device = device
        self.driver = driver
        self.testing_page = testing_page
        self.call_dependences(dependences)

    def set_config(self):
        window_size = WINDOW_SIZE[self.device]
        self.driver.set_window_size(*window_size)
        self.driver.get(self.testing_page)
        print('set config')
        self.driver.implicitly_wait(3)

    def call_dependences(self, dependences):
        print('call dependences')
        classes = (AddListener, ClickPause)

        [a() for a in map(lambda cls: cls(driver=self.driver),
                          filter(lambda cls: cls.__repr__() in dependences, classes))]
