After registering and setting your password, you can use these endpoints:

To get the auth token:
curl -X POST -H "Content-Type: application/json" -d '{"username": "<email>", "password": "<password>"}' http://ma.rcosbartolo.me/testlivesmart/api-token-auth/

To get (GET) or create (POST) your resolutions the enpoint is http://ma.rcosbartolo.me/testlivesmart/api/resolutions/

To update (PUT) or delete (DELETE) a resolution you can use http://ma.rcosbartolo.me/testlivesmart/api/resolutions/<id>/
