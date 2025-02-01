import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import RealEstateListing, VideoGame, Exercise, Technology, Project, Programmer, Task

# Create and check models
# Run and print your queries


# ZADACHA 1
house_listings = RealEstateListing.objects.by_property_type('House')
print("House listings:")
for listing in house_listings:
    print(f"- {listing.property_type} in {listing.location}")
    # Run the 'in_price_range' method
affordable_listings = RealEstateListing.objects.in_price_range(75000.00, 120000.00)
print("Price in range listings:")
for listing in affordable_listings:
    print(f"- {listing.property_type} in {listing.location}")

    # Run the 'with_bedrooms' method
two_bedroom_listings = RealEstateListing.objects.with_bedrooms(2)
print("Two-bedroom listings:")
for listing in two_bedroom_listings:
    print(f"- {listing.property_type} in {listing.location}")


popular_locations = RealEstateListing.objects.popular_locations()
print("Popular locations:")
for location in popular_locations:
    print(f"- {location['location']}")

game1 = VideoGame.objects.get(title="The Last of Us Part II", genre="Action", release_year=2020, rating=9.0)
game2 = VideoGame.objects.get(title="Cyberpunk 2077", genre="RPG", release_year=2020, rating=7.2)
game3 = VideoGame.objects.get(title="Red Dead Redemption 2", genre="Adventure", release_year=2018, rating=9.7)
game4 = VideoGame.objects.get(title="FIFA 22", genre="Sports", release_year=2021, rating=8.5)
game5 = VideoGame.objects.get(title="Civilization VI", genre="Strategy", release_year=2016, rating=8.8)

action_games = VideoGame.objects.games_by_genre('Action')
recent_games = VideoGame.objects.recently_released_games(2019)
average_rating = VideoGame.objects.average_rating()
highest_rated = VideoGame.objects.highest_rated_game()
lowest_rated = VideoGame.objects.lowest_rated_game()

# # Print the results
# print(action_games)
# print(recent_games)
# print(average_rating)
# print(highest_rated)
# print(lowest_rated)


# ZADACHA 3
specific_project = Project.objects.get(name="Web App Project")
programmers_with_technologies = specific_project.get_programmers_with_technologies()
# Iterate through the related programmers and technologies
for programmer in programmers_with_technologies:
    print(f"Programmer: {programmer.name}")
    for technology in programmer.projects.get(name="Web App Project").technologies_used.all():
        print(f"- Technology: {technology.name}")
    # Execute the "get_projects_with_technologies" method for a specific programmer

specific_programmer = Programmer.objects.get(name="Alice")
projects_with_technologies = specific_programmer.get_projects_with_technologies()
# Iterate through the related projects and technologies

 # VAJNO ! TUK ITERIRAME PURVO ZA OPREDELEN PROEKT - NAPRIMER - WEBSAIT I TOZI WEBSAIT IZPOLZVA TEHNOLOGII:
for project in projects_with_technologies:
    print(f"Project: {project.name} for {specific_programmer.name}")
    for technology in project.technologies_used.all():  # ETO TUK IZBROQVAME KOI TEHNOLOGII IZPOLZVA PREDI DA PRODULJIM
                                                        # KUM SLEDVASHTIQ PROEKT
        print(f"- Technology: {technology.name}")

# task1 = Task.objects.create(
#     description='no description',
#     title='Clean',
#     priority='High',
#     is_completed=False,
#     completion_date='2022-12-12',
#     creation_date='2021-12-12')

# Zadacha 4 - trqbva da vurne "Clean"
task_1 = Task.objects.first()
tasks = task_1.overdue_high_priority_tasks()
print("Overdue High Priority Tasks:")
for task in tasks:
    print('- ' + task.title)



