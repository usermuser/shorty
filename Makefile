rm_none_images:
	docker rmi $(docker images -a|grep "<none>"|awk '$1=="<none>" {print $3}')

fresh_build:
	docker compose up -d --build

docker_down:
	docker compose down -v

tests:
	docker compose exec -it web pytest
