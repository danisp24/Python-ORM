import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver, Registration, Car, \
    Owner
from datetime import timedelta, date


# Create queries within functions


def show_all_authors_with_their_books():
    authors = Author.objects.all().order_by('id')
    result = []
    for author in authors:
        books = Book.objects.filter(author=author)
        if not books:
            continue
        titles = ', '.join(book.title for book in books)
        result.append(f"{author.name} has written - {titles}!")
    return '\n'.join(result)


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()

# Create authors

# author1 = Author.objects.create(name="J.K. Rowling")
# author2 = Author.objects.create(name="George Orwell")
# author3 = Author.objects.create(name="Harper Lee")
# author4 = Author.objects.create(name="Mark Twain")
#
# # Create books associated with the authors
#
# book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", price=19.99, author=author1)
# book2 = Book.objects.create( title="1984", price=14.99, author=author2)
# book3 = Book.objects.create( title="To Kill a Mockingbird", price=12.99, author=author3)
# # Display authors and their books
# authors_with_books = show_all_authors_with_their_books()
# print(authors_with_books)
# # Delete authors without books
# delete_all_authors_without_books()
# print(Author.objects.count())


# zadacha 2
def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.remove(song)


# 3 zadacha
def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()
    total = 0
    for review in reviews:
        total += int(review.rating)

    average_rating = total / len(reviews)
    return average_rating


def get_reviews_with_high_ratings(threshold: int):
    reviews = Review.objects.filter(rating__gte=threshold)
    return reviews


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    return Product.objects.filter(reviews__isnull=True).delete()


# products_without_reviews = get_products_with_no_reviews()
#
# print(f"Products without reviews: {', '.join([p.name for p in products_without_reviews])}")
#
# delete_products_without_reviews()
# print(f"Products left: {Product.objects.count()}")
# print(calculate_average_rating_for_product_by_name("Laptop"))

# 4 zadacha

def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.order_by('-license_number')
    result = []
    for license_exp in licenses:
        exp_date = license_exp.issue_date + timedelta(days=365)
        result.append(f'License with id: {license_exp.license_number} expires on {exp_date}!')

    return '\n'.join(result)


def get_drivers_with_expired_licenses(due_date):
    # exp_date = due_date - timedelta(days=365)
    # exp_license_drivers = Driver.objects.filter(drivinglicense__issue_date__gt=exp_date)
    # return exp_license_drivers

    # 2ri variant
    drivers = Driver.objects.all()
    exp_license_drivers = []
    for driver in drivers:
        exp_date = driver.drivinglicense.issue_date + timedelta(365)
        if exp_date > due_date:
            exp_license_drivers.append(driver)

    return exp_license_drivers


# driver1 = Driver.objects.create(first_name="Tanya", last_name="Petrova")
#
# driver2 = Driver.objects.create(first_name="Ivan", last_name="Yordanov")
#
# license1 = DrivingLicense.objects.create(license_number="123", issue_date=date(2022, 10, 6), driver=driver1)
# license2 = DrivingLicense.objects.create(license_number="456", issue_date=date(2022, 1, 1), driver=driver2)

#
# expiration_dates = calculate_licenses_expiration_dates()
# print(expiration_dates)
# drivers_with_expired_licenses = get_drivers_with_expired_licenses(date(2023, 1, 1))
# for driver in drivers_with_expired_licenses:
#     print(f"{driver.first_name} {driver.last_name} has to renew their driving license!")


def register_car_by_owner(owner: Owner):
    register = Registration.objects.filter(car__isnull=True).first()
    vehicle = Car.objects.filter(registration__isnull=True).first()

    vehicle.owner = owner
    vehicle.registration = register
    vehicle.save()

    register.car = vehicle
    register.registration_date = date.today()
    register.save()

    return (f'Successfully registered {vehicle.model} to {owner.name} '
            f'with registration number {register.registration_number}.')







