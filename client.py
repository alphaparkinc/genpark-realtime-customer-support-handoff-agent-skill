class RealtimeCustomerSupportHandoffAgentClient:
    def handle_support(self, customer_query: str, account_tier: str = "standard") -> dict:
        q = customer_query.lower()
        if "billing dispute" in q or "refund > $1000" in q or account_tier == "enterprise_vip":
            return {
                "resolution": "Escalating to senior human support agent with full ticket context.",
                "escalate_to_human": True,
                "agent_confidence": 0.45
            }
        return {
            "resolution": "Resolved automatically: Provided self-service link to password reset.",
            "escalate_to_human": False,
            "agent_confidence": 0.98
        }
