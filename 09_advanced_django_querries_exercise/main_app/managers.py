from decimal import Decimal

from django.db import models
from django.db.models import Q, Count, Max, Min, Avg


class RealEstateListingManager(models.Manager):

    def by_property_type(self, property_type: str):
        return self.filter(property_type=property_type)

    def in_price_range(self, min_price: Decimal, max_price: Decimal):
        return self.filter(Q(price__gte=min_price) & Q(price__lte=max_price))

    def with_bedrooms(self, bedrooms_count: int):
        return self.filter(bedrooms=bedrooms_count)

    def popular_locations(self):
        return (self.values('location').
                annotate(popular_locations=Count('location')).
                order_by('-popular_locations', 'id')[:2]
                )


class VideoGameManager(models.Manager):

    def games_by_genre(self, genre: str):
        return self.filter(genre=genre)

    def recently_released_games(self, year: int):
        return self.filter(release_year__gte=year)

    def highest_rated_game(self):
        return self.annotate(highest_rating=Max('rating')).order_by('highest_rating').last()

    def lowest_rated_game(self):

        # min_rated_game = self.aggregate(min_rating=Min('rating'))['min_rating']
        # return self.filter(rating=min_rated_game).first() - variant s aggregate

        return self.annotate(lowest_rating=Min('rating')).order_by('lowest_rating').first()

    def average_rating(self):
        average_rating = self.aggregate(average_rating=Avg('rating'))["average_rating"]
        return f'{average_rating:.1f}'
