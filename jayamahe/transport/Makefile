TAG = latest

build-image:
	docker build -t nameko/nameko-example-transport-j:$(TAG) ./transport-j

docker-tag:
	docker tag nameko/nameko-example-transport-j:$(TAG) \
	nameko/nameko-example-transport-j:$(TAG)

push-image:
	docker push nameko/nameko-example-transport-j:$(TAG)