import random

def get_climate_data():
    # بيانات محاكاة (بدل NASA API لتبسيط المشروع)
    data = []

    for i in range(50):
        temp = random.randint(20, 50)
        humidity = random.randint(30, 90)

        data.append({
            "temp": temp,
            "humidity": humidity
        })

    return data