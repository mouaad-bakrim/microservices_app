#!/bin/bash
echo "🧪 Running Django tests..."
docker-compose exec auth_service python manage.py test
docker-compose exec achat_service python manage.py test
docker-compose exec vente_service python manage.py test
