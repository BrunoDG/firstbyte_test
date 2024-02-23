from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
from recipes.models import Recipe, Ingredient

class Command(BaseCommand):
    help = 'Scrape recipes from a website and import into the database'

    def handle(self, *args, **kwargs):
        # Your scraping logic here
        # Example: scrape data from a website and save it to the database
        url = 'https://example.com/recipes'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract recipe details and save to the database
        recipe = Recipe.objects.create(
            title='Scraped Recipe', instructions='Scraped Instructions')
        ingredient = Ingredient.objects.create(name='Scraped Ingredient')
        recipe.ingredients.add(ingredient)

        self.stdout.write(self.style.SUCCESS(
            'Successfully scraped and imported recipes'))
