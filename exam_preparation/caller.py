import os
import django
from django.db.models import Q, Count, F, Case, When

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from django.db.models import Q, Count
from main_app.models import Profile, Product, Order


# Create and run your queries within functions


def get_profiles(search_string: str = None):
    result = []
    if search_string is None:
        return ""
    profiles = Profile.objects.filter(Q(full_name__icontains=search_string) |
                                      Q(email__icontains=search_string) |
                                      Q(phone_number__icontains=search_string)).order_by('full_name')

    for profile in profiles:
        result.append(f"Profile: {profile.full_name}, email: {profile.email}, "
                      f"phone number: {profile.phone_number}, orders: {profile.orders.count()}")
    return '\n'.join(result)


def get_loyal_profiles():
    loyal_profiles = Profile.objects.get_regular_customers()
    if loyal_profiles is None:
        return ''
    result = []
    for profile in loyal_profiles:
        result.append(f"Profile: {profile.full_name}, orders: {profile.orders.count()}")

    return '\n'.join(result)


def get_last_sold_products():
    latest_order = Order.objects.order_by('-creation_date').first()
    if latest_order is None or not latest_order.products.exists():
        return ''
    products = latest_order.products.order_by('name')
    product_names = [product.name for product in products]

    return f"Last sold products: " + ", ".join(product_names)


def get_top_products() -> str:
    top_products = Product.objects.annotate(
        orders_count=Count('order')
    ).filter(
        orders_count__gt=0
    ).order_by(
        '-orders_count',
        'name'
    )[:5]

    if not top_products:
        return ""

    product_lines = [f"{p.name}, sold {p.orders_count} times" for p in top_products]

    return f"Top products:\n" + "\n".join(product_lines)


def apply_discounts():
    affected_orders = Order.objects.annotate(num_products=Count('products')).filter(
        num_products__gt=2, is_completed=False
    )

    num_of_updated_orders = affected_orders.update(
        total_price=F('total_price') * 0.9
    )

    return f"Discount applied to {num_of_updated_orders} orders."


def complete_order():
    oldest_order = Order.objects.filter(is_completed=False).order_by('creation_date').first()

    if oldest_order:

        oldest_order.is_completed = True
        oldest_order.save()

        for product in oldest_order.products.all():
            product.in_stock -= 1
            if product.in_stock == 0:
                product.is_available = False
            product.save()

        return "Order has been completed!"
    else:

        return ""
