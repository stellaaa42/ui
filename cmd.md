CMD
run env:
    source env/bin/activate
run django:
    python manage.py runserver
run nuxt:
    npm run dev

sqlite3 db.sqlite3:
    .tables
    SELECT * FROM api_item;
    .exit
    cp db.sqlite3 db_backup.sqlite3

django:
    rm -rf api/migrations/__pycache__
    rm api/migrations/00*.py
    python manage.py makemigrations
    python migrate
    pip list
    python manage.py shell:
        from api.models import Area
        areas = Area.objects.all()
        items = Item.objects.all()
        print(areas)
        Area.objects.create(name="One room", description="Small area, 20 sqm")
        Area.objects.create(name="Two rooms", description="Medium area, 40 sqm")
        Area.objects.create(name="Three or More rooms", description="Large area, 60 sqm+")
        Area.objects.all().values()




