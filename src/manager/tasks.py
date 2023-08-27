from time import sleep

from celery import shared_task

@shared_task(bind=True, max_retries=2)
def send_emails(self, seconds):
    try:
        int('a')
        sleep(seconds)
        print('!!!!!!!!!!!!!!!send_emails done')
        return 'result of send emails'
    except Exception as error:
        print(f'exeption - {error}')
        raise self.retry(countdown=10)


@shared_task
def hello():
    print('!!!!hello task!!!!')
    return 'result of send emails'