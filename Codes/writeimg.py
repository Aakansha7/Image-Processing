from PIL import Image, ImageDraw

# Open an image file (you can replace 'input_image.jpg' with your image file)
input_image = Image.open(r'C:\VSCode\Images\image10.jpg')

# Create a drawing object
draw = ImageDraw.Draw(input_image)

# Specify the position where you want to write the text (x, y)
text_position = (180, 20)

# Text to write on the image
text = "Hello World!"

# Write the text on the image
draw.text(text_position, text)

# Save the modified image (you can replace 'output_image.jpg' with your desired output filename)
input_image.save('output_image.jpg')

# Close the image
input_image.close()