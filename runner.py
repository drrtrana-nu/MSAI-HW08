import unittest
from tests import test_bst

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_bst))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
result.stop()