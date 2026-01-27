from src.domain.models.investment_plan import InvestmentPlan
from src.domain.models.monthly_decision import MonthlyDecision
from src.domain.value_objects.contribution_amount import ContributionAmount
from src.domain.value_objects.drawdown import Drawdown
from src.domain.value_objects.sma_value import SMAValue
from src.domain.value_objects.decision_date import DecisionDate
from typing import Optional

class ContributionDecisionEngine:
    @staticmethod
    def calculate(
        plan: InvestmentPlan,
        decision_date: DecisionDate,
        current_price: float,
        sma_200: Optional[SMAValue],
        drawdown: Optional[Drawdown]
    ) -> MonthlyDecision:

        base_amount = ContributionAmount(plan.base_contribution_amount)
        reinforcement_amount = ContributionAmount(0.0)
        reason = "Base contribution execution"

        if sma_200 is None or drawdown is None:
            return MonthlyDecision(
                plan_id=plan.id,
                decision_date=decision_date.value,
                total_amount=base_amount.value,
                base_amount=base_amount.value,
                reinforcement_amount=0.0,
                reason=reason + " (Missing market data)"
            )

        # Logic:
        # Reinforcement only if price < SMA200 AND drawdown <= -15%
        if current_price < sma_200.value and drawdown.value <= -15.0:
            multiplier = 0.0

            # Scaling:
            # -15% to -25% -> 1.5x P
            # <= -25% -> 2.0x P
            # Wait, prompt says:
            # > -15% -> 1.0 (This implies no reinforcement, handled by default)
            # -15% to -25% -> 1.5
            # <= -25% -> 2.0

            if -25.0 < drawdown.value <= -15.0:
                multiplier = 0.5 # Total 1.5x means 1.0 base + 0.5 reinforcement
                reason = "Reinforcement (Drawdown -15% to -25%)"
            elif drawdown.value <= -25.0:
                multiplier = 1.0 # Total 2.0x means 1.0 base + 1.0 reinforcement
                reason = "Reinforcement (Drawdown <= -25%)"

            reinforcement_amount = base_amount * multiplier

        total_amount = base_amount + reinforcement_amount

        return MonthlyDecision(
            plan_id=plan.id,
            decision_date=decision_date.value,
            total_amount=total_amount.value,
            base_amount=base_amount.value,
            reinforcement_amount=reinforcement_amount.value,
            reason=reason
        )
