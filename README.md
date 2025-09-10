Mevcut veri setinde eklenebilecek alanlar

Şu an elinde: user_id, name, signup_date, purchase_amount, country.
Bunları genişletmek için şunları ekleyebilirsin:
	•	Kişisel bilgiler
	•	email = fake.email()
	•	phone = fake.phone_number()
	•	birthdate = fake.date_of_birth(minimum_age=18, maximum_age=80)
	•	gender = random.choice(["Male", "Female", "Other"])
	•	Konum / adres bilgileri
	•	city = fake.city()
	•	address = fake.address()
	•	postcode = fake.postcode()
	•	latitude, longitude = fake.latitude(), fake.longitude()
	•	E-ticaret / finans verileri
	•	product = fake.word()
	•	payment_method = random.choice(["Credit Card", "PayPal", "Crypto"])
	•	transaction_id = fake.uuid4()
	•	currency = fake.currency_code()
	•	Web / teknoloji verileri
	•	ip_address = fake.ipv4()
	•	device = random.choice(["iOS", "Android", "Web"])
	•	browser = fake.user_agent()
	•	Davranışsal veriler
	•	last_login = fake.date_time_this_year()
	•	is_active = fake.boolean()
	•	loyalty_points = random.randint(0, 5000)

⸻

🔹 Daha farklı veri tipleri istersem?
	1.	Faker’in hazır metotlarını kullanabilirsin
👉 Faker docs içinde yüzlerce farklı veri tipi var (meslek, şirket, plaka, kredi kartı bilgisi, IBAN, renk, hatta lorem ipsum cümleleri bile).
	2.	Kendi custom veri tiplerini oluşturabilirsin
Örneğin:
***
favorite_genre = random.choice(["Rock", "Jazz", "HipHop", "Classical"])
subscription_plan = random.choice(["Free", "Premium", "Enterprise"])
***
    3.	Karma veri tipleri (nested JSON gibi)
Daha gerçekçi yapmak için iç içe yapılar ekleyebilirsin: