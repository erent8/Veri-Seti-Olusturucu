from faker import Faker
import pandas as pd
import random

fake = Faker()
data = []

for _ in range(1000):
    data.append({
        "user_id": fake.uuid4(),
        "name": fake.name(),
        "signup_date": fake.date_this_decade(),
        "purchase_amount": round(random.uniform(10, 500), 2),
        "country": fake.country()
    })

df = pd.DataFrame(data)
df.to_csv("synthetic_users.csv", index=False)