from mylib.wikistuff import scrape
import click

@click.command()
@click.option('--name', prompt='entry', help='entry to look up.')
@click.option('--length', default=1, help='number of sentences.')
def run(name, length=1):
    result = scrape(name, length)
    print(result)

if __name__ == '__main__':
    run()



