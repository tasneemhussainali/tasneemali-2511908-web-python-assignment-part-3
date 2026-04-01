#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write student notes to a file

with open("python_notes.txt", "w", encoding="utf-8") as file:
    file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
    file.write("Topic 2: Lists are ordered and mutable.\n")
    file.write("Topic 3: Dictionaries store key-value pairs.\n")
    file.write("Topic 4: Loops automate repetitive tasks.\n")
    file.write("Topic 5: Exception handling prevents crashes.\n")

print("Notes written to python_notes.txt successfully.")


# In[2]:


# Append two more topics to the same file

with open("python_notes.txt", "a", encoding="utf-8") as file:
    file.write("Topic 6: Functions help reuse code and improve readability.\n")
    file.write("Topic 7: File handling allows programs to read and write data.\n")

print("New topics appended successfully.")


# In[3]:


# Part A — Write
with open("python_notes.txt", "w", encoding="utf-8") as file:
    file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
    file.write("Topic 2: Lists are ordered and mutable.\n")
    file.write("Topic 3: Dictionaries store key-value pairs.\n")
    file.write("Topic 4: Loops automate repetitive tasks.\n")
    file.write("Topic 5: Exception handling prevents crashes.\n")

print("File written successfully.")

# Part B — Append
with open("python_notes.txt", "a", encoding="utf-8") as file:
    file.write("Topic 6: Functions help reuse code and improve readability.\n")
    file.write("Topic 7: File handling allows programs to read and write data.\n")

print("Lines appended.")


# In[4]:


# Read and print numbered lines
with open("python_notes.txt", "r", encoding="utf-8") as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip()}")


# In[6]:


