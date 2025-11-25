
class APIBase:
    def api_auth(self):
        print("Authentication API")

class DBBase:
    def db_connect (self):
        print("Connecting to DB")
class TestHybrid(APIBase, DBBase):
    def run(self):

        self.api_auth()
        self.db_connect()
        print("Testcase Running")

test_hybrid = TestHybrid()
test_hybrid.run()