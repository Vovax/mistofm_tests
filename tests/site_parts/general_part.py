import config
import time


class GeneralPart(object):

    def __init__(self, driver):

        self.driver = driver
        self.get_xpath_add_listener = self.xpath_add_listener()
        # self.get_division_select_confirm_link = self.division_select_confirm_link()

    # @staticmethod
    # def division_select_confirm_link():
    #     return "/html/body/table[4]/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/pre/a"

    @staticmethod
    def xpath_add_listener():
        return "*[id='play']"


    def scroll_all(self, old_pos=0):
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            new_Height = self.driver.execute_script("return document.body.scrollHeight")
            if old_pos != new_Height:
                old_pos = new_Height
            else:
                return False
