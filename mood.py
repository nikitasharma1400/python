def analyze_vibe(message):
    score = 0
    
    if message.endswith('.') and len(message.split()) < 4:
        score += 50
        
    if "fine" in message.lower():
        score += 30
        
    if message.isupper():
        score += 40

    print(f"\nChecking message: '{message}'")
    
    if score >= 70:
        return " STATUS: High Alert. They are definitely mad."
    elif score >= 30:
        return " STATUS: Slightly salty. Proceed with caution."
    else:
        return " STATUS: All good! No hidden drama detected."

msg = input("Enter the text message you received: ")
print(analyze_vibe(msg))