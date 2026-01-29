import unittest
from datetime import date
from src.application.schedulers.scheduler import Scheduler

class TestScheduler(unittest.TestCase):
    def test_is_due(self):
        scheduler = Scheduler(execution_day=1)
        self.assertTrue(scheduler.is_due(date(2023, 10, 1)))
        self.assertFalse(scheduler.is_due(date(2023, 10, 2)))

    def test_is_due_end_of_month(self):
        # Scenario: execution_day is 31, but month is Feb (28 days)
        scheduler = Scheduler(execution_day=31)
        # Should trigger on Feb 28th
        self.assertTrue(scheduler.is_due(date(2023, 2, 28)))
        # Should trigger on Jan 31st
        self.assertTrue(scheduler.is_due(date(2023, 1, 31)))
        # Should NOT trigger on Jan 30th
        self.assertFalse(scheduler.is_due(date(2023, 1, 30)))

    def test_get_next_execution_date_simple(self):
        scheduler = Scheduler(execution_day=15)
        next_date = scheduler.get_next_execution_date(date(2023, 10, 15)).value
        self.assertEqual(next_date, date(2023, 11, 15))

    def test_get_next_execution_date_year_rollover(self):
        scheduler = Scheduler(execution_day=1)
        next_date = scheduler.get_next_execution_date(date(2023, 12, 1)).value
        self.assertEqual(next_date, date(2024, 1, 1))

    def test_get_next_execution_date_short_month(self):
        # Jan 31 -> Feb 28/29
        scheduler = Scheduler(execution_day=31)
        # 2024 is leap year
        next_date = scheduler.get_next_execution_date(date(2024, 1, 31)).value
        self.assertEqual(next_date, date(2024, 2, 29))

if __name__ == '__main__':
    unittest.main()
