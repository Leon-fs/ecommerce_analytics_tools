import requests
import os

def download_data(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Data downloaded and saved to {save_path}")
    else:
        print(f"Failed to download data. Status code: {response.status_code}")

if __name__ == "__main__":
    # Example usage
    url = "https://example.com/data.csv"  # Replace with the actual URL
    save_path = os.path.join("data", "raw", "data.csv")  # Adjust the path as needed
    download_data(url, save_path)