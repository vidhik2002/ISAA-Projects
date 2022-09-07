import cv2

IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

E = [32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25]

FP = [40, 8, 48, 16, 56, 24, 64, 32,
     39, 7, 47, 15, 55, 23, 63, 31,
     38, 6, 46, 14, 54, 22, 62, 30,
     37, 5, 45, 13, 53, 21, 61, 29,
     36, 4, 44, 12, 52, 20, 60, 28,
     35, 3, 43, 11, 51, 19, 59, 27,
     34, 2, 42, 10, 50, 18, 58, 26,
     33, 1, 41, 9, 49, 17, 57, 25]

S_Box = [
    
    [[14, 4, 13, 1, 2, 15,11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]], 
    
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]], 
    
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]], 
    
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

]

PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

PC_2 = [14, 17, 11, 24, 1, 5, 3, 28, 
        15, 6, 21, 10, 23, 19, 12, 4, 
        26, 8, 16, 7, 27, 20, 13, 2, 
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

Shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def string_to_binary(password):
    key = []
    for pwrd in password:
        bval = bin(ord(pwrd))[2:]
        while(len(bval) % 8 != 0):
            bval = "0" + bval
        for i in bval:
            key.append(int(i))
    return key

def binary_to_integer(bin_value):
    enc = ""
    for i in range(0,len(bin_value),8):
        bval = ""
        for j in range(8):
            bval = bval+str(bin_value[i+j])
        enc = enc+chr(int(bval,2))
    return enc    

def generate_key(key):
    roundkey = []
    key_p = []
    for i in PC_1:
        key_p.append(key[i-1])
        
    left = key_p[:28]
    right = key_p[28:]
        
    for count in range(16):
        for i in range(Shift[count]):
            l_key_p = left[1:]
            r_key_p = right[1:]
            l_key_p.append(left[0])
            r_key_p.append(right[0])
            left = l_key_p
            right = r_key_p
        key_p = []
        key_p_2 = []
        key_p = left+right        
        
        for i in PC_2:
            key_p_2.append(key_p[i-1])
            
        roundkey.append(key_p_2) 
    return roundkey
    
def DES(img,password,action = "encrypt"):
    if(len(password) < 8):
        print("Minimun len of Key is 8")
        exit()
    elif(len(password) > 8):
        password = password[:8]
    
    key = []
    
    key = string_to_binary(password)
    roundkey = generate_key(key)
    
    shape = img.shape
    
    for x in range(0,shape[0]):
        for y in range(0,shape[1],8):
            enc_text = []
            for k in range(8):
                bval = bin(img[x][y+k])[2:] 
                while(len(bval) % 8 != 0):
                    bval = "0" + bval
                for i in bval:
                    enc_text.append(int(i))

            enc_text_p = []
            key_p = []

            for i in IP:
                enc_text_p.append(enc_text[i-1])
            enc_text = enc_text_p

            l_text = enc_text[:32]
            r_text = enc_text[32:]

            for count in range(16):
                r_e = []

                for i in E:
                    r_e.append(r_text[i-1])

                if action == "encrypt":
                    key_p = roundkey[count]
                else:
                    key_p = roundkey[15-count]
                for i in range(len(r_e)):
                    r_e[i] = r_e[i] ^ key_p[i]

                key_p = []
                key_p_2 = []           

                for j in range(0,len(r_e),6):
                    key_p = r_e[j:j+8]
                    row = int(str(key_p[0])+str(key_p[5]),2)
                    col = int(str(key_p[1])+str(key_p[2])+str(key_p[3])+str(key_p[4]),2)
                    val = S_Box[int(j/6)][row][col]
                    bval = bin(val)[2:]
                    while(len(bval) % 4 != 0):
                        bval = "0" + bval
                    for i in bval:
                        key_p_2.append(int(i))

                r_e = []

                for i in P:
                    r_e.append(key_p_2[i-1])
                l_text_p = l_text    
                l_text = r_text
                r_text = []

                for i in range(len(r_e)):
                    r_text.append(l_text_p[i] ^ r_e[i])

            enc_text = []+r_text+l_text
            enc_text_p = []
            for i in FP:
                enc_text_p.append(enc_text[i-1])

            for i in range(0,len(enc_text_p),8):
                bval = ""
                for j in range(8):
                    bval = bval+str(enc_text_p[i+j])
                img[x][int(y+(i/8))] = int(bval,2)
        
    return img

if _name_ == '_main_':
    img = cv2.imread('D:\\Pictures\\vv.jpg',cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Original ",img)
    cv2.waitKey(0)
    shape = img.shape
    
    x = shape[0]
    x = x + (8 - (x%8))
    y = shape[1]
    y = y + (8 - (y%8))

    dim = (x,y)
    img = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)

    key = "DesCiphr"
    enc = DES(img,key,"encrypt")
    cv2.imshow("Encrypted ",enc)
    cv2.waitKey(0)
    
    dec = DES(enc,key,"decrypt")
    dec = cv2.resize(dec,shape,interpolation = cv2.INTER_AREA)
    cv2.imshow("Decrypted ",dec)
    cv2.waitKey(0)
    cv2.destroyAllWindows()