import pandas as pd
from datetime import datetime

# Custom FAQ for Phone Shop
faqs = {
    "iphone": "iPhone available: iPhone 11 - K6,500, iPhone 13 - K9,500, iPhone 14 - K11,000. All boxed with warranty.",
    "samsung": "Samsung: A14 - K3,200, A32 - K4,500, S22 - K8,500. Come with charger.",
    "tecno infinix": "Yes, Tecno & Infinix from K1,800 - K4,000. New stock every Monday.",
    "price": "Prices from K1,800 to K11,000. Tell me which model you want for exact price.",
    "screen guard pouch cover": "Yes, accessories available: Screen guards K100, Pouches K150-K300, Chargers K200, Cables K100.",
    "location": "We are at Cairo Road, Lusaka, opposite Main Post Office, Shop #12.",
    "delivery": "Yes! We deliver within Lusaka - K50, outside Lusaka - K120 via courier. Pay on delivery.",
    "hours": "Open Mon-Sat 08:30-19:00, Sunday 09:00-14:00.",
    "warranty": "All phones have 6 months warranty. Accessories 1 month."
}

inquiries_log = []

print("TechZone Phone Shop Bot")
print("Hello! Welcome to TechZone. How can I help you? (iPhone price, screen guard, location)")
print("Type 'bye' to exit\n")

while True:
    user_q = input("Customer: ").lower()
    if user_q == 'bye':
        break
    
    found = False
    for keyword, answer in faqs.items():
        # check if any word in keyword is in user question
        if any(word in user_q for word in keyword.split()):
            print(f"Bot: {answer}")
            inquiries_log.append([datetime.now().strftime("%Y-%m-%d %H:%M"), user_q, answer, "Auto-answered"])
            found = True
            break
            
    if not found:
        print("Bot: Thanks! I have forwarded your request to our sales team. They will reply in 5 mins.")
        inquiries_log.append([datetime.now().strftime("%Y-%m-%d %H:%M"), user_q, "Complex query", "Human needed"])

# Auto-save to Excel - This is your automation!
df = pd.DataFrame(inquiries_log, columns=["Time", "Customer Question", "Bot Answer", "Status"])
df.to_excel(r"c:\Users\lemmy\Desktop\TechZone_Inquiries.xlsx", index=False)
print("\n--- Report Saved: TechZone_Inquiries.xlsx ---")
print(f"Total inquiries logged: {len(inquiries_log)}")