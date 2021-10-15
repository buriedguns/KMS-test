import pytest
from faker import Faker

f = Faker()
url = 'https://www.kmslh.com/automation-test/'


@pytest.mark.landing
class TestLandingPage:

	def test_submit_form(self, pages_cluster):
		"""
		- Open the following page: https://www.kmslh.com/automation-test/
		- Fill all the relevant information with random valid values
		- Submit
		- Confirmation the submit was successful
		"""

		f_name, l_name, email, phone, company = (
			f.first_name(), f.last_name(), f'{f.first_name()}@max.com', f'7{f.random_number(9)}', f.company()
		)

		lp = pages_cluster.get('LandingPage')
		lp.session.get(url)
		lp.is_ready()
		lp.fill_submit_form(f_name, l_name, email, phone, company)
		lp.wait_for_congrats()
		assert 'Thank you for singing up!' in lp.congrats_msg.get_text()

	def test_open_video(self, pages_cluster):
		"""
		- Open the following page: https://www.kmslh.com/automation-test/
		- on the redirected page, wait for the popup and click copy link button
		- open the copied link.
		- Verify GE Healthcare: A KMS Lighthouse Success Story video is opened.
		"""

		lp = pages_cluster.get('LandingPage')
		lp.session.delete_all_cookies()
		lp.session.get(url)
		lp.wait_until_popup()
		video_url = lp.watch_video_link.get_link()
		lp.session.get(video_url)
		assert 'GE Healthcare: A KMS Lighthouse Success Story' in lp.youtube_title.get_text()
