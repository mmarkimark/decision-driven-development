from datetime import date
from typing import List, Optional
import calendar
from src.domain.value_objects.decision_date import DecisionDate

class Scheduler:
    def __init__(self, execution_day: int = 1):
        self.execution_day = execution_day

    def is_due(self, current_date: date) -> bool:
        """
        Determines if a decision should be made on the current date.
        Simplistic monthly scheduler: triggers on the 'execution_day' of the month.
        Handles end-of-month logic: if execution_day > days in month, trigger on last day.
        """
        days_in_month = calendar.monthrange(current_date.year, current_date.month)[1]

        target_day = self.execution_day
        if target_day > days_in_month:
            target_day = days_in_month

        return current_date.day == target_day

    def get_next_execution_date(self, current_date: date) -> DecisionDate:
        """
        Calculates the next execution date.
        """
        year = current_date.year
        month = current_date.month + 1
        if month > 12:
            month = 1
            year += 1

        try:
            next_date = date(year, month, self.execution_day)
        except ValueError:
            # Handle short months (e.g. execution_day=31, next month is Feb)
            last_day = calendar.monthrange(year, month)[1]
            next_date = date(year, month, last_day)

        return DecisionDate(next_date)
