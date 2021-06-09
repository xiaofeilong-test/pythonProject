# from locust import HttpLocust, TaskSet, task
#
# class TsetIndex(TaskSet):
#     @task(1)
#     def baidu(self):
#         self.client.get("/")
#
#
# class WebSite(HttpLocust):
#     task_set = TsetIndex
#     min_wait = 1000
#     max_wait = 2000


from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.post(
            "/login", {
                "username":"test",
                "password":"3456"
            })
    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.get("/about/")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://debugtalk.com"
    min_wait =1000
    max_wait =5000