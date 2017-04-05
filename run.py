import argparse
from tests.pages.index import IndexPage
import config
from selenium import webdriver

parser = argparse.ArgumentParser(description='Test for mistofm')
parser.add_argument("site")
parser.add_argument("device")
args = parser.parse_args()


def start_test(device):
    # testing_page = config.MISTOFM_URL

    driver = webdriver.Firefox(executable_path='/Users/apple/Desktop/mistofm_tests/venv/selenium/geckodriver')
    IndexPage(device=device, driver=driver)


if __name__ == '__main__':
    if 'mistofm' in args.site:
        print(args.device.split("'")[-2])
        start_test(device=args.device.split("'")[-2])
