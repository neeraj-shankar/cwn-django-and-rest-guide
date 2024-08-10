"""
Certainly! Here are some interview questions based on Django ORM that are suitable for a developer with 4-5 years of experience:

### Basic Questions

1. **What is Django ORM and how does it work?**
   - Explain the concept of ORM and how Django's ORM maps models to database tables.

2. **How do you define a model in Django?**
   - Describe the process of creating a model and the different field types available.

3. **What is a QuerySet in Django?**
   - Explain what a QuerySet is and how it is used to retrieve data from the database.

4. **How do you create and apply migrations in Django?**
   - Describe the steps to create and apply migrations using `makemigrations` and `migrate`.

### Intermediate Questions

5. **How do you perform CRUD operations using Django ORM?**
   - Provide examples of how to create, read, update, and delete records using Django ORM.

6. **What are the different types of relationships in Django ORM?**
   - Explain one-to-one, one-to-many, and many-to-many relationships with examples.

7. **How do you filter and exclude records in Django ORM?**
   - Describe the use of `filter()`, `exclude()`, and other QuerySet methods for querying data.

8. **What is the purpose of the `on_delete` parameter in Django models?**
   - Explain the different options for the `on_delete` parameter and their use cases.

### Advanced Questions

9. **How do you perform complex queries using Django ORM?**
   - Discuss the use of `Q` objects, `F` expressions, and annotations for complex queries.

10. **What are Managers in Django and how do you use them?**
    - Explain the concept of Managers and how to create custom managers for models.

11. **How do you handle database transactions in Django?**
    - Describe the use of `transaction.atomic` and other transaction management techniques.

12. **What are the performance considerations when using Django ORM?**
    - Discuss techniques for optimizing database queries, such as select_related, prefetch_related, and indexing.

### Scenario-Based Questions

13. **How would you implement a many-to-many relationship with additional fields in Django?**
    - Provide an example of using a through model to add extra fields to a many-to-many relationship.

14. **How do you handle database migrations in a production environment?**
    - Discuss best practices for managing and applying migrations in a live application.

15. **How do you perform bulk operations in Django ORM?**
    - Explain the use of `bulk_create`, `bulk_update`, and other bulk operations.

16. **How do you handle database schema changes in Django?**
    - Describe the process of making schema changes and ensuring data integrity during migrations.

### Practical Questions

17. **Write a Django model for a blog application with authors, posts, and comments.**
    - Define models for `Author`, `Post`, and `Comment` with appropriate relationships.

18. **How would you retrieve all posts written by a specific author in the last 30 days?**
    - Write a QuerySet to filter posts based on the author and publication date.

19. **How do you implement soft deletion in Django?**
    - Describe a strategy for implementing soft deletion and provide a code example.

20. **How do you handle database constraints and validations in Django models?**
    - Explain the use of model field options, validators, and unique constraints.

### Behavioral Questions

21. **Describe a challenging problem you faced while working with Django ORM and how you solved it.**
    - Share a real-world example of a complex issue and your approach to resolving it.

22. **How do you stay updated with the latest features and best practices in Django?**
    - Discuss your methods for continuous learning and staying current with Django developments.

23. **How do you ensure code quality and maintainability in your Django projects?**
    - Explain your approach to writing clean, maintainable code and using tools like linters, code reviews, and testing.

24. **Can you describe a project where you extensively used Django ORM?**
    - Provide an overview of a project, highlighting how you used Django ORM to manage data and relationships.

These questions cover a range of topics and difficulty levels, providing a comprehensive assessment of a candidate's knowledge and experience

"""
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import status
from .models import Author, Book
import logging
from django.db.models.aggregates import Avg, Count
# Define a logging format that includes the date, time, level, function name, and the log message
LOG_FORMAT = "%(asctime)s - %(levelname)s - [%(funcName)s] - %(message)s"

# Configure logging with the specified format and the date format
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt="%Y-%m-%d %H:%M:%S")

# Get a logger instance with the specified name
logger = logging.getLogger(__name__)



# Create your views here.
class PracticeQueriesView(APIView):

    def get(self, request, format=None): 

        # Getting all books using a given author
        author = Author.objects.get(name="J.K. Rowling") 
        # Listing all books written a by a given author
        all_books = author.book_set.all()

        logger.info(f"Showing titel of the all retrieved books: ")
        for book in all_books:
            logger.info(f"{book.title}")

        # Annotate each author with the number of books they have written
        authors = Author.objects.annotate(book_count=Count('book'))
        logger.info(f"Author query set after annotation: {authors}")

        # Annotate each author with count and convert in dictionary
        authors = Author.objects.annotate(book_count=Count('book')).values()
        logger.info(f"Annotated author Queries after conversion to dictionary: {authors}")

        # for a in author:
        #     logging.info(f"Author name: {a.name}")

        SUCCESS_MESSAGE = {"message": "Connection to api is established"}
        return Response(SUCCESS_MESSAGE, status=status.HTTP_200_OK)