import os
import django
from django.db.models import Case, When, Value

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout


# Create and check models
# Run and print your queries

# 1 zadacha
def show_highest_rated_art():
    best_artwork = ArtworkGallery.objects.order_by('-rating', 'id').first()

    return (f"{best_artwork.art_name} is the highest-rated art "
            f"with a {best_artwork.rating} rating!")


def bulk_create_arts(first_art, second_art):
    ArtworkGallery.objects.bulk_create([first_art, second_art])


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


# 2 zadacha
def show_the_most_expensive_laptop():
    most_expensive_laptop = Laptop.objects.order_by('-price', '-id').first()

    return (f"{most_expensive_laptop.brand} is the most expensive laptop available for "
            f"{most_expensive_laptop.price}$!")


def bulk_create_laptops(*args):
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=['Asus', 'Lenovo']).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=('Apple', 'Dell', 'Acer')).update(memory=16)


def update_operation_systems():
    Laptop.objects.filter(brand='Asus').update(operation_system='Windows')
    Laptop.objects.filter(brand='Apple').update(operation_system='MacOS')
    Laptop.objects.filter(brand__in=('Dell', 'Acer')).update(operation_system='Linux')
    Laptop.objects.filter(brand='Lenovo').update(operation_system='Chrome OS')


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


# laptop1 = Laptop(brand='Asus', processor='Intel Core i5', memory=8, storage=256, operation_system='Windows', price=899.99)
# laptop2 = Laptop(brand='Apple', processor='Apple M1', memory=16, storage=512, operation_system='MacOS', price=1399.99)

# laptop3 = Laptop(brand='Lenovo', processor='AMD Ryzen 7', memory=12, storage=512, operation_system='Linux', price=999.99,)

# laptops_to_create = [laptop1, laptop2, laptop3]
# bulk_create_laptops(laptops_to_create)

# update_to_512_GB_storage()
# update_operation_systems()

# asus_laptop = Laptop.objects.filter(brand__exact='Asus').get()
# lenovo_laptop = Laptop.objects.filter(brand__exact='Lenovo').get()
# print(asus_laptop.storage)
# print(lenovo_laptop.operation_system)


# 3 zadacha
def bulk_create_chess_players(*args):
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players():
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title__exact='GM').update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title__exact='no title').update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=(2300, 2399)).update(title='IM')


def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=(2200, 2299)).update(title='FM')


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__range=(0, 2199)).update(title='regular player')


# 4 zadacha
def set_new_chefs():
    Meal.objects.update(chef=Case
        (
        When(meal_type='Breakfast', then=Value("Gordon Ramsay")),
        When(meal_type='Lunch', then=Value("Julia Child")),
        When(meal_type='Dinner', then=Value("Jamie Oliver")),
        When(meal_type='Snack', then=Value("Thomas Keller")),
    ))


def set_new_preparation_times():
    Meal.objects.filter(meal_type='Breakfast').update(preparation_time='10 minutes')
    Meal.objects.filter(meal_type='Lunch').update(preparation_time='12 minutes')
    Meal.objects.filter(meal_type='Dinner').update(preparation_time='15 minutes')
    Meal.objects.filter(meal_type='Snack').update(preparation_time='5 minutes')


def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=['Breakfast', 'Dinner']).update(calories=400)


def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).update(calories=700)


def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=('Lunch', 'Snack')).delete()


# 5 zadacha

def show_hard_dungeons():
    result = []
    hard_dungeons = Dungeon.objects.filter(difficulty='Hard').order_by('-location')
    for dungeon in hard_dungeons:
        result.append(f'{dungeon.name} is guarded by {dungeon.boss_name} who has {dungeon.boss_health} health points!')

    return '\n'.join(result)


def bulk_create_dungeons(*args):
    Dungeon.objects.bulk_create(*args)


def update_dungeon_names():
    Dungeon.objects.update(name=Case
        (
        When(difficulty='Easy', then=Value("The Erased Thombs")),
        When(difficulty='Medium', then=Value("The Coral Labyrinth")),
        When(difficulty='Hard', then=Value('The Lost Haunt')),
    ))


def update_dungeon_bosses_health():
    Dungeon.objects.exclude(difficulty='Easy').update(boss_health=500)


def update_dungeon_recommended_levels():
    Dungeon.objects.filter(difficulty='Easy').update(recommended_level=25)
    Dungeon.objects.filter(difficulty='Medium').update(recommended_level=50)
    Dungeon.objects.filter(difficulty='Hard').update(recommended_level=75)


def update_dungeon_rewards():
    Dungeon.objects.filter(boss_health=500).update(reward="1000 Gold")
    Dungeon.objects.filter(location__startswith="E").update(reward='New dungeon unlocked')
    Dungeon.objects.filter(location__endswith='s').update(reward='Dragonheart Amulet')


def set_new_locations():
    Dungeon.objects.update(
        location=Case(
            When(recommended_level=25, then=Value('Enchanted Maze')),
            When(recommended_level=50, then=Value('Grimstone Mines')),
            When(recommended_level=75, then=Value('Shadowed Abyss')),
        )
    )


# zadacha 6
def show_workouts():
    workouts = Workout.objects.filter(workout_type__in=['Calisthenics', 'CrossFit'])
    result = []
    for workout in workouts:
        result.append(f'{workout.name} from {workout.workout_type} type has {workout.difficulty} difficulty!')

    return '\n'.join(result)


def get_high_difficulty_cardio_workouts():
    return Workout.objects.filter(workout_type='Cardio', difficulty='High').order_by('instructor')


def set_new_instructors():
    Workout.objects.filter(workout_type='Cardio').update(instructor='John Smith')
    Workout.objects.filter(workout_type='Strength').update(instructor='Michael Williams')
    Workout.objects.filter(workout_type='Yoga').update(instructor='Emily Johnson')
    Workout.objects.filter(workout_type='CrossFit').update(instructor='Sarah Davis')
    Workout.objects.filter(workout_type='Calisthenics').update(instructor='Chris Heria')


def set_new_duration_times():
    Workout.objects.update(duration=Case(
        When(instructor='John Smith', then=Value("15 minutes")),
        When(instructor='Sarah Davis', then=Value("30 minutes")),
        When(instructor='Chris Heria', then=Value("45 minutes")),
        When(instructor='Michael Williams', then=Value("1 hour")),
        When(instructor='Emily Johnson', then=Value("1 hour and 30 minutes")),
    ))


def delete_workouts():
    Workout.objects.exclude(workout_type__in=['Strength', 'Calisthenics']).delete()

# print(show_workouts())

# high_difficulty_cardio_workouts = get_high_difficulty_cardio_workouts()
# for workout in high_difficulty_cardio_workouts:
#    print(f"{workout.name} by {workout.instructor}")

# set_new_instructors()
# workouts_with_new_instructors = Workout.objects.all()
# for workout in workouts_with_new_instructors:
#    print(f"Instructor: {workout.instructor}")

# set_new_duration_times()
# workouts_with_new_durations = Workout.objects.all()
# for workout in workouts_with_new_durations:
#    print(f"Duration: {workout.duration}")
