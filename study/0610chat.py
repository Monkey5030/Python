# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 17:56:01 2021

@author: Admin
"""

import pyautogui
import pyperclip
import time,random
content='''
一、我是挺花心的，不过都花在了你身上，以前是，现在是，以后也是。
二、无论世间多少荆棘，只要有你，生活就无比甜蜜。
三、我的世界很大，装得下万马千军，我的世界又很小，所见之处只有你。
四、你最近真讨厌，讨人喜欢，百看不厌。
五、遇见你之前，我对未来有很多要求，遇见你之后，我只要求是你。
六、不要问我爱你有多深，我真的说不出来，只知道你已成为我生活中的一种习惯，不可或缺的习惯，每天每天，可以不吃饭、不睡觉，却无法不想你。
七、我曾经年少轻狂，莽撞到视死如归，却因为遇到你，突然开始渴望长命百岁。
八、我的心是颗冰糖山楂，甜也为你，酸也为你。能一口咬上来吗，然后我好偷偷抱紧。
九、从你风华正茂，到你的垂垂老矣，岁月让容颜变迁，但我对的你的热情从未有丝毫减少。爱你很久很久，久到一生只够爱一个人。
十、你有没有闻到什么烧焦的味道？那是我的心在燃烧。
十一、想为你做一幅画，以心为笔，以情为墨，以爱你为内容，以余生为落笔。
十二、你说暮色醉人，我就陪你等黄昏日落；你说清醒容易孤独，我就陪你酩酊大醉；你说黑夜太难熬，我就陪你日夜颠倒。
十三、我本是个散漫的人，遇见你之后，四季变得浪漫，睡梦变得轻快，生活有了温柔的坚持。
十四、你是全宇宙最可爱的小星星，我爱了整个宇宙，只为与你碰头。
十五、一生至少该有一次，为了某个人而忘了自己，不求有结果，不求同行，不求曾经拥有，甚至不求你爱我，只求在我最美的年华里，遇到你。
十六、不想你惊艳我年少时光，只愿你暖我今后岁月。
十七、我想写一个故事，以“我”开始，以“幸福”为主题，以“我们”结尾，你看可好？
十八、写你名字可真难，倒不是笔画繁琐，只是写你名字时地蘸上四分春风，三分月色，两分微醺，还有一分你的眉眼才好。
十九、我想和你从放荡不羁的青春，伴你到安安稳稳的枕边人。
二十、你不要着急，你先去读你书，我去看我的电影。总有一天，我们会窝在一起，读同一本书，看同一场电影。
二十一、我很向往大海，如果可以的话，我愿意做一片大海，而你要做一条鱼。我要把你放在我的心里，让你永远离不开我，我要照顾你一生一世。
二十二、茫茫人海之中我也能一眼认出你，因为别人走在路上，你走在我心上。
二十三、你会游泳吗？不会。那你需要学一下了？因为我们马上要坠入爱河了！
二十四、我愿化作一枝玫瑰花，被你紧紧握在手里，为你吐露芬芳；我想变成一块巧克力，被你轻轻含在口中，让你感觉香滑。
二十五、愿陪你三世：一世枕边书，一世怀中猫，一世意中人。
二十六、也许我的笑容不够灿烂，但足够为你扫清冬日里的阴霾；也许我的双手不够温柔，但还能为你拂去俗世尘埃。
二十七、假如我是天上的一颗星星，虽然不是最闪亮的，但我愿意将这颗心交给你，我会在十字路口等你。虽然过客较多，我眼里只有你，我会在原地等你的回来。
'''

print(pyautogui.position())
time.sleep(5)

if __name__=='__main__':
    for line in content.split('\n'):
        if line:
            print(line)
            pyautogui.click(563, 657)
            pyperclip.copy(line)
            pyautogui.hotkey('ctrl','v')
            pyautogui.typewrite('\n')
            time.sleep(random.randint(1,5))