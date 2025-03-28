curl:
    curl -X GET http://localhost:8000/api/sub -c cookies.txt
    curl -X POST
    -H "Content-Type: application/json" \

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

    python manage.py shell
    from api.models import EmailVerify

    entries = EmailVerify.objects.filter(email='xx')

    for entry in entries:
        print(f" - ID: {e.id}, Token: {e.token}, Created at: {e.created_at}")
        
        print(f"Deleting entry ID: {entry.id} | {entry.email}")
        entry.delete()

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




