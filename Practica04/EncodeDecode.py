import base64

def decode_message(encoded_message):
    message_bytes = base64.b64decode(encoded_message)
    return message_bytes.decode()

def decode_image():
    with open('mystery_img1.txt', 'rb') as image_file:
        image_data = image_file.read()
        decoded_data = base64.decodebytes(image_data)
        with open('decoded_image.png', 'wb') as decoded_image:
            decoded_image.write(decoded_data)

def encode_image():
    with open('uanl.png', 'rb') as original_image:
        image_data = original_image.read()
        encoded_data = base64.b64encode(image_data)
        encoded_info = encoded_data.decode('utf-8')
        print(encoded_info)

with open('encoded_msg.b64', 'r') as encoded_file:
    encoded_message = encoded_file.readlines()

decoded_message = decode_message(' '.join(encoded_message))
encode_image()
decode_image()
print(decoded_message)

