import faker
import pandas as pd
import sys

faker = faker.Faker()

health_conditions = [
    '34.0', 'E11.9', 'I10', 'J45.909', 'M54.5', 'F32.9', 'E78.5', 'G43.909', 'K21.9', 'N39.0'
]

data = {
    'name': [faker.name() for _ in range(50000)],
    'age': [faker.random_int(min=18, max=80) for _ in range(50000)],
    'address': [faker.address() for _ in range(50000)],
    'primary_condition': [faker.random_element(health_conditions) for _ in range(50000)],
}

df = pd.DataFrame(data)

## get size of df in megabytes
size_in_mb = sys.getsizeof(df) / (1024 * 1024)
print(f"DataFrame size: {size_in_mb:.2f} MB")

df.to_csv('fake_patient_data.csv', index=False)