# Count total number of lines
with open("python_notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))


# In[7]:


# Ask user for keyword and search in file (case-insensitive)

keyword = input("Enter keyword to search: ").lower()
found = False

with open("python_notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        if keyword in line.lower():
            print(line.strip())
            found = True

if not found:
    print("No lines found containing that keyword.")


# In[8]:


import requests

# Step 1 — Fetch 20 products
url = "https://dummyjson.com/products?limit=20"

response = requests.get(url)

# Convert response to JSON
data = response.json()

# Display products
products = data["products"]

for product in products:
    print(f"{product['id']}. {product['title']} - ${product['price']}")


# In[9]:


import requests

url = "https://dummyjson.com/products?limit=20"
response = requests.get(url)

# Parse JSON response
data = response.json()
products = data["products"]

# Display selected fields
for product in products:
    pid = product["id"]
    title = product["title"]
    category = product["category"]
    price = product["price"]
    rating = product["rating"]

    print(f"{pid}. {title}")
    print(f"   Category: {category}")
    print(f"   Price: ${price}")
    print(f"   Rating: {rating}")
    print()


# In[10]:


import requests

url = "https://dummyjson.com/products?limit=20"
response = requests.get(url)
data = response.json()

products = data["products"]

# Print table header
print(f"{'ID':<4}| {'Title':<30}| {'Category':<13}| {'Price':<9}| {'Rating'}")
print("-" * 75)

# Print rows
for p in products:
    print(f"{p['id']:<4}| "
          f"{p['title'][:30]:<30}| "
          f"{p['category']:<13}| "
          f"${p['price']:<8}| "
          f"{p['rating']}")


# In[11]:


import requests

url = "https://dummyjson.com/products?limit=20"
response = requests.get(url)
data = response.json()

products = data["products"]

# Filter products with rating >= 4.5
filtered_products = [p for p in products if p["rating"] >= 4.5]

# Print results
print("Products with rating >= 4.5:\n")

for p in filtered_products:
    print(f"{p['id']}. {p['title']} | Rating: {p['rating']}")


# In[12]:


import requests

url = "https://dummyjson.com/products?limit=20"
response = requests.get(url)
data = response.json()

products = data["products"]

# Filter rating >= 4.5
filtered_products = [p for p in products if p["rating"] >= 4.5]

# Sort by price (descending)
sorted_products = sorted(filtered_products, key=lambda x: x["price"], reverse=True)

# Print results
print("Filtered & Sorted (Rating ≥ 4.5, Price High → Low):\n")

for p in sorted_products:
    print(f"{p['id']}. {p['title']} | ${p['price']} | Rating: {p['rating']}")


# In[13]:


import requests

url = "https://dummyjson.com/products?limit=20"
response = requests.get(url)
data = response.json()

products = data["products"]

# Filter products with rating >= 4.5
filtered = [p for p in products if p["rating"] >= 4.5]

# Sort by price (descending)
filtered_sorted = sorted(filtered, key=lambda x: x["price"], reverse=True)

# Print formatted table
print(f"{'ID':<4}| {'Title':<30}| {'Category':<13}| {'Price':<9}| {'Rating'}")
print("-" * 75)

for p in filtered_sorted:
    print(f"{p['id']:<4}| "
          f"{p['title'][:30]:<30}| "
          f"{p['category']:<13}| "
          f"${p['price']:<8}| "
          f"{p['rating']}")


# In[14]:


import requests

url = "https://dummyjson.com/products/category/laptops"

response = requests.get(url)
data = response.json()

products = data["products"]

print("Laptops Category Products:\n")

for p in products:
    print(f"{p['id']}. {p['title']} | ${p['price']} | Rating: {p['rating']}")


# In[15]:


import requests

url = "https://dummyjson.com/products/category/laptops"

response = requests.get(url)
data = response.json()

laptops = data["products"]

print("Laptop Name and Price:\n")

for laptop in laptops:
    print(f"{laptop['title']} - ${laptop['price']}")


# In[16]:


import requests

url = "https://dummyjson.com/products/add"

# JSON body
new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

# Send POST request
response = requests.post(url, json=new_product)

# Parse response
data = response.json()

print("Product created successfully:\n")
print(f"ID: {data['id']}")
print(f"Title: {data['title']}")
print(f"Price: ${data['price']}")
print(f"Category: {data['category']}")
print(f"Description: {data['description']}")


# In[17]:


import requests

url = "https://dummyjson.com/products/add"

payload = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

response = requests.post(url, json=payload)

# Print full response JSON
print("Full response from server:\n")
print(response.json())


# In[18]:


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"


# Test cases
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))


# In[19]:


def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")


# Test cases
print(read_file_safe("python_notes.txt"))   # should succeed
print(read_file_safe("ghost_file.txt"))     # should fail gracefully


# In[20]:


import requests

# -------- GET Example --------
def fetch_products():
    url = "https://dummyjson.com/products?limit=20"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()   # handles HTTP errors like 404
        data = response.json()

        print("Products fetched successfully.\n")
        for p in data["products"]:
            print(f"{p['title']} - ${p['price']}")

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print(f"Error: {e}")


# -------- POST Example --------
def add_product():
    url = "https://dummyjson.com/products/add"

    payload = {
        "title": "My Custom Product",
        "price": 999,
        "category": "electronics",
        "description": "A product I created via API"
    }

    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        data = response.json()

        print("\nProduct added successfully:")
        print(data)

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print(f"Error: {e}")


# Run both
fetch_products()
add_product()


# In[21]:


import requests

