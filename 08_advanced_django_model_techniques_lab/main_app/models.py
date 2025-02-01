from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.validators import validate_menu_categories


# Create your models here.
class ReviewMixin(models.Model):
    class Meta:
        abstract = True
        ordering = ['-rating']

    review_content = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(
                limit_value=2,
                message="Name must be at least 2 characters long."),
            MaxLengthValidator(100, message="Name cannot exceed 100 characters.")
        ])
    location = models.CharField(max_length=200, validators=[
        MinLengthValidator(limit_value=2,
                           message='Location must be at least 2 characters long.'),
        MaxLengthValidator(200, message="Location cannot exceed 200 characters.")
    ])
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[
        MinValueValidator(0, message='Rating must be at least 0.00.'),
        MaxValueValidator(5, message='Rating cannot exceed 5.00.')
    ])


class Menu(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(validators=[validate_menu_categories])
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)


class RestaurantReview(ReviewMixin, models.Model):
    reviewer_name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)


    class Meta(ReviewMixin.Meta):
        verbose_name = 'Restaurant Review'
        verbose_name_plural = 'Restaurant Reviews'
        unique_together = ['reviewer_name', 'restaurant']
        abstract = True


class RegularRestaurantReview(RestaurantReview):
    ...


class FoodCriticRestaurantReview(RestaurantReview):
    food_critic_cuisine_area = models.CharField(max_length=100)

    class Meta(RestaurantReview.Meta):
        verbose_name = 'Food Critic Review'
        verbose_name_plural = "Food Critic Reviews"


class MenuReview(ReviewMixin, models.Model):
    reviewer_name = models.CharField(max_length=100)
    menu = models.ForeignKey(to='Menu', on_delete=models.CASCADE)

    class Meta(ReviewMixin.Meta):
        verbose_name = 'Menu Review'
        verbose_name_plural = 'Menu Reviews'
        unique_together = ['reviewer_name', 'menu']
        indexes = [
            models.Index(fields=['menu'], name="main_app_menu_review_menu_id")
                 ]

# taka si pravim indeksi za Meta clas
# class Customer(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#
#     class Meta:
#         indexes = [
#             models.Index(fields=["last_name", "first_name"]),
#             models.Index(fields=["first_name"], name="first_name_idx"),
#         ]