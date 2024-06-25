TAG = latest

build-image:
	docker build -t nameko/nameko-example-transport-m:$(TAG) ./transport-m

docker-tag:
	docker tag nameko/nameko-example-transport-m:$(TAG) \
	nameko/nameko-example-transport-m:$(TAG)

push-image:
	docker push nameko/nameko-example-transport-m:$(TAG)