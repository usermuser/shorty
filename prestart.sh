echo "Waiting for postgres connection"

#проверка db на запуск каждые 0.1 секунды
while ! nc -z db 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

exec "$@"