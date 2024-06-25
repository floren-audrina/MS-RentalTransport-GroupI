build-image:
	docker build -t nameko/nameko-example-gateway-ak:$(TAG) ./gateway-ak;

docker-tag:
	docker tag nameko/nameko-example-gateway-ak:$(TAG) \
	nameko/nameko-example-gateway-ak:$(TAG)

push-image:
	docker push nameko/nameko-example-gateway-ak:$(TAG)