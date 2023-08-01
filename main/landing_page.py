import random
import os

def generate_landing_page():
  title = "Welcome to our digital storefront!"
  products = ["Product 1", "Product 2", "Product 3"]
  prices = [100, 200, 300]
  images = ["product1.jpg", "product2.jpg", "product3.jpg"]

  landing_page = """
<html>
<head>
<title>{title}</title>
</head>
<body>
<h1>{title}</h1>

<ul>
{products}
</ul>

<ul>
{prices}
</ul>

<ul>
{images}
</ul>

</body>
</html>
""".format(
    title=title,
    products="<li>{}</li>".format(product) for product in products,
    prices="<li>${}</li>".format(price) for price in prices,
    images="<li><img src='{}'></li>".format(image) for image in images,
  )

  return landing_page

def main():
  landing_page = generate_landing_page()
  print(landing_page)

if __name__ == "__main__":
  main()