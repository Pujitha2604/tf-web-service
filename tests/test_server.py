import unittest
from lambda_function import handler  # Adjust import according to your structure

class TestLambdaFunction(unittest.TestCase):
    def test_handler(self):
        event = {}
        context = {}
        response = handler(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], '"Hello World!"')

if __name__ == '__main__':
    unittest.main()
