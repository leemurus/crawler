from core.celery import celery_app


@celery_app.task
def add(x, y):
    print(x, y)

    import time
    time.sleep(5)

    return x + y
