TAG = latest

build-image:
	docker build -t nameko/nameko-example-transport-ak:$(TAG) ./transport-ak

docker-tag:
	docker tag nameko/nameko-example-transport-ak:$(TAG) \
	nameko/nameko-example-transport-ak:$(TAG)

push-image:
	docker push nameko/nameko-example-transport-ak:$(TAG)