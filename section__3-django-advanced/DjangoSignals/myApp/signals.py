from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from .models import Book
from django.dispatch import Signal, receiver
from utils.loggers import setup_logger

logger = setup_logger(__name__)

@receiver(pre_save, sender=Book)
def update_information(sender, instance, **kwargs):
    logger.info("Pre save signal received and updating the actual data.")
    instance.name = "Corrupted Data"

# @receiver(post_save, sender=Book)
def information_message(sender, instance, created, **kwargs):
    """
    Signal triggered every time a Book instance is saved.
    Logs a message based on whether the book was created or updated.
    """

    logger.info(f"Singal is triggered........")
    if created:
        logger.info(f"New Book Added: {instance.name} which is written by {instance.author}")
    else:
        logger.info(f"New Book Updated: {instance.name} which is written by {instance.author}")

# Connecing the signal manually without using the decorator
post_save.connect(information_message, sender=Book)

# Signal to track books names to be deleted 
@receiver(pre_delete, sender=Book)
def pre_delete_signal(sender, instance, **kwargs):
    logger.warning(f"The request for deleting all books containing following name: {instance.name} ")
