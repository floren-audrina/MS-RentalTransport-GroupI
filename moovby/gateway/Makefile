build-image:
	docker build -t nameko/nameko-example-gateway-m:$(TAG) ./gateway-m;

docker-tag:
	docker tag nameko/nameko-example-gateway-m:$(TAG) \
	nameko/nameko-example-gateway-m:$(TAG)

push-image:
	docker push nameko/nameko-example-gateway-m:$(TAG)