from client import RealtimeCustomerSupportHandoffAgentClient

def main():
    client = RealtimeCustomerSupportHandoffAgentClient()
    res1 = client.handle_support("How do I change my profile email address?", "standard")
    print(f"Query 1 -> Escalate: {res1['escalate_to_human']} | {res1['resolution']}")

    res2 = client.handle_support("Billing dispute for high enterprise invoice", "enterprise_vip")
    print(f"Query 2 -> Escalate: {res2['escalate_to_human']} | {res2['resolution']}")

if __name__ == "__main__":
    main()
