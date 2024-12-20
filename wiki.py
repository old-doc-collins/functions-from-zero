import wikipedia
from wikipedia import PageError


def scrape(name, length=1):
    try:
        result = wikipedia.summary(name, sentences=length)
    except PageError:
        result = None
    return result


print(scrape('calculus', length=3))

r = scrape('blargblumpf')
print(r)