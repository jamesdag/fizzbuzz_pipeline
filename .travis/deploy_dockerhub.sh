#!/bin/sh
REPO_NAME=n0223109/fizzbuzz_pipeline
echo "$DOCKER_PASS" | docker login -u $DOCKER_USER --password-stdin

if [ "$TRAVIS_BRANCH" = "master" ]; then
  TAG="latest"
else
  TAG="$TRAVIS_BRANCH"
fi
docker build -f Dockerfile -t $REPO_NAME:$TAG .
docker push $REPO_NAME
