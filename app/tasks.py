from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.utils.log import get_task_logger

from app.email import send_review_email

logger = get_task_logger(__name__)

@shared_task
def send_email_task(name, email, review):
    logger.info("send review email")
    return send_review_email(name, email, review)