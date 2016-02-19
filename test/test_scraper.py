import vcr
from src.scraper import scrape_page


@vcr.use_cassette('vcr_cassettes/CSE.yaml')
def test_scrape_page():
    data = scrape_page('CSE')
    assert len(data) == 64

