import unittest
from test import CreateContents

# get all tests from SearchProductTest and HomePageTest class
basic_page_create_test = unittest.TestLoader().loadTestsFromTestCase(CreateContents)

# Create test suite:
smoke_test = unittest.TestSuite(basic_page_create_test)

# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_test)