import os
import django
from django.db.models import F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here


from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Create queries within functions

# 1 zadacha
def create_pet(name: str, species: str):
    Pet.objects.create(name=name, species=species)

    return f"{name} is a very cute {species}!"

    # 2ri variant
    # pet1 = Pet(
    #    name=name,
    #    species=species,
    # )
    # pet1.save()


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))

# 2 zadacha
def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    return f'The artifact {name} is {age} years old!'


def delete_all_artifacts():
    Artifact.objects.all().delete()


# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300, 'A magical amulet believed to bring good fortune', True))

# 3 zadacha
def show_all_locations():
    locations = Location.objects.all().order_by('-id')

    return '\n'.join(str(l) for l in locations)


def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()
    # vtori variant
    # Location.objects.filter(pk=1).update(is_capital=True)


def get_capitals():
    capitals = Location.objects.filter(is_capital=True)
    return capitals.values('name')


def delete_first_location():
    Location.objects.first().delete()


# print(show_all_locations())
# print(new_capital())
# print(get_capitals())

# 4 zadacha
def apply_discount():
    for car in Car.objects.all():
        discount = sum(int(x) for x in str(car.year)) / 100 * float(car.price)
        car.price_with_discount = float(car.price) - discount

        car.save()


def get_recent_cars():
    recent_cars = Car.objects.all().filter(year__gte=2020)
    return recent_cars.values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


# print(get_recent_cars())

# 5 zadacha
def show_unfinished_tasks():
    unfinished_tasks = Task.objects.filter(is_finished=False)
    return '\n'.join(str(task) for task in unfinished_tasks)


def complete_odd_tasks():
    for task in Task.objects.all():
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    tasks_with_title = Task.objects.filter(title=task_title)
    decoded_text = ''.join(chr(ord(x) - 3) for x in text)

    for task in tasks_with_title:
        task.description = decoded_text
        task.save()

    # vtori variant


# decoded_text = ''.join(chr(ord(x) - 3) for x in text)
# Task.objects.filter(title=task_title).update(description =decoded_text)

# 6 zadacha
def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
    even_id_rooms = []
    for room in deluxe_rooms:
        if room.id % 2 == 0:
            even_id_rooms.append(str(room))

    return '\n'.join(even_id_rooms)


def increase_room_capacity():
    rooms = HotelRoom.objects.all().order_by('id')
    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue
        if previous_room_capacity:
            room.capacity += previous_room_capacity
        elif not previous_room_capacity:
            room.capacity += room.id

        previous_room_capacity = room.capacity
        room.save()


def reserve_first_room():
    reserved_room = HotelRoom.objects.first()
    reserved_room.is_reserved = True
    reserved_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()
    if last_room.is_reserved:
        last_room.delete()


# 7 zadacha
def update_characters():
    mages = Character.objects.filter(class_name='Mage')
    for mage in mages:
        mage.level += 3
        mage.intelligence -= 7
        mage.save()

    warriors = Character.objects.filter(class_name='Warrior')
    for warrior in warriors:
        warrior.hit_points //= 2  # Decrease hit points by half
        warrior.dexterity += 4
        warrior.save()

    assassins_scouts = Character.objects.filter(class_name__in=['Assassin', 'Scout'])
    for character in assassins_scouts:
        character.inventory = 'The inventory is empty'
        character.save()


def fuse_characters(first_character: Character, second_character: Character):
    name = first_character.name + ' ' + second_character.name
    class_name = 'Fusion'
    level = (first_character.level + second_character.level) // 2
    strength = (first_character.strength + second_character.strength) * 1.2
    dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    hit_points = (first_character.hit_points + second_character.hit_points)

    if first_character.class_name in ('Mage', 'Scout'):
        inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    #elif first_character.class_name in ('Warrior', 'Assassin'):
    else:
        inventory = 'Dragon Scale Armor, Excalibur'

    Character.objects.create(
        name=name,
        class_name=class_name,
        level=level,
        strength= strength,
        dexterity=dexterity,
        intelligence=intelligence,
        hit_points=hit_points,
        inventory=inventory
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.update(dexterity=30)


def grand_intelligence():
    Character.objects.update(intelligence=40)


def grand_strength():
    Character.objects.update(strength=50)


def delete_characters():
    Character.objects.filter(inventory='The inventory is empty').delete()
