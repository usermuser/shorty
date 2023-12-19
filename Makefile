rm_none_images:
	docker rmi $(docker images -a|grep "<none>"|awk '$1=="<none>" {print $3}')

frash_build:
	docker compose up -d --build

tests:
	docker compose exec -it web pytest
