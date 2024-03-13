"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""

import unittest
from counter import Counter


class TestCounterSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        # Create two instances of Counter
        counter1 = Counter()
        counter2 = Counter()

        # Verify that both instances are the same
        self.assertNotEqual(counter1, Counter)
        self.assertNotEqual(counter2, Counter)
        self.assertIs(counter1, counter2)

    def test_shared_count(self):
        # Create two instances of Counter
        counter1 = Counter()
        counter2 = Counter()

        # Increment count using one instance
        counter1.increment()

        # Verify that count is shared between instances
        self.assertEqual(counter1.count, counter2.count)

        # Increment count using one instance
        counter2.increment()

        # Verify that count is shared between instances
        self.assertEqual(counter1.count, counter2.count)

    def test_count_not_reset(self):
        # Create an instance of Counter and increment count
        counter1 = Counter()
        counter1.increment()

        # Create another instance of Counter
        counter2 = Counter()

        # Verify that count is not reset to 0
        self.assertNotEqual(counter2.count, 0)
