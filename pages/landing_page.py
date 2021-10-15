from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from elements.input import Input
from elements.button import Button
from elements.base_element import BaseElement
from .landing_page_locators import LandingPageLocators as Loc


class LandingPage:

	def __init__(self, session):
		self.session = session
		self.first_name_input = Input(session, Loc.first_name_input)
		self.last_name_input = Input(session, Loc.last_name_input)
		self.email_input = Input(session, Loc.email_input)
		self.phone_input = Input(session, Loc.phone_input)
		self.company_input = Input(session, Loc.company_input)
		self.submit_button = Button(session, Loc.submit_button)
		self.watch_video_link = BaseElement(session, Loc.popup_link)
		self.congrats_msg = BaseElement(session, Loc.congrats_msg)
		self.youtube_title = BaseElement(session, Loc.youtube_title)

	def is_ready(self):
		WebDriverWait(self.session, 15).until(ec.element_to_be_clickable(Loc.submit_button))

	def fill_submit_form(self, f_name, l_name, email, phone, company):
		self.first_name_input.clear_and_send_keys(f_name)
		self.last_name_input.clear_and_send_keys(l_name)
		self.email_input.clear_and_send_keys(email)
		self.phone_input.clear_and_send_keys(phone)
		self.company_input.clear_and_send_keys(company)
		self.submit_button.click()

	def wait_until_popup(self):
		WebDriverWait(self.session, 40).until(ec.presence_of_element_located(Loc.popup_link))

	def wait_for_congrats(self):
		WebDriverWait(self.session, 15).until(ec.presence_of_element_located(Loc.congrats_msg))

	def get_link_for_video(self):
		self.wait_until_popup()
		return self.watch_video_link.get_link()
