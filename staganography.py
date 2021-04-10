import cv2


def set_bit(value):
    return value | 1

def clear_bit(value):
    return value & ~1


def get_bit(value):
    return value%2



def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result


def frombits(bits):
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def encode(img, text):
    bit_count = 0
    string_bits = tobits(text)
    data_length = len(string_bits)


    shape = img.shape

    if len(shape) == 2:
        rows, columns = shape
        channels = 1
    elif len(shape) == 3:
        rows, columns, channels = shape
    
    for i in range(rows):
        for j in range(columns):
            for k in range(channels):
                if bit_count < data_length:
                    if string_bits[bit_count]:
                        img[i][j][k] = set_bit(img[i][j][k])
                    else:
                        img[i][j][k] = clear_bit(img[i][j][k])

                bit_count += 1

    return img


def decode(img, data_length):
    bit_list = []
    bit_count = 0

    shape = img.shape

    if len(shape) == 2:
        rows, columns = shape
        channels = 1
    elif len(shape) == 3:
        rows, columns, channels = shape

    for i in range(rows):
        for j in range(columns):
            for k in range(channels):
                if bit_count < data_length:
                    bit_list.append(get_bit(img[i][j][k]))
                bit_count += 1

    return frombits(bit_list)


def enconde_img(img1, img2):
    bits = 32

    shape = img1.shape

    if len(shape) == 2:
        rows, columns = shape
        channels = 1
    elif len(shape) == 3:
        rows, columns, channels = shape


    for i in range(rows):
        for j in range(columns):
            for k in range(channels):
                print("row: " + str(i))
                print("column: " + str(j))
                img1[i][j][k] = (img1[i][j][k]>>4<<4) + (img2[i][j][k]>>4)

    return img1


def decode_img(img):

    shape = img1.shape
    img2 = img.copy()

    if len(shape) == 2:
        rows, columns = shape
        channels = 1
    elif len(shape) == 3:
        rows, columns, channels = shape


    for i in range(rows):
        for j in range(columns):
            for k in range(channels):
                img2[i][j][k] = img1[i][j][k]<<4

    return img2





img_path_1 = "/Users/renanmaronni/Projects/steganografia-python/woman.png"
img_path_2 = "/Users/renanmaronni/Projects/steganografia-python/dog.png"
img_path_res = "/Users/renanmaronni/Projects/steganografia-python/res.png"
img_path_decoded = "/Users/renanmaronni/Projects/steganografia-python/decoded.png"

img1 = cv2.imread(img_path_1)
img2 = cv2.imread(img_path_2)

rows, columns, channel = img1.shape
print(img1.shape)



img_res = enconde_img(img1, img2)

cv2.imwrite(img_path_res, img_res)

img_decoded = decode_img(img_res)
cv2.imwrite(img_path_decoded, img_decoded)

