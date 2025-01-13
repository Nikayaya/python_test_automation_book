# 1 Write a TestCase class with methods for setup(), run(), and teardown(). Create objects of the TestCase class to represent individual test cases.
class TestCase:
    # Constructor of the class
    def __init__(self, name):
        self.name = name  # Attribute/Property/State

    def setup(self):
        print(f"Set up the test environment: {self.name}.")

    def run(self): # Method/Behaviour
        print(f"Running test case: {self.name}.")

    def teardown(self):
        print(f"Act of tearing test case: {self.name}")

test = TestCase("Test")
test1 = TestCase("Test1")

test.setup()
test.run()
test.teardown()

test1.setup()
test1.run()
test1.teardown()


#2 Implement method overriding in a test automation context. Override a method in the child test class to customize the test execution.
class BaseCase:

    def setup(self):
        print("Set up BaseCase")

    def run(self): # Method/Behaviour
        print("Running BaseCase")

    def teardown(self):
        print("Teardown BaseCase")

class ChildCase(BaseCase):
    def run(self):
        print("Running Override test - Child Case")

testCase = ChildCase()


testCase.setup() #--> inherit from parent
testCase.run()  #--> override
testCase.teardown() #--> inherit from parent


#Create a multiple inheritance example: Write a class that inherits from multiple parent classes (e.g., BaseTest and a custom mixin class), and check how MRO impacts method calls.

class BaseTest:
    def setup(self):
        print("Setting up the BaseTest.")

    def run(self):
        print("Running the BaseTest.")

    def teardown(self):
        print("Tearing down the BaseTest.")

class CustomMixin:
    def setup(self):
        print("Setting up the CustomMixin.")

class TestCase(CustomMixin,BaseTest):
    def run(self):
        print("Running the inherited test.")

TestCase = TestCase()

TestCase.run() # -->>Running the inherited test.
TestCase.setup() #-->> Setting up the CustomMixin.
TestCase.teardown() # -->>Tearing down the BaseTest


