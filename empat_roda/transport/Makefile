TAG = latest

build-image:
	docker build -t nameko/nameko-example-transport-er:$(TAG) ./transport-er

docker-tag:
	docker tag nameko/nameko-example-transport-er:$(TAG) \
	nameko/nameko-example-transport-er:$(TAG)

push-image:
	docker push nameko/nameko-example-transport-er:$(TAG)