## Build and run the app

From your project directory, start up your application by running

```bash
docker-compose up
```

for celery 

```
celery worker -B -l info --app src.task.app
```
