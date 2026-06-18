"""
Freemium — first N units are free, overage delegated to another strategy.

This is a great example of COMPOSITION: Freemium HAS-A inner PricingStrategy
rather than IS-A specific kind of pricing.

Example: 1000 free API calls per month, then ₹0.50 per call (UsageBased).
"""

from billing_engine.money import Money
from billing_engine.pricing.base import PricingStrategy


class Freemium(PricingStrategy):
 raise NotImplementedError("Day 1: implement Freemium.__init__")
        if free_quota < 0:
            raise ValueError("free_quota cannot be negative")

        if not isinstance(overage_strategy, PricingStrategy):
            raise TypeError("overage_strategy must be a PricingStrategy")

        self.free_quota = free_quota
        self.overage_strategy = overage_strategy
