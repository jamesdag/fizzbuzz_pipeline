#!/bin/sh
heroku container:login
echo "$HEROKU_API_KEY" | docker login --username=_ --password-stdin registry.heroku.com
heroku container:push web --app $HEROKU_APP_NAME
heroku container:release web --app $HEROKU_APP_NAME
