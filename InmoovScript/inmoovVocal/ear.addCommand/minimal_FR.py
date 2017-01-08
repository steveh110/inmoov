# -- coding: utf-8 --
# GENERAL
ear.addCommand("attacher tout", "i01", "attach")
ear.addCommand(u"détacher tout", "i01", "detach")
ear.addCommand("repos", "python", "rest")

# ARM((S) - inmoovGestures\_minimalArm.py
ear.addCommand("attacher le bras gauche", "i01.leftArm", "attach") #to remove soon
ear.addCommand(u"détacher le bras gauche", "i01.leftArm", "detach") #to remove soon
ear.addCommand(u"lève le biceps droit", "python", "rightbicepsraise")
ear.addCommand("baisse le biceps droit", "python", "rightbicepslower")
ear.addCommand(u"lève le biceps gauche", "python", "leftbicepsraise")
ear.addCommand("baisse le biceps gauche", "python", "lefttbicepslower")
ear.addCommand(u"lève les omoplates", "python", "omoplate")
ear.addCommand("bras devant", i01.getName(), "armsFront")
ear.addCommand("da vinci", i01.getName(), "daVinci")


# HAND(S) - inmoovGestures\_minimalHand.py
ear.addCommand("open your hands", "python", "handsopen")
ear.addCommand("close your hands", "python", "handsclose")
ear.addCommand("open your right hand", "python", "handopen")
ear.addCommand("close your right hand", "python", "handclose")
ear.addCommand("open your hand", "python", "handopen")
ear.addCommand("close your hand", "python", "handclose")
ear.addCommand("open your left hand", "python", "lefthandopen")
ear.addCommand("close your left hand", "python", "lefthandclose")