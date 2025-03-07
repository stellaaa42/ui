curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "test1", "password": "your_password"}' \
  -c cookies.txt -v

python manage.py shell:
    from api.models import Area
    print(Area.objects.all().values())
    Area.objects.create(name="One room", description="Small area, 20 sqm")

curl -X POST http://127.0.0.1:8000/api/book/ -H "Content-Type: application/json" \
    -d'{
        "name": "John Doe",
        "email": "john@example.com",
        "address": "123 Main St",
        "service": 3,
        "area": 2,
        "appointment_date": "2025-03-15",
        "appointment_time": "14:00",
        "payment_method": "paypal"
    }'

env:
    source env/bin/activate
npm:
    npm run dev
    rm -rf .nuxt node_modules package-lock.json
django:
    python manage.py runserver
    python manage.py showmigrations
    rm -rf api/migrations/__pycache__
    rm -rf api/migrations/00*.py
    python manage.py migrate auth zero
    touch api/migrations/__init__.py

    python manage.py makemigrations
    python migrate
sqlite3 shell:
    rm db.sqlite3
    sqlite3 db.sqlite3
    .tables
    SELECT * FROM api_item;
    .exit
    cp db.sqlite3 db_backup.sqlite3




