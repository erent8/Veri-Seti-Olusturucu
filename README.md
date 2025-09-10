## 📊 Veri Seti Genişletme Önerileri

Mevcut veri setinde aşağıdaki alanlar bulunuyor:

- `user_id`
- `name`
- `signup_date`
- `purchase_amount`
- `country`

Bunları daha zengin hale getirmek için aşağıdaki ek alanları kullanabilirsin:

---

### 🧍 Kişisel Bilgiler
- `email = fake.email()`
- `phone = fake.phone_number()`
- `birthdate = fake.date_of_birth(minimum_age=18, maximum_age=80)`
- `gender = random.choice(["Male", "Female", "Other"])`

---

### 🌍 Konum / Adres Bilgileri
- `city = fake.city()`
- `address = fake.address()`
- `postcode = fake.postcode()`
- `latitude, longitude = fake.latitude(), fake.longitude()`

---

### 🛒 E-Ticaret / Finans Verileri
- `product = fake.word()`
- `payment_method = random.choice(["Credit Card", "PayPal", "Crypto"])`
- `transaction_id = fake.uuid4()`
- `currency = fake.currency_code()`

---

### 💻 Web / Teknoloji Verileri
- `ip_address = fake.ipv4()`
- `device = random.choice(["iOS", "Android", "Web"])`
- `browser = fake.user_agent()`

---

### 📈 Davranışsal Veriler
- `last_login = fake.date_time_this_year()`
- `is_active = fake.boolean()`
- `loyalty_points = random.randint(0, 5000)`

---

## 🔹 Daha Farklı Veri Tipleri İstersen?

1. **Faker’in hazır metotlarını kullanabilirsin**  
👉 [Faker Docs](https://faker.readthedocs.io/en/master/) içinde yüzlerce farklı veri tipi mevcut (meslek, şirket, plaka, kredi kartı bilgisi, IBAN, renk, hatta lorem ipsum cümleleri bile).

2. **Kendi custom veri tiplerini oluşturabilirsin**  
Örneğin:
```python
favorite_genre = random.choice(["Rock", "Jazz", "HipHop", "Classical"])
subscription_plan = random.choice(["Free", "Premium", "Enterprise"])