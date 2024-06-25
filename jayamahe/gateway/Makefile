build-image:
	docker build -t nameko/nameko-example-gateway-j:$(TAG) ./gateway-j;

docker-tag:
	docker tag nameko/nameko-example-gateway-j:$(TAG) \
	nameko/nameko-example-gateway-j:$(TAG)

push-image:
	docker push nameko/nameko-example-gateway-j:$(TAG)