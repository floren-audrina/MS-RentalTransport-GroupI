build-image:
	docker build -t nameko/nameko-example-gateway-p:$(TAG) ./gateway-p;

docker-tag:
	docker tag nameko/nameko-example-gateway-p:$(TAG) \
	nameko/nameko-example-gateway-p:$(TAG)

push-image:
	docker push nameko/nameko-example-gateway-p:$(TAG)