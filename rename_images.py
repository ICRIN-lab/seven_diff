import os

# L = ['img_51_0.png', 'img_51_1.png', 'img_51_2.png', 'img_51_3.png', 'img_51_4.png', 'img_51_5.png', 'img_51_6.png', 'img_51_7.png', 'img_52_0.png', 'img_52_1.png', 'img_52_2.png', 'img_52_3.png', 'img_52_4.png', 'img_52_5.png', 'img_52_6.png', 'img_53_0.png', 'img_53_1.png', 'img_53_2.png', 'img_53_3.png', 'img_53_4.png', 'img_53_5.png', 'img_53_6.png', 'img_53_7.png', 'img_54_0.png', 'img_54_1.png', 'img_54_2.png', 'img_54_3.png', 'img_54_4.png', 'img_54_5.png', 'img_54_6.png', 'img_54_7.png', 'img_55_0.png', 'img_55_1.png', 'img_55_2.png', 'img_55_3.png', 'img_55_4.png', 'img_55_5.png', 'img_55_6.png', 'img_55_7.png', 'img_56_0.png', 'img_56_1.png', 'img_56_2.png', 'img_56_3.png', 'img_56_4.png', 'img_56_5.png', 'img_56_6.png', 'img_56_7.png', 'img_57_0.png', 'img_57_1.png', 'img_57_2.png', 'img_57_3.png', 'img_57_4.png', 'img_57_5.png', 'img_57_6.png', 'img_58_0.png', 'img_58_1.png', 'img_58_2.png', 'img_58_3.png', 'img_58_4.png', 'img_58_5.png', 'img_58_6.png', 'img_58_7.png', 'img_59_0.png', 'img_59_1.png', 'img_59_2.png', 'img_59_3.png', 'img_59_4.png', 'img_59_5.png', 'img_59_6.png', 'img_59_7.png', 'img_60_0.png', 'img_60_1.png', 'img_60_2.png', 'img_60_3.png', 'img_60_4.png', 'img_60_5.png', 'img_60_6.png', 'img_60_7.png', 'img_61_0.png', 'img_61_1.png', 'img_61_2.png', 'img_61_3.png', 'img_61_4.png', 'img_61_5.png', 'img_61_6.png', 'img_61_7.png', 'img_62_0.png', 'img_62_1.png', 'img_62_2.png', 'img_62_3.png', 'img_62_4.png', 'img_62_5.png', 'img_62_6.png', 'img_62_7.png', 'img_63_0.png', 'img_63_1.png', 'img_63_2.png', 'img_63_3.png', 'img_63_4.png', 'img_63_5.png', 'img_63_6.png', 'img_63_7.png', 'img_64_0.png', 'img_64_1.png', 'img_64_2.png', 'img_64_3.png', 'img_64_4.png', 'img_64_5.png', 'img_64_6.png', 'img_64_7.png', 'img_65_0.png', 'img_65_1.png', 'img_65_2.png', 'img_65_3.png', 'img_65_4.png', 'img_65_5.png', 'img_65_6.png', 'img_65_7.png', 'img_66_0.png', 'img_66_1.png', 'img_66_2.png', 'img_66_3.png', 'img_66_4.png', 'img_67_0.png', 'img_67_1.png', 'img_67_2.png', 'img_67_3.png', 'img_67_4.png', 'img_67_5.png', 'img_68_0.png', 'img_68_1.png', 'img_68_2.png', 'img_68_3.png', 'img_69_0.png', 'img_69_1.png', 'img_69_2.png', 'img_69_3.png', 'img_69_4.png', 'img_69_5.png', 'img_69_6.png', 'img_70_0.png', 'img_70_1.png', 'img_70_2.png', 'img_70_3.png', 'img_71_0.png', 'img_71_1.png', 'img_71_2.png', 'img_71_3.png', 'img_71_4.png', 'img_72_0.png', 'img_72_1.png', 'img_72_2.png', 'img_72_3.png', 'img_73_0.png', 'img_73_1.png', 'img_73_2.png', 'img_74_0.png', 'img_74_1.png', 'img_75_0.png', 'img_75_1.png', 'img_75_2.png', 'img_75_3.png', 'img_75_4.png', 'img_76_0.png', 'img_76_1.png', 'img_76_2.png', 'img_76_3.png', 'img_76_4.png', 'img_76_5.png', 'img_76_6.png', 'img_77_0.png', 'img_77_1.png', 'img_78_0.png', 'img_78_1.png', 'img_78_2.png', 'img_78_3.png', 'img_79_0.png', 'img_79_1.png', 'img_79_2.png', 'img_79_3.png', 'img_79_4.png', 'img_79_5.png', 'img_80_0.png', 'img_81_0.png', 'img_82_0.png', 'img_83_0.png', 'img_83_1.png', 'img_83_2.png', 'img_83_3.png', 'img_83_4.png', 'img_83_5.png', 'img_83_6.png', 'img_83_7.png', 'img_84_0.png', 'img_84_1.png', 'img_84_2.png', 'img_84_3.png', 'img_84_4.png', 'img_84_5.png', 'img_84_6.png', 'img_85_0.png', 'img_85_1.png', 'img_86_0.png', 'img_86_1.png', 'img_87_0.png', 'img_87_1.png', 'img_87_2.png', 'img_87_3.png', 'img_87_4.png', 'img_87_5.png', 'img_88_0.png', 'img_88_1.png', 'img_89_0.png', 'img_89_1.png', 'img_89_2.png', 'img_89_3.png', 'img_90_0.png', 'img_90_1.png', 'img_90_2.png', 'img_90_3.png', 'img_90_4.png', 'img_90_5.png', 'img_91_0.png', 'img_91_1.png', 'img_91_2.png', 'img_91_3.png', 'img_91_4.png', 'img_91_5.png', 'img_91_6.png', 'img_92_0.png', 'img_92_1.png', 'img_92_2.png', 'img_92_3.png', 'img_92_4.png', 'img_93_0.png', 'img_93_1.png', 'img_93_2.png', 'img_93_3.png', 'img_94_0.png', 'img_94_1.png', 'img_94_2.png', 'img_95_0.png', 'img_95_1.png', 'img_95_2.png', 'img_95_3.png', 'img_95_4.png', 'img_95_5.png', 'img_95_6.png', 'img_96_0.png', 'img_97_0.png', 'img_98_0.png', 'img_99_0.png', 'img_99_1.png', 'img_99_2.png', 'img_99_3.png', 'img_99_4.png', 'img_99_5.png', 'img_99_6.png', 'img_99_7.png','img_100_0.png', 'img_100_1.png', 'img_100_2.png', 'img_100_3.png', 'img_100_4.png', 'img_100_5.png', 'img_100_6.png']
calligraphy = []
chess = []

# rename pictures if you have a hole inside your data
'''for elt in L:
    if elt[4:6] != "10":
        print("elt : ", elt)
        new_elt = elt[0:4] + str(int(elt[4:6]) - 1) + elt[6:]
        print("new : ", new_elt)
        print("\n\n")
    else:
        print("yoh", elt[4:7])
        new_elt = elt[0:4] + str(int(elt[4:7]) - 1) + elt[7:]
    os.rename('im/' + elt, 'im/' + new_elt)
'''

# create a random list from calligraphy and chess separately
for elt in os.listdir('img/'):
    if 50 <= int(elt[4:4 + elt[4:].find("_")]) <= 74:
        calligraphy.append(elt)
    elif int(elt[4:4 + elt[4:].find("_")]) >= 75:
        chess.append(elt)
print(calligraphy)
print(chess)
