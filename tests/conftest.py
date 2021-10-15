import pytest
from selenium import webdriver
from pages.landing_page import LandingPage


@pytest.fixture(scope='session', autouse=True)
def session():
	driver = webdriver.Chrome()
	yield driver
	driver.quit()


@pytest.fixture(scope='session', autouse=True)
def pages_cluster(session):
	yield {"LandingPage": LandingPage(session)}
