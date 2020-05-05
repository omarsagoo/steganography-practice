from PIL import Image, ImageDraw

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

def encode_image(text, image_path):
    image = Image.open(image_path)
    pixels = image.load()

    x_size = image.size[0]
    y_size = image.size[1]

    create_encode_image = write_text(text, (x_size,y_size))
    create_red_channel = create_encode_image.split()[0]

    for i in range(x_size):
        for j in range(y_size):
            read_pixel = create_red_channel.getpixel((i,j))

            if (pixels[i,j][0] | 1) == pixels[i,j][0]:
                pixels[i,j] = (pixels[i,j][0] + 1, pixels[i,j][1], pixels[i,j][2])
            
            if read_pixel == 0:
                pix = pixels[i,j]
                pix = (pix[0] + 1, pix[1], pix[2])
                pixels[i,j] = pix


    image.save("new_encoded_image.png")
                
    

def write_text(text, size):
    image = Image.new("RGB", size, (255,255,255))
    
    draw = ImageDraw.Draw(image)
    draw.text((20,20), text, fill=(0,0,0))

    image.save("encode_image.png", "png")
    return image

if __name__ == "__main__":
    # decode_image("images/encoded_sample.png")
    # encode_image("hello world! I hid this text in this image!!!!!", "images/images.jpeg")
    decode_image("new_encoded_image.png")

