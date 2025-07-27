
def extract_data():
    print("Extracting data...")
    data = [100,343,454,7678,4745]
    return data

def transform_data(data):
    print("Transforming data...")
    # Simple transformation: square each value
    transformed = [x ** 2 for x in data]
    return transformed

def load_data(transformed):
    print("Loading data...")
    # Simulate data load
    print("Transformed data loaded:", transformed)

def main():
    print("Databricks CI/CD Demo Pipeline")
    data = extract_data()
    transformed = transform_data(data)
    load_data(transformed)
    print("Pipeline completed successfully!")
    print("Raja Your Second Pipeline Successful")

if __name__ == "__main__":
    main()
