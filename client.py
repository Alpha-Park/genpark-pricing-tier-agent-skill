from typing import Dict, Any

class PricingTierAdvisorClient:
    def recommend_tier(self, api_queries: int, user_seats: int) -> Dict[str, Any]:
        if api_queries > 50000 or user_seats > 20:
            tier = "Enterprise"
            price = 499.0
        elif api_queries > 10000 or user_seats > 5:
            tier = "Professional"
            price = 99.0
        elif api_queries > 1000:
            tier = "Starter"
            price = 29.0
        else:
            tier = "Free"
            price = 0.0
        return {"recommended_tier": tier, "monthly_base_price": price}
