TAG = latest

build-image:
	docker build -t nameko/nameko-example-transport-a:$(TAG) ./transport-a

docker-tag:
	docker tag nameko/nameko-example-transport-a:$(TAG) \
	nameko/nameko-example-transport-a:$(TAG)

push-image:
	docker push nameko/nameko-example-transport-a:$(TAG)