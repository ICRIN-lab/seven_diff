import os

L = ['img_9_1.png', 'img_17_5.png', 'img_11_3.png', 'img_13_1.png', 'img_13_0.png', 'img_11_2.png', 'img_9_0.png', 'img_15_4.png', 'img_9_2.png', 'img_11_0.png', 'img_13_2.png', 'img_11_1.png', 'img_9_3.png', 'img_15_1.png', 'img_17_3.png', 'img_11_5.png', 'img_17_2.png', 'img_15_0.png', 'img_15_2.png', 'img_17_0.png', 'img_9_4.png', 'img_13_4.png', 'img_13_5.png', 'img_17_1.png', 'img_15_3.png', 'img_10_0.png', 'img_8_2.png', 'img_16_6.png', 'img_14_4.png', 'img_8_3.png', 'img_10_1.png', 'img_12_3.png', 'img_12_1.png', 'img_8_1.png', 'img_16_5.png', 'img_8_0.png', 'img_10_2.png', 'img_12_0.png', 'img_12_4.png', 'img_10_6.png', 'img_16_0.png', 'img_14_2.png', 'img_14_3.png', 'img_8_5.png', 'img_16_1.png', 'img_14_1.png', 'img_14_0.png', 'img_16_2.png', 'img_10_4.png', 'img_12_6.png', 'img_2_0.png', 'img_0_2.png', 'img_18_0.png', 'img_6_4.png', 'img_4_6.png', 'img_18_1.png', 'img_0_3.png', 'img_2_1.png', 'img_2_3.png', 'img_18_2.png', 'img_0_0.png', 'img_2_2.png', 'img_0_4.png', 'img_6_2.png', 'img_4_0.png', 'img_4_1.png', 'img_6_3.png', 'img_0_5.png', 'img_2_5.png', 'img_6_1.png', 'img_18_5.png', 'img_4_3.png', 'img_4_2.png', 'img_18_4.png', 'img_6_0.png', 'img_5_5.png', 'img_1_1.png', 'img_3_3.png', 'img_3_2.png', 'img_1_0.png', 'img_7_6.png', 'img_19_2.png', 'img_5_4.png', 'img_19_0.png', 'img_7_4.png', 'img_1_2.png', 'img_3_0.png', 'img_3_1.png', 'img_1_3.png', 'img_7_5.png', 'img_19_1.png', 'img_5_3.png', 'img_19_5.png', 'img_3_4.png', 'img_1_6.png', 'img_19_4.png', 'img_7_0.png', 'img_5_2.png', 'img_5_0.png', 'img_7_2.png']

calligraphy = []
chess = []
img = []
# create a random list from calligraphy and chess separately
for elt in os.listdir('img/'):
    print(elt)
    print(elt[4:elt.find("_", 4)])
    if 30 < int(elt[4:elt.find("_", 4)]):
        img.append(elt)
    print("---------")
print(img)
print(len(img))

# rename pictures
'''for elt in L:
    if elt[4:6] != "10":  # to make sure we are not facing a three digits number
        new_elt = elt[0:4] + str(int(elt[4:6]) - 1) + elt[6:]
    else:
        print("yoh", elt[4:7])
        new_elt = elt[0:4] + str(int(elt[4:7]) - 1) + elt[7:]
        print(new_elt)
    os.rename('temp/' + elt, 'temp/' + new_elt)
'''