import os
from datetime import date

import django
from django.core.exceptions import ValidationError

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Necromancer, Mage, Student, CreditCard, SpecialReservation, Room, Hotel

# Create queries within functions
# Create instances

# mage = Mage.objects.create(
#
# name="Fire Mage",
#
# description="A powerful mage specializing in fire magic.",
#
# elemental_power="Fire",
#
# spellbook_type="Ancient Grimoire"
#
# )
#
# necromancer = Necromancer.objects.create(
#
# name="Dark Necromancer",
#
# description="A mage specializing in dark necromancy.",
#
# elemental_power="Darkness", spellbook_type="Necronomicon",
#
# raise_dead_ability="Raise Undead Army"
#
# )
#
# print(mage.elemental_power)
#
# print(mage.spellbook_type)
#
# print(necromancer.name)
# print(necromancer.description)
# print(necromancer.raise_dead_ability)

# student1 = Student(name="John", student_id=12345)
#
# student1.save()
#
# student2 = Student(name="Alice", student_id=45.23)
#
# student2.save()
#
# student3 = Student(name="Bob", student_id="789")
#
# student3.save()
#
# # Retrieving student IDs from the database
#
# retrieved_student1 = Student.objects.get(name="John")
#
# retrieved_student2 = Student.objects.get(name="Alice")
#
# retrieved_student3 = Student.objects.get(name="Bob")
#
# print(retrieved_student1.student_id)
#
# print(retrieved_student2.student_id)
#
# print(retrieved_student3.student_id)


# # Create CreditCard instances with card owner names and card numbers
#
# credit_card1 = CreditCard.objects.create(card_owner="Krasimir", card_number="1234567890123450")
#
# credit_card2 = CreditCard.objects.create(card_owner="Pesho", card_number="9876543210987654")
#
# credit_card3 = CreditCard.objects.create(card_owner="Vankata", card_number="4567890123456789")
#
# # Save the instances to the database
#
# credit_card1.save()
#
# credit_card2.save()
#
# credit_card3.save()
#
# # Retrieve the CreditCard instances from the database
#
# credit_cards = CreditCard.objects.all()
#
# # Display the card owner names and masked card numbers

# for credit_card in credit_cards:
#     print(f"Card Owner: {credit_card.card_owner}")
#     print(f"Card Number: {credit_card.card_number}")

# Create a Hotel instance
#
# hotel = Hotel.objects.create(name="Hotel ABCa", address="1234 Main St")
#
# # Create Room instances associated with the hotel
#
# room1 = Room.objects.create(
#
#     hotel=hotel,
#
#     number="301", capacity=2, total_guests=1, price_per_night=100.00)
# # Create SpecialReservation instances
# #
# special_reservation1 = SpecialReservation(room=room1, start_date=date(2020, 1, 1), end_date=date(2020, 1, 5))
# print(special_reservation1.save())
# special_reservation2 = SpecialReservation(room=room1, start_date=date(2021, 1, 10), end_date=date(2021, 1, 12))
# print(special_reservation2.save())
# print(special_reservation1.calculate_total_cost())
# print(special_reservation1.reservation_period())
# # Example of extending a SpecialReservation
# try:
#     special_reservation1.extend_reservation(5)
# except ValidationError as e:
#     print(e)
