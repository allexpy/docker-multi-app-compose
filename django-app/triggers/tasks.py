import time
from celery import shared_task


@shared_task
def test_task(num=10):
    time.sleep(num)
    print(f'Waited {num} seconds...')