while True:
    user_input = input("Enter a product ID to look up (1–100), or 'quit' to exit: ")

    # Exit condition
    if user_input.lower() == "quit":
        print("Exiting program.")
        break

    # Validate integer input
    if not user_input.isdigit():
        print("Invalid input. Please enter a number between 1 and 100.")
        continue

    product_id = int(user_input)

    # Validate range
    if not (1 <= product_id <= 100):
        print("Invalid range. Enter a number between 1 and 100.")
        continue

    url = f"https://dummyjson.com/products/{product_id}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 404:
            print("Product not found.")
        elif response.status_code == 200:
            product = response.json()
            print(f"Title: {product['title']}")
            print(f"Price: ${product['price']}")
        else:
            print(f"Unexpected status code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print(f"Error: {e}")


# In[22]:


import requests
from datetime import datetime


# Logger function
def log_error(function_name, error_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("error_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n")


# Example 1 — fetch products
def fetch_products():
    url = "https://dummyjson.com/products?limit=20"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.ConnectionError as e:
        print("Connection failed. Please check your internet.")
        log_error("fetch_products", "ConnectionError", str(e))

    except requests.exceptions.Timeout as e:
        print("Request timed out. Try again later.")
        log_error("fetch_products", "Timeout", str(e))

    except Exception as e:
        print(f"Error: {e}")
        log_error("fetch_products", type(e).__name__, str(e))


# Example 2 — lookup product
def lookup_product(product_id):
    url = f"https://dummyjson.com/products/{product_id}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 404:
            print("Product not found.")
            log_error(
                "lookup_product",
                "HTTPError",
                f"404 Not Found for product ID {product_id}"
            )
            return

        data = response.json()
        print(f"{data['title']} - ${data['price']}")

    except requests.exceptions.ConnectionError as e:
        print("Connection failed. Please check your internet.")
        log_error("lookup_product", "ConnectionError", str(e))

    except requests.exceptions.Timeout as e:
        print("Request timed out. Try again later.")
        log_error("lookup_product", "Timeout", str(e))

    except Exception as e:
        print(f"Error: {e}")
        log_error("lookup_product", type(e).__name__, str(e))


# Test calls
fetch_products()
lookup_product(999)   # will trigger 404


# In[26]:


from datetime import datetime

def log_error(function_name, error_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("error_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n")


# In[28]:


log_error(
    "fetch_products",
    "ConnectionError",
    "No connection could be made"
)

log_error(
    "lookup_product",
    "HTTPError",
    "404 Not Found for product ID 999"
)


# In[29]:


import requests
from datetime import datetime


# Logger
def log_error(function_name, error_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("error_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n")


# Trigger 1 — ConnectionError
def trigger_connection_error():
    url = "https://this-host-does-not-exist-xyz.com/api"

    try:
        requests.get(url, timeout=5)
    except requests.exceptions.ConnectionError as e:
        print("Connection failed. Please check your internet.")
        log_error("trigger_connection_error", "ConnectionError", str(e))


# Trigger 2 — HTTP 404 (not an exception)
def trigger_http_error():
    product_id = 999
    url = f"https://dummyjson.com/products/{product_id}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            print("Product not found.")
            log_error(
                "lookup_product",
                "HTTPError",
                f"{response.status_code} Not Found for product ID {product_id}"
            )

    except requests.exceptions.ConnectionError as e:
        print("Connection failed. Please check your internet.")
        log_error("lookup_product", "ConnectionError", str(e))
    except requests.exceptions.Timeout as e:
        print("Request timed out. Try again later.")
        log_error("lookup_product", "Timeout", str(e))


# Run both tests
trigger_connection_error()
trigger_http_error()


# In[30]:


import requests
from datetime import datetime


# Logger
def log_error(function_name, error_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("error_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n")


# Trigger ConnectionError
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except requests.exceptions.ConnectionError as e:
    print("Connection failed. Please check your internet.")
    log_error("fetch_products", "ConnectionError", str(e))


# Trigger HTTP 404
product_id = 999
response = requests.get(f"https://dummyjson.com/products/{product_id}", timeout=5)

if response.status_code != 200:
    print("Product not found.")
    log_error(
        "lookup_product",
        "HTTPError",
        f"{response.status_code} Not Found for product ID {product_id}"
    )


# Read and print log file
print("\nContents of error_log.txt:\n")

with open("error_log.txt", "r", encoding="utf-8") as file:
    print(file.read())

