TAG = latest

build-image:
	docker build -t nameko/nameko-example-transport-p:$(TAG) ./transport-p

docker-tag:
	docker tag nameko/nameko-example-transport-p:$(TAG) \
	nameko/nameko-example-transport-p:$(TAG)

push-image:
	docker push nameko/nameko-example-transport-p:$(TAG)