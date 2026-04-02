# tests/performance_tests.py

from locust import HttpUser, task, between
import json

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    
    @task(1)
    def view_homepage(self):
        self.client.get("/")
    
    @task(2)
    def view_majors(self):
        self.client.get("/majors/")
    
    @task(3)
    def take_test(self):
        login_data = {
            "username": "testuser",
            "password": "testpass123"
        }
        self.client.post("/accounts/login/", login_data)
        
        self.client.get("/tests/")
    
    @task(1)
    def api_endpoints(self):
        headers = {
            "Authorization": "Bearer testtoken",
            "Content-Type": "application/json"
        }
        
        self.client.get("/api/majors/", headers=headers)
        
        chat_data = {
            "message": "اختبار الأداء"
        }
        self.client.post("/api/chat/", 
                        json.dumps(chat_data), 
                        headers=headers)