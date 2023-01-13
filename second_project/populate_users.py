import os
from faker import Faker
import django

# FAKE POP SCRIPT
fakegen = Faker()


def populate(n=5):
    for entry in range(n):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # New entry
        user = User.objects.get_or_create(
            first_name=fake_first_name, last_name=fake_last_name, email=fake_email
        )[0]


if __name__ == "__main__":
    print("Populating databases!")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "second_project.settings")
    # Allow us to actually go in and populate the database.
    django.setup()

    from second_app.models import User

    populate(20)
    print("Populating complete!")
