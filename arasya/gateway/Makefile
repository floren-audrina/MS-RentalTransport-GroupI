build-image:
	docker build -t nameko/nameko-example-gateway-a:$(TAG) ./gateway-a;

docker-tag:
	docker tag nameko/nameko-example-gateway-a:$(TAG) \
	nameko/nameko-example-gateway-a:$(TAG)

push-image:
	docker push nameko/nameko-example-gateway-a:$(TAG)