# Dictionary mapping MCC-MNC codes to telecom providers
SIM_PROVIDERS = {
    "404-01": "Vodafone Idea", "404-02": "Airtel", "404-10": "Airtel",
    "404-11": "Vodafone", "404-20": "BSNL", "404-30": "Airtel",
    "404-56": "Idea", "404-70": "Reliance Jio", "405-799": "Reliance Jio"
}

# Recharge plans for major telecom providers
RECHARGE_PLANS = {
    "Airtel": ["₹179 - 28 Days, 2GB", "₹299 - 28 Days, 1.5GB/Day", "₹719 - 84 Days, 1.5GB/Day"],
    "Vodafone Idea": ["₹199 - 28 Days, 1GB/Day", "₹399 - 56 Days, 1.5GB/Day", "₹839 - 84 Days, 2GB/Day"],
    "Reliance Jio": ["₹209 - 28 Days, 1GB/Day", "₹399 - 56 Days, 1.5GB/Day", "₹666 - 84 Days, 2GB/Day"],
    "BSNL": ["₹147 - 30 Days, 10GB", "₹247 - 30 Days, 3GB/Day", "₹997 - 180 Days, 3GB/Day"]
}

def get_sim_provider(mcc, mnc):
    """Returns the SIM provider based on MCC-MNC"""
    key = f"{mcc}-{mnc}"
    return SIM_PROVIDERS.get(key, "Unknown Provider")

def get_recharge_plans(provider):
    """Returns available recharge plans for the provider"""
    return RECHARGE_PLANS.get(provider, ["No plans available"])

# Get MCC and MNC input
mcc = input("Enter MCC (e.g., 404): ")
mnc = input("Enter MNC (e.g., 10): ")

# Identify SIM provider
provider = get_sim_provider(mcc, mnc)
print(f"\nDetected SIM Provider: {provider}")

# Show recharge plans
print("\nAvailable Recharge Plans:")
for plan in get_recharge_plans(provider):
    print("-"+plan)
