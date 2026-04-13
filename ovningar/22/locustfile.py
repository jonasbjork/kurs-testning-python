from locust import HttpUser, task, between


class BookApiUser(HttpUser):
    """Simulerar en användare av bok-API:t."""
    wait_time = between(1, 3)

    @task(5)
    def list_books(self):
        self.client.get("/api/books")

    @task(3)
    def get_one_book(self):
        self.client.get("/api/books/1")

    @task(1)
    def create_book(self):
        self.client.post("/api/books", json={
            "title": "Testbok",
            "author": "Locust"
        })
