# test_repository.py
import pytest
import os
from repository import BookRepository


@pytest.fixture
def repo(tmp_path):
    """Skapa ett repository med en temporär databas."""
    db_path = str(tmp_path / "test_books.db")
    repository = BookRepository(db_path)
    yield repository

