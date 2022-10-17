from bs4 import BeautifulSoup

# Get HTML file
with open("website.html", encoding="utf-8") as file:
    contents = file.read()

# Create BS4 Soup
soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)

# Show entire html file
# print(soup.prettify())

# Find all tags by name (or any element)
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# Get all anchor tags
for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

# Find specific elements with specific id
heading = soup.find(name="h1", id="name")
# print(heading)

# Find element based on class
section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.name)

# Get an element's class
# print(section_heading.get("class"))

# Getting specific selectors
company_url = soup.select_one(selector="p a")
# print(company_url)

# Get list of classes
headings_list = soup.select(".heading")
print(headings_list)
