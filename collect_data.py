import requests
from bs4 import BeautifulSoup

# Fetch the content from the URL
url = "https://brainlox.com/courses/category/technical"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract text from the HTML
Documents = soup.get_text()

# Print first 1000 characters to check
print(Documents[:1000])

# Save to a text file
file_path = "brainlox_courses.txt"
with open(file_path, "w", encoding="utf-8") as file:
    file.write(Documents)

print(f"Text saved to {file_path}")
