import os
from decimal import Decimal

import django
from django.db.models import Sum, F, Q

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct


# Create and check models
def add_records_to_database():
    # Categories
    food_category = Category.objects.create(name='Food')
    drinks_category = (Category.objects.create(name='Drinks'))


    # Food
    product1 = Product.objects.create(name='Pizza', description='Delicious pizza with toppings', price=10.99,
                                      category=food_category, is_available=False)
    product2 = Product.objects.create(name='Burger', description='Classic burger with cheese and fries', price=7.99,
                                      category=food_category, is_available=False)
    product3 = Product.objects.create(name='Apples', description='A bag of juicy red apples', price=3.99,
                                      category=food_category, is_available=True)
    product4 = Product.objects.create(name='Bread', description='A freshly baked loaf of bread', price=2.49,
                                      category=food_category, is_available=True)
    product5 = Product.objects.create(name='Pasta and Sauce Bundle',
                                      description='Package containing pasta and a jar of pasta sauce', price=6.99,
                                      category=food_category, is_available=False)
    product6 = Product.objects.create(name='Tomatoes', description='A bundle of ripe, red tomatoes', price=2.99,
                                      category=food_category, is_available=True)
    product7 = Product.objects.create(name='Carton of Eggs', description='A carton containing a dozen fresh eggs',
                                      price=3.49, category=food_category, is_available=True)
    product8 = Product.objects.create(name='Cheddar Cheese', description='A block of aged cheddar cheese', price=7.99,
                                      category=food_category, is_available=False)
    product9 = Product.objects.create(name='Milk', description='A gallon of fresh cow milk', price=3.49,
                                      category=food_category, is_available=True)

    # Drinks
    product10 = Product.objects.create(name='Coca Cola', description='Refreshing cola drink', price=1.99,
                                       category=drinks_category, is_available=True)
    product11 = Product.objects.create(name='Orange Juice', description='Freshly squeezed orange juice', price=2.49,
                                       category=drinks_category, is_available=False)
    product12 = Product.objects.create(name='Bottled Water', description='A 12-pack of purified bottled water',
                                       price=4.99, category=drinks_category, is_available=True)
    product13 = Product.objects.create(name='Orange Soda', description='A 6-pack of carbonated orange soda', price=5.49,
                                       category=drinks_category, is_available=True)
    product14 = Product.objects.create(name='Bottled Green Tea', description='A bottled green tea', price=3.99,
                                       category=drinks_category, is_available=False)
    product15 = Product.objects.create(name='Beer', description='A bottled craft beer', price=5.49,
                                       category=drinks_category, is_available=True)

    # Customers
    customer1 = Customer.objects.create(username='john_doe')
    customer2 = Customer.objects.create(username='alex_alex')
    customer3 = Customer.objects.create(username='peter132')
    customer4 = Customer.objects.create(username='k.k.')
    customer5 = Customer.objects.create(username='peter_smith')

    # Orders
    order1 = Order.objects.create(customer=customer1)
    order_product1 = OrderProduct.objects.create(order=order1, product=product3, quantity=2)
    order_product2 = OrderProduct.objects.create(order=order1, product=product6, quantity=1)
    order_product3 = OrderProduct.objects.create(order=order1, product=product7, quantity=5)
    order_product4 = OrderProduct.objects.create(order=order1, product=product13, quantity=1)

    order2 = Order.objects.create(customer=customer3)
    order_product5 = OrderProduct.objects.create(order=order2, product=product3, quantity=2)
    order_product6 = OrderProduct.objects.create(order=order2, product=product9, quantity=1)

    order3 = Order.objects.create(customer=customer1)
    order_product5 = OrderProduct.objects.create(order=order3, product=product12, quantity=4)
    order_product6 = OrderProduct.objects.create(order=order3, product=product7, quantity=3)
    return "All data entered!"


# Run and print your queries
# print(add_records_to_database())

# print('All Products:')
# print(Product.objects.all())
# print()
# print('All Available Products:')
# print(Product.objects.available_products())
# print()
# print('All Available Food Products:')
# print(Product.objects.available_products_in_category("Food"))


def product_quantity_ordered():
    total_quantity_ordered = Product.objects.annotate(
        total_ordered_quantity=Sum('orderproduct__quantity')
    ).exclude(
        total_ordered_quantity=None
    ).order_by('-total_ordered_quantity')
    # print(total_quantity_ordered)
    result = []
    for product in total_quantity_ordered:
        result.append(f'Quantity ordered of {product.name}: {product.total_ordered_quantity}')

    return '\n'.join(result)

product_quantity_ordered()

# 2ri variant
# def product_quantity_ordered():
#     ordered_products = (
#         OrderProduct.objects
#         .values('product__name')
#         .annotate(total_ordered_quantity=Sum('quantity'))
#         .order_by('-total_ordered_quantity')
#     )
#
#     summary_text = ""
#     for product_data in ordered_products:
#         product_name = product_data['product__name']
#         total_quantity = product_data['total_ordered_quantity']
#         summary_text += f"Quantity ordered of {product_name}: {total_quantity}\n"
#
#     return summary_text
#
# print(product_quantity_ordered())


def ordered_products_per_customer():
    orders = Order.objects.prefetch_related('orderproduct_set__product__category',)
    result = []
    for order in orders:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}\n")

        for product in order.products.all():
            result.append(f"- Product: {product.name}, Category: {product.category.name}\n")

    return ''.join(result)
#
# print(ordered_products_per_customer())

#
# def ordered_products_per_customer():
#     orders = Order.objects.order_by('id')  # Retrieve orders in ascending order by ID
#     result = ""
#
#     for order in orders:
#         result += f"Order ID: {order.id}, Customer: {order.customer.username}\n"
#         order_products = OrderProduct.objects.filter(order=order)
#
#         products_info = []
#         for order_product in order_products:
#             product = order_product.product
#             product_info = f"- Product: {product.name}, Category: {product.category.name}\n"
#             products_info.append(product_info)
#
#         result += "".join(products_info)
#
#     return result
# #
# print(ordered_products_per_customer())


# def filter_products():
#
#     products = (Product.objects.filter(price__gt=3.00,is_available=True).order_by('-price', 'name'))
#     result = []
#     for product in products:
#         result.append(f'{product.name}: {product.price}lv.')
#
#
#     return '\n'.join(result)

#
# def filter_products():
#     products = Product.objects.filter(Q(price__gt=3.00) & Q(is_available=True)).order_by('-price', 'name')
#     result = []
#
#     for product in products:
#         result.append(f'{product.name}: {product.price}lv.')
#
#     return '\n'.join(result)
#
# print(filter_products())


# def give_discount():
#     discounted_products = Product.objects.filter(Q(is_available=True) & Q(price__gt=2.00)).order_by('-price', 'name')
#
#     result = []
#     for product in discounted_products:
#         product.price = product.price * Decimal(0.7)  # Apply 30% discount using F()
#
#         result.append(f"{product.name}: {product.price:.2f}lv.")
#
#
#     return '\n'.join(result)

def give_discount():
    products = Product.objects.filter(Q(price__gt=3) & Q(is_available=True)).order_by('-price', 'name')
    products.update(price=F('price') * 0.7)
    result = []
    for product in Product.objects.filter(is_available=True).order_by('-price', 'name'):
        result.append(f'{product.name}: {product.price}lv.')
    return '\n'.join(result)

print(give_discount())