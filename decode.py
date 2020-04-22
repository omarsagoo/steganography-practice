from PIL import Image 

from PIL import Image 
def decode_image(file_location):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            pixel = red_channel.getpixel((i,j))
            if (pixel | 1) == pixel:
                pixels[i,j] = (0,0,0)
            else:
                pixels[i,j] = (255,255,255)

    decoded_image.save("images/decoded_image.png")

if __name__ == "__main__":
    decode_image("images/encoded_sample.png")
