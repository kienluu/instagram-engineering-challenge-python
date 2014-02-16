import unittest

testsuite = unittest.TestLoader().discover('.')

unittest.TextTestRunner(failfast=True).run(testsuite)