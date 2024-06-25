build-image:
	docker build -t nameko/nameko-example-gateway-er:$(TAG) ./gateway-er;

docker-tag:
	docker tag nameko/nameko-example-gateway-er:$(TAG) \
	nameko/nameko-example-gateway-er:$(TAG)

push-image:
	docker push nameko/nameko-example-gateway-er:$(TAG)