import requests
import time

URL = "http://localhost:5000/random-number"  # Change to your REST endpoint
N = 5  # Number of calls

def main():
    start = time.time()
    for i in range(N):
        response = requests.get(URL)
        data = response.json()
        print(f"Call {i+1}: {data}")
    elapsed = time.time() - start
    print(f"Total time elapsed: {elapsed:.2f} seconds")

if __name__ == "__main__":
    main()