from django.core.exceptions import ValidationError


def validate_menu_categories(value):

    #  value ni referira kum poleto na koeto zadavame validatora
    # naprimer tuk validirme dali v poleto 'description' na class 'Menu' ima sledniq tekst

    categories = ["Appetizers", "Main Course", "Desserts"]
    for category in categories:
        if category.lower() not in value.lower():
            raise ValidationError(
                f'The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')
