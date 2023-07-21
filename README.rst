=====
Maintenance
=====

Maintenance is a Django app to conduct sheduled maintenance.
Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "maintenance" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "maintenance",
    ]

2. Include the polls URLconf in your project urls.py like this::

    path("", include("maintenance.urls")),

3. Run ``python manage.py migrate`` to create the polls models.
