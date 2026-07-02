from client import PricingTierAdvisorClient
def main():
    c = PricingTierAdvisorClient()
    print(c.recommend_tier(15000, 3))
if __name__ == '__main__':
    main()
