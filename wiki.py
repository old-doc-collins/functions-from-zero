import wikipedia
from wikipedia import PageError
import click

@click.command()
@click.option('--name', default='wikipedia', help='entry to look up.')
@click.option('--length', default=1, help='number of sentences.')
def scrape(name, length):
    try:
        result = wikipedia.summary(name, sentences=length)
    except PageError:
        result = None
    print(result)


if __name__ == '__main__':
    scrape()



