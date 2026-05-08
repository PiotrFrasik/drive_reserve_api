# Drive Reserve API

A Car Rental API built with **Django REST Framework**. This system manages vehicle fleets, secure user bookings, and a verified review system with data integrity at its core.

## Key Features

* Simple car management with automatic price calculations.
* Secure reservations that automatically prevent double-booking.
* Verified Reviews - only real customers can leave ratings and comments.
* Real-time average scores for every vehicle.
* Permission-based access and strict data validation.

## API Endpoints

| Endpoint           | Description                               |
|:-------------------|:------------------------------------------|
| `/api/cars/`       | List and manage the vehicle fleet         |
| `/api/bookings/`   | Handle user reservations and availability |
| `/api/reviews/`    | Verified customer feedback and ratings    |
| `/api/docs/`       | Swagger UI                                |
| `/api/schema/`     | Raw YAML/JSON                               |
| `/admin/`          | Secure administrative dashboard           |

## Quick Start

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver`