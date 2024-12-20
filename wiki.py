import wikipedia


def scrape(name, length=1):
    try:
        result = wikipedia.summary(name, sentences=length)
    except:
        result = None
    return result


print(scrape('calculus', length=3))

r = scrape('blargblumpf')
print(r)