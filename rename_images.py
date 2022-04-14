import os

L = ['img_76_5.png', 'img_96_0.png', 'img_94_0.png', 'img_90_4.png', 'img_89_4.png', 'img_94_5.png', 'img_89_0.png', 'img_90_0.png', 'img_92_0.png', 'img_92_1.png', 'img_96_5.png', 'img_76_0.png', 'img_97_3.png', 'img_95_3.png', 'img_97_1.png', 'img_77_5.png', 'img_95_2.png', 'img_91_6.png', 'img_93_0.png', 'img_88_3.png', 'img_88_2.png', 'img_100_6.png', 'img_100_4.png', 'img_93_3.png', 'img_77_3.png', 'img_91_0.png', 'img_84_1.png', 'img_80_4.png', 'img_84_2.png', 'img_82_5.png', 'img_86_5.png', 'img_99_2.png', 'img_79_6.png', 'img_82_0.png', 'img_80_0.png', 'img_86_6.png', 'img_79_5.png', 'img_99_0.png', 'img_85_2.png', 'img_87_0.png', 'img_78_3.png', 'img_87_3.png', 'img_81_4.png', 'img_98_5.png', 'img_98_1.png', 'img_83_3.png', 'img_81_1.png', 'img_83_0.png', 'img_78_6.png', 'img_85_6.png']
print(len(L))
calligraphy = []
chess = []

# create a random list from calligraphy and chess separately
for elt in os.listdir('../chess_differences/Chess_PNG/'):
    chess.append(elt)
print(calligraphy)
print(chess)
print(len(chess))

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