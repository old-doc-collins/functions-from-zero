import wikipedia


def scrape(name, length=1):
    result = wikipedia.summary(name, sentences=length)
    return result


print(scrape('calculus', length=3))