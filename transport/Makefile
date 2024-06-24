TAG = latest

build-image:
	docker build -t nameko/nameko-example-transport:$(TAG) ./transport

docker-tag:
	docker tag nameko/nameko-example-transport:$(TAG) \
	nameko/nameko-example-transport:$(TAG)

push-image:
	docker push nameko/nameko-example-transport:$(TAG)