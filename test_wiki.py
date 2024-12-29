from wiki import scrape

def test_scrape():
    assert scrape(name='calculus') is not None
    assert scrape(name='blargblumbpf') is None


