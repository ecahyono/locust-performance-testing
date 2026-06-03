from locust import HttpUser, task, between
from locust import events

@events.quitting.add_listener
def _(environment, **kw):
    print("Performance test completed")

class DummyJsonUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        payload = {
            "username": "emilys",
            "password": "emilyspass"
        }

        response = self.client.post("/auth/login", json=payload)

        if response.status_code == 200:
            self.token = response.json().get("accessToken")
        else:
            self.token = None

    @task(3)
    def get_products(self):
        self.client.get("/products")

    @task(2)
    def search_product(self):
        self.client.get("/products/search?q=phone")

    @task(1)
    def get_profile(self):
        if self.token:
            headers = {
                "Authorization": f"Bearer {self.token}"
            }
            self.client.get("/auth/me", headers=headers)