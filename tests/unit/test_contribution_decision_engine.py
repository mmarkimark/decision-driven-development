import unittest
from datetime import date
from uuid import uuid4
from src.domain.models.investment_plan import InvestmentPlan
from src.domain.value_objects.decision_date import DecisionDate
from src.domain.value_objects.sma_value import SMAValue
from src.domain.value_objects.drawdown import Drawdown
from src.domain.services.contribution_decision_engine import ContributionDecisionEngine

class TestContributionDecisionEngine(unittest.TestCase):
    def setUp(self):
        self.plan = InvestmentPlan(
            id=uuid4(),
            asset_symbol="BTC",
            base_contribution_amount=100.0,
            is_active=True
        )
        self.decision_date = DecisionDate(date(2023, 10, 27))

    def test_base_execution_missing_data(self):
        decision = ContributionDecisionEngine.calculate(
            self.plan, self.decision_date, 30000.0, None, None
        )
        self.assertEqual(decision.total_amount, 100.0)
        self.assertEqual(decision.reinforcement_amount, 0.0)
        self.assertIn("Missing market data", decision.reason)

    def test_no_reinforcement_price_above_sma(self):
        decision = ContributionDecisionEngine.calculate(
            self.plan, self.decision_date,
            current_price=31000.0,
            sma_200=SMAValue(30000.0),
            drawdown=Drawdown(-20.0)
        )
        self.assertEqual(decision.total_amount, 100.0)
        self.assertEqual(decision.reinforcement_amount, 0.0)

    def test_no_reinforcement_small_drawdown(self):
        decision = ContributionDecisionEngine.calculate(
            self.plan, self.decision_date,
            current_price=29000.0,
            sma_200=SMAValue(30000.0),
            drawdown=Drawdown(-10.0)
        )
        self.assertEqual(decision.total_amount, 100.0)
        self.assertEqual(decision.reinforcement_amount, 0.0)

    def test_reinforcement_tier_1(self):
        # Drawdown -15% to -25% -> 1.5x (100 base + 50 reinforcement)
        decision = ContributionDecisionEngine.calculate(
            self.plan, self.decision_date,
            current_price=29000.0,
            sma_200=SMAValue(30000.0),
            drawdown=Drawdown(-20.0)
        )
        self.assertEqual(decision.total_amount, 150.0)
        self.assertEqual(decision.reinforcement_amount, 50.0)
        self.assertIn("Reinforcement (Drawdown -15% to -25%)", decision.reason)

    def test_reinforcement_tier_2(self):
        # Drawdown <= -25% -> 2.0x (100 base + 100 reinforcement)
        decision = ContributionDecisionEngine.calculate(
            self.plan, self.decision_date,
            current_price=29000.0,
            sma_200=SMAValue(30000.0),
            drawdown=Drawdown(-30.0)
        )
        self.assertEqual(decision.total_amount, 200.0)
        self.assertEqual(decision.reinforcement_amount, 100.0)
        self.assertIn("Reinforcement (Drawdown <= -25%)", decision.reason)

    def test_reinforcement_boundary_15(self):
        # -15% exactly -> 1.5x
        decision = ContributionDecisionEngine.calculate(
            self.plan, self.decision_date,
            current_price=29000.0,
            sma_200=SMAValue(30000.0),
            drawdown=Drawdown(-15.0)
        )
        # Wait, condition was: drawdown <= -15%.
        # Logic:
        # > -15% -> 1.0
        # -15% to -25% -> 1.5
        # So -15.0 falls into "to -25%" bucket? Or "> -15%"?
        # Prompt: "drawdown <= -15%" triggers reinforcement.
        # Prompt Scaling: "> -15% -> 1.0", "-15% to -25% -> 1.5".
        # So -15.0 is included in 1.5.
        self.assertEqual(decision.total_amount, 150.0)

if __name__ == '__main__':
    unittest.main()
