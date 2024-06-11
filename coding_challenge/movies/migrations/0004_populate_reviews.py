
from django.db import migrations

def populate_reviews(apps, schema_editor):
    Review = apps.get_model("movies", "Review")
    Movie = apps.get_model("movies", "Movie")
    db_alias = schema_editor.connection.alias

    reviews_data = [
        {"movie_title": "Forrest Gump", "name": "Reviewer 1", "rating": 4},
        {"movie_title": "Forrest Gump", "name": "Reviewer 2", "rating": 5},
        {"movie_title": "Toy Story", "name": "Reviewer 3", "rating": 4},
        {"movie_title": "Toy Story", "name": "Reviewer 4", "rating": 5},
        {"movie_title": "Captain Phillips", "name": "Reviewer 5", "rating": 3},
        {"movie_title": "Captain Phillips", "name": "Reviewer 6", "rating": 2},
        {"movie_title": "Catch Me If You Can", "name": "Reviewer 7", "rating": 2},
        {"movie_title": "Catch Me If You Can", "name": "Reviewer 8", "rating": 4},
        {"movie_title": "Catch Me If You Can", "name": "Reviewer 9", "rating": 2},
        {"movie_title": "Bridge of Spies", "name": "Reviewer 10", "rating": 4},
        {"movie_title": "Bridge of Spies", "name": "Reviewer 11", "rating": 4},
    ]

    for review_data in reviews_data:
        movie_title = review_data.pop("movie_title")
        movie = Movie.objects.using(db_alias).get(title=movie_title)
        Review.objects.using(db_alias).create(movie=movie, **review_data)

def empty_reviews(apps, schema_editor):
    Review = apps.get_model("movies", "Review")
    db_alias = schema_editor.connection.alias

    Review.objects.using(db_alias).all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_review"), 
    ]

    operations = [
        migrations.RunPython(populate_reviews, empty_reviews),
    ]
