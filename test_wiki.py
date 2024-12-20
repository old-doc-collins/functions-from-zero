from wiki import scrape

def test_scrape():
    assert scrape('calculus') is not None
    assert scrape('blargblumbpf') is None


