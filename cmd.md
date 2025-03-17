curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMjE2MDI3LCJpYXQiOjE3NDIyMTU3MjcsImp0aSI6Ijg0Yzg0NTcyM2NhYjQxOTliYTcyYmI1ZDI3N2FiYjMyIiwidXNlcl9pZCI6MX0.hSXorscsoKUdX21hBSJHNlo0GWpbUNXsVprslrEBL2s" \
  -d '{ "action": "logout" }' \
  http://localhost:3000/api/auth/logout
  
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "test1", "password": "your_password"}' \
  -c cookies.txt -v

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
    rm -rf .nuxt node_modules package-lock.json
    npx nuxi cleanup
    npm install
    ls -la .nuxt
    npx nuxi prepare
    npm run dev --verbose
django:
    rm -rf api/migrations/__pycache__
    rm -rf api/migrations/00*.py
    touch api/migrations/__init__.py

    python manage.py flush
    python manage.py migrate auth zero
    
    python manage.py showmigrations
    python manage.py makemigrations api
    python migrate
    python manage.py runserver --verbose
sqlite3:
    rm db.sqlite3
    sqlite3 shell
    sqlite3 db.sqlite3
    .tables
    SELECT * FROM api_item;
    .exit
    cp db.sqlite3 db_backup.sqlite3

python manage.py shell:
    from api.models import Area
    print(Area.objects.all().values())
    Area.objects.create(name="One room", description="Small area, 20 sqm")




