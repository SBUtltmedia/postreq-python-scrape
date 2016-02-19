import vcr
from src.scraper import scrape_page


@vcr.use_cassette('vcr_cassettes/CSE.yaml')
def test_scrape_page():
    assert scrape_page('CSE')

