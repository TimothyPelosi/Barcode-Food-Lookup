import requests

# Get barcode from user.
def getBarcode():
    userInput = "076808003901" # input("Please enter a barcode: ")
    return userInput

# Get country code from user.
def getCountryCode():
    userInput = "world" # input("Please enter your country code or 'world': ")
    return userInput

# Make request to API for information based on country code and barcode.
def makeRequest(countryCode: str, barcode: int):
    response = requests.get(f"https://{countryCode}.openfoodfacts.org/api/v0/product/{barcode}.json")
    return response

# Print results of the barcode in readable format.
def printResults(productInfo):
    product = productInfo.json()
    print(f"Product name: {product['product']['product_name']}")
    print(f"Product barcode: {product['code']}")
    print(f"Product brand: {product['product']['brands']}")
    print(f"Generic name: {product['product']['generic_name']}")
    count = 1
    for ingredient in product['product']['ingredients']:
        print(f"{count}|Ingredient: {ingredient['text']}")
        count += 1
    

barcode = getBarcode()

countryCode = getCountryCode()

response = makeRequest(countryCode, barcode)

printResults(response)