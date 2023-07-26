=====
dj_maintenance
=====

Django_maintenance is a Django app to conduct sheduled maintenance on your web application.
Detailed documentation is in the "docs" directory.

Installation
--------------

.. start installation

``dj_maintenance`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install dj_maintenance

.. end installation

1. Add "django_maintenance" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "dj_maintenance",
    ]

2. Add maintenance_mode variable to base or settings::

    MAINTENANCE_MODE = bool(os.getenv('MAINTENANCE_MODE'))

3. Update the URLconf in your project urls.py like this::

    if base.MAINTENANCE_MODE:
        path("", include("dj_maintenance.urls")),
    else:
        # All project URLconf
    # static URLconf
    # others ..

4. Run ``python manage.py migrate`` to create the polls models.
