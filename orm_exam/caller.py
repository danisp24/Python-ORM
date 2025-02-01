import os
import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article


# Create and run your queries within functions


def get_authors(search_name=None, search_email=None):
    if search_name is not None and search_email is not None:
        authors = Author.objects.filter(full_name__icontains=search_name, email__icontains=search_email)
    elif search_name is not None:
        authors = Author.objects.filter(full_name__icontains=search_name)
    elif search_email is not None:
        authors = Author.objects.filter(email__icontains=search_email)
    else:
        return ""

    authors = authors.order_by('-full_name')  # Order authors by full name, descending

    if authors.exists():
        author_info = ""
        for author in authors:
            status = "Banned" if author.is_banned else "Not Banned"
            author_info += f"Author: {author.full_name}, email: {author.email}, status: {status}\n"
        return author_info.strip()
    else:
        return ""


def get_top_publisher():
    top_author = Author.objects.get_authors_by_article_count().first()

    num_of_articles = getattr(top_author, 'article_count', 0)
    if num_of_articles == 0:
        return ""

    return f"Top Author: {top_author.full_name} with {num_of_articles} published articles."


def get_top_reviewer():
    top_reviewer = Author.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews', 'email').first()

    num_of_reviews = getattr(top_reviewer, 'num_reviews', 0)
    if num_of_reviews == 0:
        return ''

    return f"Top Reviewer: {top_reviewer.full_name} with {num_of_reviews} published reviews."


def get_latest_article():
    latest_article = Article.objects.prefetch_related('authors').order_by('-published_on').first()
    if not latest_article:
        return ''
    authors = ', '.join(sorted([author.full_name for author in latest_article.authors.all()]))
    num_reviews = latest_article.review_set.count()
    if num_reviews > 0:
        average_rating = latest_article.review_set.aggregate(avg_rating=Avg('rating'))['avg_rating']

    else:
        average_rating = 0.00

    return (f"The latest article is: {latest_article.title}. "
            f"Authors: {authors}. "
            f"Reviewed: {num_reviews} times. Average Rating: {average_rating:.2f}.")


def get_top_rated_article():
    top_rated_articles = (Article.objects.filter(review__isnull=False).
                          annotate(avg_rating=Avg('review__rating')).
                          order_by('-avg_rating', 'title'))

    if top_rated_articles.exists():
        top_rated_article = top_rated_articles.first()

        num_reviews = top_rated_article.review_set.count() if top_rated_article.review_set.exists() else 0
        avg_rating = top_rated_article.avg_rating if num_reviews > 0 else 0.0

        return f"The top-rated article is: {top_rated_article.title}, with an average rating of {avg_rating:.2f}, reviewed {num_reviews} times."
    else:
        return ""


def ban_author(email=None):
    if email is None:
        return 'No authors banned.'

    try:
        banned_author = Author.objects.get(email__exact=email)
    except Author.DoesNotExist:
        return 'No authors banned.'

    if banned_author:
        number_of_reviews = banned_author.reviews.count()
        banned_author.is_banned = True
        banned_author.save()
        banned_author.reviews.all().delete()
        return f"Author: {banned_author.full_name} is banned! {number_of_reviews} reviews deleted."


