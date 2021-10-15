from selenium.webdriver.common.by import By


class LandingPageLocators:

	first_name_input = By.CSS_SELECTOR, '[name="firstname"]'
	last_name_input = By.CSS_SELECTOR, '[name="lastname"]'
	email_input = By.CSS_SELECTOR, '[name="email"]'
	phone_input = By.CSS_SELECTOR, '[name="phone"]'
	company_input = By.CSS_SELECTOR, '[name="company"]'
	submit_button = By.CSS_SELECTOR, '[value="Submit"]'
	popup_link = By.XPATH, "//*[text()='Watch The Video']"
	congrats_msg = By.CSS_SELECTOR, '.elementor-heading-title.elementor-size-small'
	youtube_title = By.CSS_SELECTOR, 'h1.title.ytd-video-primary-info-renderer'
