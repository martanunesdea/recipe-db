import requests
from bs4 import BeautifulSoup

def parse_website_instructions(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        instructions_element = soup.find(string=lambda text: text and 'ingredients' in text.lower())

        if instructions_element:
            # Find the parent element containing the instructions
            parent_element = instructions_element.find_parent()
            
            new_line = "\n\n\n"
            # Extract text until the end of the list
            instructions_text = ""

            for sibling in parent_element.find_next_siblings():
                if sibling.name == 'ul' or sibling.name == 'ol':
                    # If it's a list, parse until the end of the list
                    for li in sibling.find_all('li'):
                        instructions_text += li.get_text(strip=True) + new_line
                else:
                    # Otherwise, add the text to the instructions
                    instructions_text += sibling.get_text(strip=True) + new_line

            return instructions_text.strip()
        else:
            return "Instructions not found on the webpage."
    else:
        return f"Failed to fetch the webpage. Status code: {response.status_code}"

# Example usage
if __name__ == "__main__":
    # Replace 'https://example.com' with the actual URL of the website
    #website_url = 'https://www.bbcgoodfood.com/recipes/best-ever-macaroni-cheese-recipe'
    #website_url = 'https://www.bbcgoodfood.com/recipes/pan-fried-sea-bass-citrus-dressed-broccoli'
    #website_url = 'https://crumbsandcaramel.com/vegan-pesto-risotto-roasted-tomatoes-chickpeas/'
    website_url =  'https://www.olivemagazine.com/recipes/family/spinach-ricotta-and-pesto-lasagne/'
    instructions_text = parse_website_instructions(website_url)
    print(instructions_text)