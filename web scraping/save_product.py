import json
import os

working_directory = os.getcwd()
web_scraping_folder = os.path.join(working_directory, "web_scraping")
products_folder = os.path.join(web_scraping_folder, "products")


def save_product(product):
    # create products folder
    if not os.path.exists(products_folder):
        os.mkdir(products_folder)

    # product json file path
    product_title = product['title'].replace("/", "").replace(" ", "")
    product_json_file = os.path.join(
        products_folder,
        f"{product_title}.json"
    )

    # create json file
    with open(product_json_file, 'w') as json_file:
        product_string = json.dumps(product)
        json_file.write(product_string)
        print(f"[+] {product['title']}.json has been created!")