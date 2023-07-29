import random
import os

def generate_background():
  """Generates a random background image for a landing page."""
  image_path = os.path.join("images", random.choice(["flower.jpg", "mountains.jpg", "city.jpg"]))
  with open(image_path, "rb") as f:
    image = f.read()
  return image

def create_landing_page(image):
  """Creates a landing page with the given image as a background."""
  with open("index.html", "w") as f:
    f.write("""
    <!DOCTYPE html>
    <html>
      <head>
        <title>My Landing Page</title>
        <style>
          body {
            background-image: url(data:image/png;base64,{});
          }
        </style>
      </head>
      <body>
        <h1>My Landing Page</h1>
        <p>This is my landing page.</p>
      </body>
    </html>
    """.format(base64.b64encode(image).decode()))

if __name__ == "__main__":
  image = generate_background()
  create_landing_page(image)