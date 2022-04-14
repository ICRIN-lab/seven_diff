import os

L = ['img_51_1.png', 'img_51_6.png', 'img_52_1.png', 'img_52_3.png', 'img_53_1.png', 'img_53_6.png', 'img_54_3.png',
     'img_54_6.png', 'img_55_2.png', 'img_55_5.png', 'img_56_2.png', 'img_56_5.png', 'img_57_1.png', 'img_57_6.png',
     'img_58_3.png', 'img_58_4.png', 'img_59_2.png', 'img_59_5.png', 'img_60_3.png', 'img_60_4.png', 'img_61_3.png',
     'img_61_4.png', 'img_62_3.png', 'img_62_4.png', 'img_63_2.png', 'img_63_5.png', 'img_64_1.png', 'img_64_5.png',
     'img_65_0.png', 'img_65_6.png', 'img_66_0.png', 'img_66_4.png', 'img_67_2.png', 'img_67_3.png', 'img_68_0.png',
     'img_68_3.png', 'img_69_2.png', 'img_69_4.png', 'img_70_0.png', 'img_70_1.png', 'img_71_1.png', 'img_71_3.png',
     'img_72_1.png', 'img_72_2.png', 'img_73_0.png', 'img_73_2.png', 'img_74_0.png', 'img_74_1.png', 'img_75_1.png',
     'img_75_3.png']
calligraphy = []
chess = []

# create a random list from calligraphy and chess separately
for elt in os.listdir('temp/'):
    if 50 <= int(elt[4:4 + elt[4:].find("_")]) <= 75:
        calligraphy.append(elt)
    elif int(elt[4:4 + elt[4:].find("_")]) >= 76:
        chess.append(elt)
print(calligraphy)
print(chess)

# rename pictures
for elt in L:
    if elt[4:6] != "10":  # to make sure we are not facing a three digits number
        new_elt = elt[0:4] + str(int(elt[4:6]) - 1) + elt[6:]
    else:
        print("yoh", elt[4:7])
        new_elt = elt[0:4] + str(int(elt[4:7]) - 1) + elt[7:]
        print(new_elt)
    os.rename('temp/' + elt, 'temp/' + new_elt)
