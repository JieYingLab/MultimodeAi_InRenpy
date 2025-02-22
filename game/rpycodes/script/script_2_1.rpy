﻿
###  episode2上半部分 ################
label episode2_1:
    $ config.allow_skipping = False
    window hide
    image episode1_video2 = Movie(play="videos/episode_video/episode2.mpg",loops=0,stop_music=True)
    show episode1_video2
    $ renpy.pause(4.5,hard = False)#时长是你视频的长度，播完自动退出
    hide episode1_video2
    #scene bg2
    #play music "bgm/九衢长街/九衢长街新版.mp3"
    $ renpy.pause(1.0,hard = True)#时长是你视频的长度，播完自动退出
    $ config.allow_skipping = True
    #（黑幕淡出，播放Episode 02界面画面“象牙塔尖的歌剧院”）
    #（停顿3s左右，播放效果音：飞机着陆的那种气流音，保持黑幕）
    stop music fadeout 1.0
    play sound "audio/飞机降落.mp3"
    $renpy.pause(3.0,hard=True)
    #show bg5 with fade
    "和预想的一样，我们很轻而易举地就通过了日本的海关"
    "无论初咲恋柚说出多么蹩脚的中文，日本的海关都没有察觉出任何不对劲的地方. . ."
    "总之，一切都进展得出乎意料的顺利"
    scene black
    #（画面逐渐展开，转到飞机场，白天，画面平移（或者换一种方式移动也可以））
    "遥遥地眺望远处，夕阳落下的余晖洒在天桥与路面的缝隙中"  #会改，看AI最终出图效果
    #
    show sky afternoon with dissolve
    ch "“真美啊”"
    "这是我对这片景色发出来自心底的由衷赞美"
    #voice "voice/cxly_voice/episode2/初咲001.mp3"
    cq "好. . .漂亮"  #日语

    "不知道什么时候从我身边窜出来的初咲恋柚，和我一样被眼前的景象所深深吸引"
    #（注意：这里不要显现立绘，只是有角色说话就行了）
    ch "看起来，能到东京进修. . .也算是个不错的选择"
    scene airport afternoon with dissolve
    voice "voice/l_voice/episode2/e2 蘭 001.mp3"
    show lan size1 a3 normal:
        xalign 0.1
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    l size1 a3 little_serious"真是幼稚，一副没见过世面的样子"
    voice "voice/l_voice/episode2/e2 蘭 002.mp3"
    l "这个‘魔都’，还完全比不上我们自家的‘魔都’"
    "蘭拍了拍我的肩膀，手指了一下远处停靠在路边的智能出租车，向我示意她就要离开了"
    show cx size2 a3 smile:
        xalign 0.9
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    cq "这么快就要走了吗？" #日语
    voice "voice/l_voice/episode2/e2 蘭 003.mp3"
    l size1 a3 smile"是呀，我已经预定好了今天晚上的演出了"
    ch "原来如此. . ."
    ch "来到这边第一件事就是看演出，也会是你做出来的事了"
    voice "voice/l_voice/episode2/e2 蘭 004.mp3"
    l size1 a3 proud"哼哼，那可不是嘛"
    voice "voice/l_voice/episode2/e2 蘭 005.mp3"
    l "毕竟本小姐也对日本这边的演出很感兴趣"
    voice "voice/yqtt_voice/episode2/岩崎001.mp3"
    hide cx size2 a3 smile with dissolve
    show yq size3 a1 smile:
        xalign 0.9
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    yq "好啦，大小姐，只有一个小时了。再不走就真要错过了噢"
    "蘭低头看了看手机，表情从刚才的“胸有成竹”逐渐转变为“惊慌失措”"
    voice "voice/l_voice/episode2/e2 蘭 006.mp3"
    l size1 a3 mad"你. . .刚刚为什么不提醒我！"
    voice "voice/yqtt_voice/episode2/岩崎002.mp3"
    yq size3 a1 little_sad"还不是刚才从机场出来的时候. . .我们的大小姐还非要拉着我到处闲逛. . ."
    voice "voice/l_voice/episode2/e2 蘭 007.mp3"
    l "好了，好了，你不要说了"
    hide lan size1 a3 mad with dissolve
    "岩崎天桐脸上流露出久违的尴尬表情，一边拉着蘭和行李一边往后退"
    voice "voice/yqtt_voice/episode2/岩崎003.mp3"
    yq size3 a1 smile"那我们就先行一步了，明天学校里见！"
    show cx size2 a3 smile:
        xalign 0.1
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    cq "再见咯！" #日语
    ch "回见"
    hide yq size3 a1 smile
    hide cx size2 a3 smile
    with dissolve
    "目送岩崎把蘭拉进智能出租车后，就只剩下我和初咲两个人了"
    "这种不自然的感觉是怎么回事. . ."
    "余光确切地告诉我初咲正在仔细地注视着我的脸"
    show cx size2 a2 wry_smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    cq "那个. . ."
    cq "我也想看演出. . ."  #（此处浮现出初咲的立绘）
    ch "不可以的"
    ch "今天还是先回家吧. . .我对东京这一带完全不熟"
    cq size2 a4 amazing"诶？"
    cq "说起来，海川不是有半个日本的血统吗？"
    ch "那个. . ."
    ". . ."
    "这也难怪"
    "我好像一直都没有说明任何关于自己过去的事情"
    ch "我从小都是在中国长大的，从来没有来到日本. . ."
    cq size2 a3 smile"原来如此. . ."
    cq size2 a3 happy"哼哼，看来以后还得靠我给主人指路了！"
    ch "是这样的"
    ch "不过当务之急还是要先找到初咲的主人，不是吗？"
    cq size2 a2 serious"主人吗. . .？"
    "初咲转过头，又看向了远处的夕阳"
    "那个时候，初咲又显得那么脆弱"
    "就算是robot. . ."
    ch "你放心. . .在找到你的主人之前我是不会离开初咲的！"
    cq size2 a3 surprised"真的？"
    ch "真的！"
    cq size2 a3 happy"我们拉钩"
    ch "拉钩"
    "于是，我们的小拇指交合环绕在一起，形成紧密的闭环"
    cq "说好了哟！"
    hide cx size2 a3 happy with dissolve
    show airport afternoon:
        linear 0.5 zoom 1.2
        linear 0.5 xalign 0.2
        linear 0.5 xalign 0.5
        linear 0.5 zoom 1.0
    $renpy.pause(2.0,hard=False)
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with dissolve
    #（画面中立绘消失，背景从右向左缓缓移动，稍微停顿3-5s）
    "这是我第一次以这么近的距离看着初咲的脸"
    "闭着眼睛向我微笑的她，修长的眉毛和可爱的小嘴再次直勾勾地展现在我的面前"
    "很难不让人想入非非啊. . ."

    #（此处播放效果音，“叮”，手机响了的声音）
    play sound "audio/手机铃声.ogg"
    "收到了母亲的短信"
    ch "是定位地图，让我看看. . ."
    cq size2 a3 happy"也就是说，现在我们要去主人的新家对吧？"
    ch "是的"
    ch "母亲还在家里等我"
    cq size2 a3 smile"噢. . .原来是母上大人. . ."
    cq size2 a3 happy"看来要好好表现了. . .加油，初咲，你一定可以的！"
    "初咲对着旁边的透视镜摆出了一个剪刀手的姿势，突然的“宣言”引来旁边好多人的目光"
    ch ". . .我们还是赶快走吧"
    cq "好的！"
    scene black with tran_lf
    show park2 afternoon with tran_lf
    #（黑幕转场，场景转变：夕阳，目黑川公园+桥+街边）
    "这么来看，实际走在东京的街道上，也并没有我想象中的那么繁华. . ."
    "平房和高楼大厦排布地交错排布，除了几个知名的地标建筑和新建的几个“灯塔”，基本上和我在电影中看到的十几年前的东京一模一样"
    "不过这看起来也算是在情理中的"
    "人们总说,"
    "是东京抓住了时代发展的契机，站住了仿生机器人制造的脚跟，才会出现laser这样的“后起之秀”. . ."
    "实际上据我所知，行业内的架构远非看上去这么简单"
    "倒不如说，这只是一场交易"
    "一场用注资让另一方承担“挡箭牌”的交易"
    "好的商品，无论国际市场如何禁止其销售，只要是好的，就必然有利益产出"
    "有利润，就必然会有能在多边站得住脚的，有一定声望的“商人”出现"
    "“商人”并不需要掌握很多高深的工作很简单。也就只有代言品牌，协调各方，保障交易能以所谓“公正安全”的方式推进"
    "这个“商人”，也就是坐落在东京的“laser高塔”"
    "从国内源源不断运输到东京的robot还有东京的场景也都佐证了这个事实"
    "这也是这种时代里的另一种生存手段. . ."
    "这么说，我也算是“反向求学”了"
    "因为同位于东京的缘故，我的家和“东番高大”以及飞机场的距离不是很远"
    "搭乘地铁的话，基本只要几十分钟就可以来去自如了"
    "虽然说这种效率完全比不上九衢市的地铁. . .但对我来说，这种速度来上学和出游已经足够了"
    "和我相反的是，初咲恋柚恰好展现出无比的激动和喜悦的神情"
    show cx size2 a4 amazing:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    cq "好厉害. . ."
    "就好像. . .她完全没来过日本一样. . ."
    ch "还记得之前主人的具体住址吗？"
    cq size2 a4 sad"那个，"
    cq "好像一点印象都没了"
    ". . . . . ."
    cq size2 a3 happy"不过，我想在找到主人之前再多玩几天！"
    cq size2 a3 smile"如果这时候回到主人身边，又会有很多很多工作等着初咲的. . ."
    ch "这样啊. . ."
    "我不由得想到和初咲相处的一个月里的种种"
    "好像除了做饭好吃点，其他的工作简直就是“一言难尽”啊. . ."
    hide cx size2 a3 smile
    hide park2 afternoon
    with tran_lf
    show home2 afternoon with tran_lf
    #（场景转换，来到海川渡的家门口）
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    cq "这就是主人的家吗？"
    ch "没错，我们到了"
    play sound "audio/门铃.ogg"
    #（播放效果音，“叮”，按下门铃的声音）
    voice "voice/hch_voice/episode2/海川花001.mp3"
    who "来了~"  #（这个地方插入音效调整，类似于从门后传出的声音）
    "熟悉的声音房子里传出来，紧接着就是一阵比较急促，赶过来开门的脚步声"
    play sound "audio/开门.ogg"
    #（插入效果音：“哐当”，开门的声音）
    voice "voice/hch_voice/episode2/海川花002.mp3"
    who "欢迎回家哦，海川渡！"
    show mom size1 a1 happy:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    #（此时插入海川花的立绘，微笑）

    "这是我的母亲，海川花"
    "她的样子看上去比之前在中国生活的那段时间要更显疲惫一点，可能是因为搬到日本之后还是有很多事情要处理"
    voice "voice/hch_voice/episode2/海川花004.mp3"
    ma size1 a1 smile"你身后的是. . .？"
    "她够起身子往后看了看，很明显是注意到了我身后的初崎"
    hide size1 a1 smile with Dissolve(0.2)
    show mom size1 a1 smile:
        xalign 0.2
        yalign 1.0
        zoom 1.3
    show cx size2 a3 smile:
        xalign 0.8
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    cq "主人的. . .母亲大人！晚上好！"
    voice "voice/hch_voice/episode2/海川花005.mp3"
    ma size1 a1 surprised"啊嘞嘞. . ."
    "母亲先是愣了一会儿，然后很快地回过神来"
    "她的嘴角似乎是向上微微扬起了一点，转而用一种调侃的眼神看着我"

    #（这里切换海川花的表情，从一开始的惊讶变成调侃表情）
    voice "voice/hch_voice/episode2/海川花006.mp3"
    ma size1 a1 smile"原来是这样啊. . ."
    voice "voice/hch_voice/episode2/海川花007.mp3"
    ma size1 a1 happy"海川君好厉害呀！"
    voice "voice/hch_voice/episode2/海川花008.mp3"
    ma "竟然背着你的母上大人找到了一个日本的女朋友"
    ch ". . . . . ."
    ch "不是这样的"
    voice "voice/hch_voice/episode2/海川花009.mp3"
    ma size1 a1 smile"才刚刚下飞机几个小时. . .蛮不错的嘛. . ."
    cq size2 a4 amazing"才. . .才不是什么女朋友"
    cq "恋柚是主人的仆从来着！"
    voice "voice/hch_voice/episode2/海川花010.mp3"
    ma size1 a1 happy"哼哼. . ."
    #voice "voice/hch_voice/episode2/海川花011.mp3"
    ma size1 a1 smile"我还是听得懂一点日语的"
    voice "voice/hch_voice/episode2/海川花011.mp3"
    ma "原来现在的年轻人之间还有这样刺激的玩法. . .噗噗. . ."
    ch "越说越乱了啊喂！！！"
    voice "voice/hch_voice/episode2/海川花012.mp3"
    ma "好啦，你们俩还是先进来吧"
    hide mom size1 a1 smile
    hide cx size2 a3 smile
    with Dissolve(0.2)
    hide home2 afternoon with tran_lf
    show livingroom2 night with tran_lf
    #（场景转换：来到日式房间的客厅：海川渡的家，要求能看到餐桌，里面的风格是日式，稍微有一点点科技感）

    "一股温馨感铺面而来，整栋小房子的布局风格和在九衢市的那间几乎完全一致"
    "习惯了在国内的装潢设计，这种日风给我带来一种别具一格的韵味"
    voice "voice/hch_voice/episode2/海川花013.mp3"
    show mom size1 a1 happy:
        xalign 0.2
        yalign 1.0
        zoom 1.3
    with dissolve
    ma "我先去准备晚饭啦，稍等~"
    show cx size2 a3 happy:
        xalign 0.8
        yalign 1.0
        zoom 1.3
    with dissolve
    cq "我也来帮忙吧！"
    voice "voice/hch_voice/episode2/海川花014.mp3"
    ma size1 a1 smile"哦~看起来很积极嘛！你的名字是？"
    cq size2 a3 smile"母上大人，是初咲恋柚哦"
    voice "voice/hch_voice/episode2/海川花015.mp3"
    ma ". . .那就先喊你‘柚子’吧！感觉还蛮符合你的性格"
    cq size2 a3 happy"好的！"
    "她们不断的交谈声吵得我有些不太习惯"
    "之前在家独处的时候我从来没有这样的感觉"
    hide cx size2 a3 happy
    hide mom size1 a1 smile
    with Dissolve(0.2)
    hide livingroom2 night with tran_lf
    show bedroom2 night with tran_lf
    #（场景转换：来到日式的海川渡的房间/或者保持房间风格和之前的一样）

    "房间看上去和在九衢市的一模一样，只不过已经换上了崭新的家具"
    "我轻轻地放下手中的行李，把包中的东西慢慢清理出来"
    "在这里面的，不仅有我自己的衣物和入学前准备的各种物品书籍. . ."
    "还装着初咲的各种随身物品. . ."
    "这么说来，我完全没想到自己和这样的女孩子同居了两个月. . ."
    "就算是机器人. . ."
    ". . ."
    "我到底在想什么啊？！"
    ch "嘶~"
    "在我正在进行无聊的分拣工作的时候，一股刺痛感从我的手指间袭来"
    "从众多的杂物中，我摸到了一柄小刀"
    "钴蓝色的刀柄. . .和那个时候的一模一样. . ."

    #（昏黄滤镜+
    
    show street afternoon
    show cx size2 a2 serious:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    show memory
    with dissolve
    voice "voice/cxly_voice/episode1/初咲012.mp3"
    cq "提问："  #（日语）
    voice "voice/cxly_voice/episode1/初咲013.mp3"
    cq "由中国代表在联合国大会上提倡的新世代三个核心词是？"
    hide street afternoon
    hide cx size2 a2 serious
    hide memory
    with dissolve
    "还有那个时候. . ."

    #（昏黄滤镜+
    show park night
    show cx size2 a2 serious:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    show memory
    with Dissolve(0.2)
    cq "要不然很快就会. . ."
    cq "没，命，噢~"
    hide park night
    hide cx size2 a2 serious
    hide memory
    with dissolve
    #昏黄滤镜关闭)
    "原来，初咲一直都把这么“危险”的东西一直带在身边"
    "看来还是. . ."
    show cx size2 a2 serious:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with dissolve
    cq "在干什么呢，主人！"
    ch "诶？！"
    "不知道是什么时候开始，初咲就站在了我的身后"
    "从她的脸上，我似乎感受到了满溢的杀气感"
    cq "全都看完了吧. . .那个东西. . ."  #日语，声音稍显低沉，冰冷
    ch "你. . .你说什么"
    "阴沉着脸的初咲着实把我又吓了一跳，但是我很快意识到这又是初咲口的“演出”"
    cq "让我看看"
    "还没等我反应过来，初咲猛地转到我的身后，把我背在身后的小刀给抽出来了"
    cq size2 a3 normal"什么嘛，原来是这个！"
    ch ". . ."
    ch "难不成你说的不是这个？"
    "看到初咲恋柚一脸如释重负的样子，我故意把手伸向半开的行李"
    cq size2 a4 amazing"欸欸欸！"
    cq size2 normal"那个是. . .初咲的隐私. . ."
    "说完，初咲从行李中抽出一本黑皮日记本，看上去像是有了很长年代感的物件了"
    "倒不如说. . .已经好久没见到“日记本”这种东西了"
    "日常的记录和学习，我都更喜欢用电子屏来记下来，已经快忘记了这种纸质化记录是怎样的体验了"
    cq size2 a4 little_serious"主人一定要答应我，这个绝对不能偷看哦！"
    ch "好的好的. . .我对这种什么‘少女的隐私’完全不感兴趣"
    ch "你大可以放心"
    cq size2 a3 smile"那我就大胆地相信主人一次吧！"
    "说完，初咲便把这本书随手搁置在一旁的书桌上，哼着歌走出去了"
    hide cx size2 a3 smile 
    with dissolve
    #（立绘消失）

    "与其在意初咲的事情，不如说我更应该在意的是明天开学的各种准备"
    "到现在为止我甚至连校服都没有拿出来好好清洗一遍. . ."
    voice "voice/hch_voice/episode2/海川花016.mp3"
    show mom size1 a1 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    ma "海川，可以一起来吃饭啦！"
    ch "好"
    hide mom size1 a1 smile
    with Dissolve(0.2)
    hide bedroom2 night with tran_lf
    show livingroom2 night with tran_lf
    #（黑幕转场，转到日式客厅）
    voice "voice/hch_voice/episode2/海川花017.mp3"
    show mom size1 a1 happy:
        xalign 0.1
        yalign 1.0
        zoom 1.3
    show cx size2 a3 smile:
        xalign 0.9
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    ma "啊拉拉，看来你们的关系很不错欸. . .真好"
    "可能是看到了初咲不断给我夹菜的缘故，母亲又开始用这样的口吻调侃我了"
    ch "初咲只不过是个机器人而已啦. . ."
    voice "voice/hch_voice/episode2/海川花018.mp3"
    ma size1 a1 smile"我当然知道了，刚刚柚子已经把她的事跟我讲了一遍"
    voice "voice/hch_voice/episode2/海川花019.mp3"
    ma "不然我们的海川，青春都没体验过就成年了. . ."
    voice "voice/hch_voice/episode2/海川花020.mp3"
    ma size1 a1 normal"找到真正的女朋友，应该还是有一定难度的"
    ch "也不能这样说啊！"
    "忽然想起来在国内的那段高中生活"
    "好像确实连一段恋爱经验都没有. . ."
    voice "voice/hch_voice/episode2/海川花021.mp3"
    ma size1 a1 smile"不过都在变好，不是吗？"
    "说完，海川花还不忘把头朝我身旁的初咲轻轻点了点"
    cq size2 a3 happy"当然，我会尽可能让主人的生活变好！"
    cq "毕竟我可是最先进的哦！"
    voice "voice/hch_voice/episode2/海川花022.mp3"
    ma size1 a1 happy"要学会把握当下"
    ch "咳咳. . .你在说什么呀！"
    voice "voice/hch_voice/episode2/海川花023.mp3"
    ma "海川当然懂我的意思"
    ch "我吃饱了，去收拾了"
    hide mom size1 a1 happy
    hide cx size2 a3 happy
    with Dissolve
    hide livingroom2 night with tran_lf
    "匆忙地从餐桌逃离后，我简单冲了个澡，然后就倒在床上睡着了"
    $renpy.pause(1.0,hard=False)
    #（转场黑幕转场，转到目黑川の樱花大道，白天）
    show street2 day with dissolve
    "匆忙与母亲道别后，我循着地图前往学校"
    ch "第一天去学校，我就迟到了. . ."
    "更糟的是，我没有喊初咲起来. . ."
    "管不了那么多了"
    hide street2 day with tran_lf
    show school day with tran_lf
    #（场景转换，转到东番高大门口，白天）

    ch "呼. . .呼. . ."
    "勉强算是赶上了"
    "“东番高大”的几个片假名和圆型的显目校徽在阳光的照射下显得那么耀眼"
    ch "九点钟的‘机器人制造’学院的新生大会. . .只有十五分钟了. . ."
    "我加快了速度，希望能尽早到达校园内"
    hide school day with tran_lf
    show schoolpassage day with tran_lf
    #（播放效果音：“扑通”，把人撞倒的声音）
    play sound "audio/撞击.ogg"
    ch "嘶啊. . ."
    "因为太着急的缘故，我没有注意到旁边有别的学生经过，狠狠地与这个人撞上了"
    who "没事. . .吧？"
    ch "没事的. . .倒是你. . .刚刚是我太着急了"
    who "诶？"
    show xy size2 a1 normal:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with Dissolve(0.2)
    #（这里显示出西野玥奈的立绘，脸稍微红，惊讶表情）

    "眼前的是一个高挑的黑发女生，甚至从她身上闻到淡淡的鲜花芬香"
    "从妆容和打扮上看，完全就是我幻想中大小姐的模样啊！"
    "但是她现在正在用异常惊讶的神情打量着我，就像是在打量一个“异类”一样"
    who "中国人？"
    ch "抱歉抱歉，那个. . .我先走一步了. . ."
    "我从这位“大小姐”的身边绕过，然后继续向前跑去. . ."
    hide schoolpassage day 
    hide xy size2 a1 normal
    with tran_lf
    $renpy.pause(0.5,hard=False)
    show hall with tran_lf
    #（场景转换，转到东番高大的礼堂内。在西野做演讲的时候，镜头逐渐从右往左移，或者按照聚焦方式推进镜头也可以）

    "在这里听了一个多小时的会议后，很快就到了最后一项——“学生代表发言”"
    "实际上我还是很期待这个环节的"
    "往往在这个时候亮相的都是非常厉害的新生. . ."
    "更何况是最顶尖的高大. . .最顶尖的学院. . ."
    "从舞台屏风后慢慢走出一个高挑曼丽的身影"
    play sound "audio/鼓掌.mp3"
    #（播放效果音：鼓掌）
    sa "听说了吗？那个就是. . ."
    sb "西野好像是我们的学姐. . ."
    sc "选她上来演讲也是理所当然的事情吧. . ."
    "并排坐在我身边的几位同学用日语在窃窃私语着什么。听上去好像是和登台的这个女孩子有关. . .好像来头还不小. . ."
    show hall:
        linear 0.5 zoom 1.3
    show xy size2 a1 normal:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with Dissolve(0.2)
    ch "诶，等等. . ."
    ch "是刚才那个我撞上的女孩子！"
    "一样的服装，一样的气质. . .虽然我坐在整个剧场靠后的位置，但是我能立刻断定舞台的这个人就是刚才那个女孩！"
    xy size2 a1 smile"大家好，我是四年级的西野玥奈"
    xy "今天很荣幸能作为学生代表在此为各位发言"
    "大. . .大小姐？果然不错，和我预想中是一样的"
    "优雅大度的上台方式，一看上去就是富家子女"
    xy "我想在这里与大家分享一下我和‘robot’的故事. . ."
    hide xy size2 a1 smile
    hide hall 
    with clockwise
    $renpy.pause(0.5,hard=False)
    show hall 
    with clockwise
    #（此处的场景转换，由该场景变成该场景，展现出一种时间流逝的感觉）

    "在这样甜美动听的声音洗礼下，我的注意力很快就集中在了她身上"
    "无论什么专业，高大的学生都是相同的制服"
    "但是在素来被誉为“机造男子学院”的地方，这样漂亮的女生也是很少见了"
    "从她讲的故事来看，想必也是和其他来到这里的同学一样，抱着对时下大火的仿生机器人制造的兴趣而来. . ."
    "从小就能接触到这么高深的知识，她的家庭条件已经可见一斑了"
    "舞台上变换的灯光束不断投影出一个个极为真实的场景，似乎都是些和她所讲述的故事相关的场景"
    "在高大，对“优秀”的定义大抵也是到了她这种地步吧. . ."

    #（此处的场景转换，由该场景变成该场景，展现出一种时间流逝的感觉）
    hide hall 
    with clockwise
    $renpy.pause(0.5,hard=False)
    show hall 
    with clockwise
    "很快，这场演讲就作为迎新典礼的结束致辞落下了帷幕"
    "四周的同学也逐渐从座位上起身离场"
    "周围窃窃私语的声音似乎都在讨论今天的迎新典礼"
    "看上去，不少同学都对今天这位女生的演讲很感兴趣. . ."

    #（播放效果音：嘈杂的，很多人的窃窃私语声）（嘈杂声持续到本幕结束）
    play music "audio/嘈杂.mp3"
    sa "这个学姐真的好优雅啊. . ."
    sb "作为高大的优秀学生代表，想一想都知道，是我们之中最优秀的存在吧！"
    sc "从今天开始要好好努力，然后争取到认识她的机会！"
    "不过，注重细节的我还是在这场演讲中发现了一些不足——"
    "在整个演讲的过程中还是存在着着本可以避免的用词不当和停顿问题"
    "对于这样“优秀”的存在，应该是她没怎么准备就直接上台发言的吧. . ."
    "嘛. . .比起这个，我现在更应该关注的是自己的事情"
    "在要求严苛的高大里，我不仅需要维持自己的功课达到学校的标准，还要抽出时间帮助初咲找到她真正的主人"
    "这学期看上去也会是“举步维艰”的一段时期"
    "伴随着这样的想法，我也起身离开了礼堂"
    stop music
    hide hall with tran_lf
    show corridor with tran_lf
    #（场景转换，东番高大的走廊上，露出蘭和岩崎的立绘）
    show lan size2 a1 normal:
        xalign 0.1
        yalign 1.0
        zoom 1.3
    show yq size3 a1 normal:
        xalign 0.9
        yalign 1.0
        zoom 1.3
    with dissolve
    "就在离开礼堂不久后，我很快就在走廊上碰到了刚刚参加完“交演院”开学典礼的蘭和岩崎天桐"
    "与此同时，他们正在就今天“交演院”的开学典礼发生的种种进行激烈的讨论"
    voice "voice/yqtt_voice/episode2/岩崎004.mp3"
    yq "害，一个迎新会，为什么会有这么多复杂的流程. . ."
    voice "voice/l_voice/episode2/e2 蘭 008.mp3"
    l size2 a2 little_serious"这是礼节，也是墨守成规的规定"
    voice "voice/yqtt_voice/episode2/岩崎005.mp3"
    yq "照我看，还不如一上来就直接教会我们各种厉害的术式. . ."
    voice "voice/l_voice/episode2/e2 蘭 009.mp3"
    l size1 a3 little_serious"傻瓜，是‘交叉演出’，不是‘术式’这种说法"
    #voice "voice/yqtt_voice/episode2/岩崎005.mp3"(配掉了)
    yq size3 a1 smile"哟，是海川啊，早上好！"
    "在看到远处的我后，岩崎天桐摆出了剪刀手的pose，似乎很是兴奋的样子"
    ch "早上好"
    voice "voice/l_voice/episode2/e2 蘭 010.mp3"
    l size1 a3 smile"海川这边感觉如何？"
    voice "voice/l_voice/episode2/e2 蘭 011.mp3"
    l "我们‘交演院’的迎新活动可全部都是采用‘演出’的形式开展的哦！"
    ch "这个. . ."
    ch "好像一直在演讲. . .没有什么特别的地方"
    ch "我只记得最后一个演讲的是. . ."
    voice "voice/l_voice/episode2/e2 蘭 012.mp3"
    l size1 a3 normal"是‘西野’学姐对吧？"
    ch "啊？我不知道诶"
    ch "不过看上去也确实像是学姐那样的人物"
    voice "voice/yqtt_voice/episode2/岩崎006.mp3"
    yq size3 a1 little_sad"你连这个都不知道吗？是‘西野玥奈’啊，大名鼎鼎的‘西野公主’"
    ch ". . ."
    ch "能不用这种中二的口气说话吗？我真的有点听不懂"
    voice "voice/l_voice/episode2/e2 蘭 013.mp3"
    l size2 a1 normal"岩崎确实没有夸大，叫她‘公主’也正常"
    ch "等等. . .你们说的西野. . "
    ch "不会说的是‘laser’的那个西野家族吧？"
    voice "voice/l_voice/episode2/e2 蘭 014.mp3"
    l size2 a1 little_serious"没错，‘激光’的唯一的千金小姐，也是‘机造院’大我们一级的学姐"

    #（下面这两句话看看是加在文本注释中还是怎么搞，感觉直接插入台本中有点问题）
    "laser，激光集团，也就是现在全球最大的新世代机器人制造公司"
    "初咲恋柚这样优秀的机身和系统也是由laser公司一起做的"

    voice "voice/l_voice/episode2/e2 蘭 015.mp3"
    l size2 a2 proud"连我这个外院的学生都听说过，海川可真是孤陋寡闻啊"
    ch "好了好了，我也知道高大肯定是人才辈出的"
    ch "只是很惊讶能在这里竟然能亲眼见到那样的人物"
    ch ". . . . . ."
    ch "倒不如，现在这个时间，还是先去吃午饭吧？"
    voice "voice/yqtt_voice/episode2/岩崎007.mp3"
    yq size3 a1 happy"好耶！是补充魔力的时间！"
    voice "voice/l_voice/episode2/e2 蘭 016.mp3"
    l size2 a1 little_serious"小声点啊喂，这里可不是九衢市. . ."
    ch ". . ."
    "看着蘭和岩崎互相打闹着，我尴尬地笑一笑，刻意地将视线避开他们俩"
    "这时，旁边掠过的一道黑影引起了我的注意"
    "尽管只是在一瞬之间，我还是捕捉到了西野大小姐的身形"
    "独属于千金特性-略带忧郁的神色和那种淡雅的高贵感很难不引起我的注意"
    "看上去，西野学姐是有很大的心事吧. . ."
    "刚刚的演讲，对她来说怎么都是“失败”的"
    voice "voice/l_voice/episode2/e2 蘭 017.mp3"
    l size2 a1 smile"走吧，别发呆了"
    ch "好的好的"
    "看着西野学姐远去的背影，我本来以为，我们再也不会有任何交集"
    "毕竟那种身世，与我相比简直就是天和地的区别. . ."
    "我不知道的是，我们很快就会再次以不寻常的方式相遇. . ."
    hide lan size2 a1 smile
    hide yq size3 a1 happy
    with dissolve
    hide corridor with clockwise
    show classroom day with clockwise
    #（Q版动画转场，转到教室内，此时为白天）

    "在学校里熟悉了两个星期后，我大概对学校的很多事情有了初步了解"
    "虽然在学校的这段时间里确实显得有些无聊. . .可能是白天几乎见不到初咲的缘故. . ."
    "到了晚上也是一个人跑出去，很晚才回来"
    "好像说是要找“真正的主人”. . ."
    "虽然我尝试过跟着初咲，防止她在外面出现什么意外"
    "不过每次尾随在她身后的结果都是跟丢了. . ."
    "在和她的交集少了很多之后，事情一下子就少了很多"
    "虽然每天学习的课程带给了我过量的充足感"
    "不过少了她的吵闹或许给我带来一种奇怪的缺憾感. . ."
    voice "voice/yqtt_voice/episode2/岩崎008.mp3"
    yq "来自平行时空的再次传唤. . .ダークナイト在这个清晨为您而战. . .吾王！"  #（在此处显现出岩崎的立绘）
    show yq size3 a1 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with dissolve
    "从我的身后突然传来熟悉的“中二”声音"
    "虽然我已经习惯了平常这个时间点会遇上刚从教学楼走出来刚上完编导课的蘭"
    "但在这个时间点遇上岩崎还是第一次"
    ch "喂喂，这样子真的很让人尴尬的. . .还是用夹杂着日语的中文说出这样的话！"
    ch "你就别拿你那蹩脚的日语丢人了…"
    voice "voice/yqtt_voice/episode2/岩崎009.mp3"
    yq "嘿嘿，又一次进入‘混沌状态’了"
    ch "给我正经点啊喂！"
    voice "voice/yqtt_voice/episode2/岩崎010.mp3"
    yq size3 a1 normal"咳咳，初咲呢？"
    "岩崎清了清嗓子，然后够着脚尖，似乎是在努力在我身后寻找着预想中初咲的身影"
    ch ". . ."
    "虽然东番高大也对初咲，岩崎这种仿生机器人开放了部分培训课程，但是似乎要通过主人和机器人两者同意才会有的修习内容"
    "也就是说，在学校里的“仿生机器人”，是最自由的，无拘无束的群体。他们完全可以做自己喜欢做的事情"
    "当然是在学校规定范畴之内的. . ."
    "对于初咲那家伙. . .自然是把学校每周都有的演出和寻找真正主人的住处这两件事情放在最重要的位置. . ."
    ch "最近在学校里都没怎么见到她了. . ."
    voice "voice/yqtt_voice/episode2/岩崎011.mp3"
    yq size3 a1 amazing "你这副样子，是和初咲发生矛盾了吗？"
    ch ". . ."
    ch "也算不上是矛盾吧"
    ch "或许在学校里，我们都有自己着重的事情. . ."
    voice "voice/yqtt_voice/episode2/岩崎012.mp3"
    yq size3 a1 normal "原来是这样啊"
    voice "voice/yqtt_voice/episode2/岩崎013.mp3"
    yq "你们还有繁多的课业。不像我，每天都可以绕行高大散步好几圈. . .然后再去做个例行检查. . .然后开启一天的‘养老’生活. . ."
    ch ". . ."
    ch "真羡慕你们啊"
    ch "要是能帮我们完成一下作业就更好了"
    voice "voice/yqtt_voice/episode2/岩崎014.mp3"
    yq  size3 a1 smile"那可不行"
    voice "voice/yqtt_voice/episode2/岩崎015.mp3"
    yq "毕竟你们是被‘魔导书’挑选出来的‘继任者’。这种事情. . .恕我无力帮忙"
    ch ". . ."
    "确实如此,"
    "在进入东番高大的时候，每个仿生机器人就安装了独特的‘高大芯片’"
    "这些芯片在一定程度上限制了他们的行动. . ."
    "需要人力完成的作业都是不被允许使用外力帮忙的"
    voice "voice/yqtt_voice/episode2/岩崎016.mp3"
    yq size3 a1 normal"今天过来找海川也是想提醒一下你"
    voice "voice/yqtt_voice/episode2/岩崎017.mp3"
    yq "与机器人相处，最重要的就是让她知道自己是被需要的一方"
    ch "被. . .需要的？"
    show cafe
    show memory
    with pixellate
    #（此处切换回忆到和阿泉先生对话那一段，白色顺闪转场）
    #开始
    mrquan "如果时间允许的情况下. . .我建议还是和那个‘要帮助的对象’多多接触. . ."
    mrquan "不然草草决定‘帮助’和‘不帮助’都是很不明智的选择啊"
    #结束
    hide cafe
    hide memory
    with pixellate
    voice "voice/yqtt_voice/episode2/岩崎018.mp3"
    yq "没错，我们的意义就在于完成主人给定的任务"
    ch "好吧，我知道了"
    voice "voice/yqtt_voice/episode2/岩崎019.mp3"
    yq "蘭前几天调查了整个东京的人员名单，关于初咲主人的记录显示为空"
    ch "一点线索都没找到吗？"
    voice "voice/yqtt_voice/episode2/岩崎020.mp3"
    yq size3 a1 little_sad"是的. . ."
    voice "voice/yqtt_voice/episode2/岩崎021.mp3"
    yq "我们已经拜托她的父母调查laser相关的购置记录. . .估计不久之后就会有答案了吧. . ."
    voice "voice/yqtt_voice/episode2/岩崎022.mp3"
    yq size3 a1 normal"在此之前，你很难摆脱‘临时主人’这个身份，成为一个好主人是海川的‘必修课’"
    ch ". . ."
    ch "这副说教的态度，看来是蘭让你来传话的对吧？"
    "岩崎吃惊地看着我，似乎是没想到我会这样一针见血地指出来，然后很快转变成平静的表情"
    voice "voice/yqtt_voice/episode2/岩崎023.mp3"
    yq "没错"
    voice "voice/yqtt_voice/episode2/岩崎024.mp3"
    yq size3 a1 little_sad"小兰也知道. . .她说的话海川是听不进去的"
    ch "所以. . .她没来？"
    ch "按理来说她应该在这个时间点等着和我们一起吃饭的"
    voice "voice/yqtt_voice/episode2/岩崎025.mp3"
    yq size3 a1 amazing"诶，你不知道吗？"
    voice "voice/yqtt_voice/episode2/岩崎026.mp3"
    yq "今天是各社团开展招新活动的时间哦，小兰去参加编导部的部活去了"
    ch "招新活动？"
    ch "哦！我想起来了"
    "要不是岩崎提醒我，我差点忘记了这个异常重要的时间节点"
    "学校里各个社团的路演展示时间！"
    "这是我一直以来都非常向往的“部活”，也就是在国内被称为“社团活动”的东西"
    "在各种部门活动中，往往能从中找到志趣相投的异性同伴. . ."
    "在高大里，加入一个部门是强制要求的活动，这样也保证了我们能在课业之外拓展很多兴趣"
    ch "诶等等？那个不是下午才正式开始吗？"
    voice "voice/yqtt_voice/episode2/岩崎027.mp3"
    yq size3 a1 normal"是这样. . .但她已经迫不及待地跑过去了"
    "不愧是她. . ."
    "蘭对编导和编剧的热爱似乎永远超过了我的想象"
    voice "voice/yqtt_voice/episode2/岩崎028.mp3"
    yq size3 a1 smile"这么说来，海川有什么特别中意的部门吗？"
    ch "要说起来的话. . .还是和演出相关的吧. . .我还是很喜欢参与策划一些表演的"
    voice "voice/yqtt_voice/episode2/岩崎029.mp3"
    yq "哦？~"
    voice "voice/yqtt_voice/episode2/岩崎030.mp3"
    yq "我记得高中的时候海川就好像成立了一个‘PTF演出社团’来着. . ."
    ch "嗯"
    "在高中的时候，出于自己的爱好，我组建了一个名为“PTF演出社团”的社团"
    "在这里遇见了很多有着共同爱好的同学，好好地享受了我的高中生活"
    "只可惜，因为我要来目黑川进修，社团里的大家也没有时间接手. . .最后也就这么轻易地解散了. . ."
    voice "voice/yqtt_voice/episode2/岩崎031.mp3"
    yq size3 a1 happy"好好弥补回高中的遗憾吧"
    ch "嗯"
    ch "岩崎呢？我记得在手册上好像说过仿生机器人也是可以参加部活的吧. . ."
    voice "voice/yqtt_voice/episode2/岩崎032.mp3"
    yq size3 a1 smile"那可是当然. . ."
    voice "voice/yqtt_voice/episode2/岩崎033.mp3"
    yq "我的目标就是加入‘超自然研究协会’！"
    voice "voice/yqtt_voice/episode2/岩崎034.mp3"
    yq "研究这种不被物理世界规则束缚的怪异，不觉得是很酷的事情吗？"
    ch ". . ."
    ch "听上去就是为你量身打造的部活. . ."
    voice "voice/yqtt_voice/episode2/岩崎035.mp3"
    yq "那下午再见吧"
    ch "好"
    hide yq size3 a1 smile
    show yq size4 a1 leave:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    hide yq size4 a1 leave with dissolve
    #（岩崎的立绘隐去）

    "实话说，我还是很期待今天下午的部活路演"
    "在这两周里，东番高大的活动好像就没让我失望过"
    "我的青春. . ."
    "再次焕发了生机！"
    hide classroom with clockwise
    show square day with clockwise
    #（黑幕转场，转到部活路演现场，大场景）
    "于是，下午的时间很快就到来了"
    "被岩崎拉着的我很不情愿地在‘超自然研究协会’的摊前转了很久"
    "听了一群奇奇怪怪的学长学姐给我‘预测天命’什么什么之类的"
    "岩崎看上去也是非常激动的样子"
    "虽然在语言上并不是非常相通，但是这样‘志趣相投’的人聚集在一起"
    "想必也有自己独特的沟通方式吧"
    voice "voice/yqtt_voice/episode2/岩崎036.mp3"
    show yq size1 a1 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with dissolve
    yq "喂喂，你要不要和我一起入部呀，这个真的超厉害的. . ."
    "看着岩崎眼中不断冒出来的星星，直觉告诉我"
    "这个地方不可久留"
    ch "我稍微去那边休息一下. . .等下过来找你. . ."
    "我指着旁边的一个长椅，尝试给自己开脱的借口"
    voice "voice/yqtt_voice/episode2/岩崎037.mp3"
    yq size1 a1 happy"好嘞"
    hide yq size1 a1 happy with dissolve
    #岩崎的立绘消失

    "终于，在岩崎随口敷衍了我一下之后，我更加放心地从这个摊位上离开了"

    #如果有AI生成的额外背景，这里画面一转，来到部活路演附近的一个长椅特写上，旁边的细节有帐篷，路演道具等等，和国内那种路演差不多，带一点点日式科技风就可以了

    "我坐在长椅上，翻看着发给每一位新生的“宣传手册”"
    "小小的一本手册充满着各个部门宣传文字"
    "于我来说，从中发掘出有用的信息实在是太难了. . ."
    ch "诶. . .这是. . .？"
    "在一瞬间，我的视线突然聚集到了这个宣传单的一隅"
    ch "上面写着的是. . ."
    ch "‘创作演绎部’"
    "作为一度痴迷于演出的我来说，能找到这样的一个时和我的去处看上去是再合适不过了"
    ch "或许，在这里还能收获‘断片的青春’"
    "在“创作演绎部”的这一行小字和一个简单的宣传照片在整张过分精致的部活中显得尤为普通"
    "不对. . .甚至都不能用“普通”这个词来形容“创作演绎部”的部活了. . ."
    "应该是用“简陋”啊喂！"
    "但是. . .当我翻看了整本手册足足三遍后，能发现和“演出”相关的部活只有编导部的前往剧院的编导工作和创演部的演出工作了. . ."
    "和蘭一起去“编导部”部活. . .这种事还是算了吧"
    "给我的选择，也只剩下最后这一个了"
    ch "下一步，就是要找到‘创作演绎部’了"
    "虽然我对创演部的部活环境很是担心. . ."
    "抱着试一试的态度，去看看吧！"

    #（场景转换，来到路演摊位上，白天）

    "但是在这么多的路演摊位上，要找到我心仪的社团简直如同海底捞针"
    "在哪里呢. . ."
    "路演布局并没有什么规律，我只能慢慢搜找了. . ."

    #（这里可以加入一个小游戏，如何找到社团，凸显出找到“创作演绎部”的困难。笔者的建议是可以加入很多个label，然后让玩家做出方向的选择，大概有5-6次选择，最终找到“创作演绎部”的摊位）

    ch "呼呼，看到啦！"
    "经历了长期的找寻之后，我总算找到了‘创作演绎部’的地方——"
    "看起来，创作演绎部就这样被诸如“LAS机器人协会”，“发热电子同好会”等这样的高科技社团挤在角落里，看上去一点也不显眼"
    hide square with tran_lf
    show booth with tran_lf
    #（切换背景图：创作演绎部：路演地点，并随着屏幕慢慢移动）

    "搭在角落里的，一个小小的帐篷上挂着‘创作演绎部’的几个大字"
    "在摊位前，好像只有一个看上去像是学姐的角色在打理着摊位"
    "随着我慢慢地接近，那个学姐也向我投来了打趣的目光"

    #（展示西野玥奈的立绘，微笑脸）
    show xy size2 a2 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with dissolve
    who "下午好呀. . .你是对‘创作演绎部’感兴趣的吗？"
    ". . . . . ."
    "虽然在帐篷中的光线很暗，但是我还是立马认出了她的脸"
    ch "等等. . .你是那个. . ."
    ch "西野学姐？？？！"
    hide xy size2 a2 smile
    show xy size2 a2 perspire:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with Dissolve(0.2)
    who "诶. . .？"  #（此时转疑惑脸）
    "她再次投过来和我第一次相遇时的那种眼光"
    "诶，不对. . ."
    "刚刚我好像说的是中文！"
    "我忽然想起来上次我好像也说的是中文"
    ch "抱歉抱歉，因为一直都没有和本地人交流过，中文就脱口而出了. . ."
    "平常见到的人都是初咲，岩崎，蘭，还有母亲. . ."
    "好像来到目黑川后也没有几次开口说日语的机会. . ."
    "说出口的日语也多少让我感到奇怪. . ."
    hide xy size2 a2 perspire
    show xy size2 a2 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with Dissolve(0.2)
    who "没关系的"
    who "是在中国长大的吗？"
    ch "嗯嗯"
    ch "虽然我是从中国来的. . .但是我有一半的日本血统. . ."
    who "唔呣. . ."
    who "中国. . ."
    hide xy size2 a2 smile
    show xy size2 a2 happy:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with Dissolve(0.2)
    who "厉害耶！"  #（西野玥奈立绘表情转换为激动）
    "学姐的脸上露出非常羡慕的表情，直勾勾地盯着我"
    who "那你应该知道中国的古典乐对吧？！对吧？！"
    ch "嗯…稍微知道一点演奏古典乐的乐器. . ."
    who "好耶！！！我很喜欢中国的古典乐！"
    "学姐兴奋地挥动着双手，然后搭在了我的肩膀上"
    who "那. . .要不要考虑一下加入我的创作演绎部. . ."
    ch "嗯. . .好. . .也可以试试？. . ."
    hide xy size2 a2 happy
    show xy size2 a2 normal:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with Dissolve(0.2)
    who "？"
    hide xy size2 a2 normal
    show xy size2 a2 perspire:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with Dissolve(0.2)
    who "！！！"
    "学姐好像是注意到了我尴尬的神情，脸一下涨得通红，然后很快把手抽下来"
    hide xy size2 a2 perspire
    show xy size2 a2 littlesad:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with Dissolve(0.2)
    who "抱歉抱歉"
    who "失礼了"
    who "我一直想找一位中国的同学给我指点一下"
    "搓着双手的学姐像是犯错事的小孩一样"
    "就连道歉都这么惹人怜爱. . ."
    "真的是那种高高在上的“西野公主”吗？看上去完全不像诶. . ."
    ch "没事的，你又没有犯什么错. . ."
    hide xy size2 a2 littlesad
    show xy size2 a2 happy:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with Dissolve(0.2)
    who "这样吗. . .太好了. . ."
    hide xy size2 a2 happy
    show xy size2 a2 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with Dissolve(0.2)
    who "容许我自我介绍一下. . ."
    xy "我的名字叫西野玥奈"
    xy "现在是四年级robot制造技术兼交叉演出学院的学生. . ."
    "西野玥奈. . "
    "是个非常好听的名字欸"
    "等等. . ."
    "居然同时在两个学院上课？！"

    #（此时镜头从下到上扫视西野玥奈）

    "明明一个专业的课程就已经多到令人望而却步了. . .这么刻苦的大小姐，恐怕也太厉害了一点吧. . ."
    xy size2 a2 perspire"有什么问题吗. . ."
    "看着我表情的微妙变化，西野学姐似乎是从中读出了某些含义"
    ch "咳咳，没问题的"
    ch "我叫海川渡，也在修习机器人制造技术"
    ch "以后请多指教了"
    xy size2 a2 smile "海川渡是吗. . .请多指教了！"
    xy "机器人. . ."
    "西野玥奈好像是突然想起了什么，飘忽不定的眼神，似乎是在刻意避开着我"  #（此时注意西野玥奈立绘表情的转变）
    xy size2 a2 littlesad"那个. . ."
    xy "开学典礼的演讲…？果然很糟糕吧"
    "西野学姐的双手不停地在胸口前摩擦着，看上去很是焦虑的样子"
    "一时之间，我不知道该用什么样的话回应她. . .虽然我认为在演讲上仍然有很多不足的地方. . ."
    "但也不至于到糟糕的地步吧"
    ch "嗯. . ."
    ch "原来是指那个演讲吗？"
    ch "我觉得. . ."
    ch "真的很棒！"
    ch "至少西野学姐大胆地讲出了自己的心里话，自己热爱的东西"
    ch "来东番高大的同学，我想也没有那种目标清晰，观点坚定的人吧. . .至少我是这样的"
    ch "在我看来，这样的演讲是我很喜欢的！"
    "西野学姐抬头望向我，在她的眼中，我似乎看到了点点的亮光在不断跃动"
    xy size2 a2 smile2"真的吗？"
    xy "谢谢！"
    "明明才刚认识，她怎么有种完全被感动到的感觉. . ."
    xy size2 a2 littlesad"明明是这么正式的演讲. . ."
    xy "说出这样的话，还是好难"
    "小声嘀咕的西野似乎还是很计较自己的那场“失败”的演讲"
    ch "呃. . ."
    "只是过来咨询“创作演绎部”的我，也完全没有想到事情会按照这样的方式展开"
    "在这个时候，转移话题是最好的选择"
    ch "加入‘创作演绎部’的话，有什么‘能力考察’的测试吗. . ."
    xy size2 a2 normal"‘能力考察’？那是什么东西呀"  #（立绘转为疑问脸，可适当增加效果）
    ch "嗯. . .简单来说的话，就是类似于那种‘资格考试’的感觉"
    xy size2 a2 smile"没有哦"  #（立绘转为微笑脸）
    xy "倒不如说，这是‘演出爱好者’的同好会"
    xy "因为才成立不久，部门里面也没有几位成员. . ."
    xy "找到像海川君这样优秀的同学才是我最希望的！"
    ch "原来如此"
    ch "虽然我也不是很‘优秀’的说. . .对演出和古典乐只是略懂皮毛而已"
    xy size2 a2 smile2"没关系的，我们一起进步吧"  #（立绘：闭眼微笑脸）
    ch "真是治愈的笑容啊. . ."
    xy size2 a2 smile"诶，你刚刚说什么呀？"
    ch "没什么的没什么的"
    "幸好我刚才说的是纯中文. . .说出来的话，会太尴尬了吧. . ."
    xy size2 a2 happy"要不去我的演出舞台看一下？"
    ch "可以啊"
    "遇到西野家的大小姐，完完全全是超出我意料之外的事情"
    "而且还是这样一个不起眼的部门. . ."
    "我又一次想到了宣传手册上的那几张看上去极为简陋和朴实的部活照片，似乎已经预感到了接下来西野学姐要带我去的地方. . ."
    xy size2 a2 smile"走吧"
    "随着西野玥奈拉开帐篷后的幕布，一个小门呈现在我的面前"
    "这个方向，好像是. . ."

    #（场景转换，黑幕转场，来到了东番高大的礼堂内，也是演出舞台。具体背景参考主催的样图：演出厅）
    hide booth 
    hide xy size2 a2 smile
    with tran_lf
    show hall with tran_lf
    "映入我眼帘的，是最开始机器人制造技术的迎新会的礼堂兼演出舞台"
    ch "这个不是. . .？"
    show xy size2 a2 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with dissolve
    xy "没错"
    xy "是之前迎新时使用的舞台"
    xy "这里不仅可以用于表演，还可以举办很多别的活动哦"
    xy "我们的部活以后可以随时在这里开展了"
    ch "学校的场地，真的可以随便使用吗. . ."
    xy size2 a2 smile2"没事的"  #微笑脸
    xy "应该是我们家和学校共同的场地"
    ch ". . ."
    "对于她这种富裕的家庭来说，给学校捐赠一两座演出厅好像确实没有什么问题. . ."
    xy size2 a2 smile"既然都来了，海川君想要尝试‘试演’吗？"
    ch "‘试演’？是说让我在台上即兴表演的那种感觉吗？"
    xy size2 a2 happy"嗯！"
    hide xy size2 a2 happy with dissolve
    #（黑幕转场，背景转换：东番高大的舞台上，播放效果音：“嘎吱嘎吱”，快速走上木质台阶声音的那种感觉）

    "就这样被西野学姐一路推搡着，我很快便站在了大舞台上"
    "尽管在高中的社团我有过类似的演出经验. . ."
    "但这么大的舞台. . .好像对我来说还是第一次"
    "在剧院周围的工作人员都停下了手中的事情，向我投来了一股好奇的目光，他们似乎对我接下来要表演什么产生了浓厚的兴趣"
    "好尴尬. . ."
    ch "所以说，是只有我一个角色在台上表演吗？"
    show xy size2 a2 happy:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with Dissolve(0.2)
    xy "请放心，这是自然会有的. . ."
    xy size2 a2 smile"那么，就有请我们的女嘉宾！"
    hide xy size2 a2 smile with dissolve
    show cx size2 a3 smile:
        xalign 0.2
        yalign 1.0
        zoom 1.3
    with dissolve
    "随着西野的手一挥动，另一侧的红幕应声落下，在那一片暗淡的灯光里，我似乎看到了一个若隐若现的女生站在那里. . ."
    "银白色的长发披在她制服的两侧，她也向我投来目光，浅浅地微笑着. . ."
    ch "那是. . ."
    ch "初咲恋柚？！！"
    "丝毫没有忍住惊讶的情绪，我直接大声地呼喊了出来"
    "可是. . .她为什么又会出现在这里呢？"
    "好像一切都在预料之外，但都似乎尽在预料之中"
    cq size2 a3 happy"请多指教噢，主，上，大，人~"
    ch "请. . .多. . .多指教"
    "被一群以日语为母语的观众夹杂着，一种不知所从感忽然占据了我的内心"
    "不对. . .还裹挟着那种角色扮演被发现的那种无比羞耻感. . ."
    "最关键的是作为机器人的初咲恋柚并没有意识到. . ."
    "她眨了眨眼睛，又朝向我做出了一个舞会上常见的行礼的动作——用两手夹住短裙裙摆的两端，双腿微曲"
    "反常于平常的初咲，今天的她完全就是一个成熟而又极会调侃的女性"
    cq size2 a3 smile"哎呀呀，主人的脸真的是通红呢~"
    ch "啊，是这样吗？"
    "因模糊于舞台灯照射而晕眩的感官，我完全不清楚我自己到底处于一种什么样的状态..."
    "甚至可以说，我整个人完全处在一种‘飘飘忽忽’的氛围中"
    "在初咲的‘引导’下，我不自觉捂住了自己的脸，生怕自己有什么失态的地方"
    cq size2 a3 happy"嘿嘿，单纯的主人果然被我骗到了~"
    show xy size3 a1 smile:
        xalign 0.9
        yalign 1.0
        zoom 1.2
    with dissolve
    xy "原来是叫‘初咲恋柚’啊. . ."
    xy "要不. . .我们开始来即兴试演？"
    cq size2 a3 smile"对哦，今天来主要是加入创作演绎部！"
    cq size2 a3 happy"还正好遇上了主人，非常幸运呢！"
    ch ". . ."
    xy "好啦，那就现在开始吧，两位都有什么问题吗？"
    cq size2 a3 smile"没有问题"
    ch "没有"
    xy "第一个需要即兴试演的剧情是——"
    xy size2 a2 happy"充满青春的校园情感剧~start！"

    #（此处切bgm：演出时间！！！）

    "在西野学姐说完后，背景装潢用的幕布很快随着电动机的拉动移动到两侧，巨大的光电全息显示器在舞台上投影出了一个生动复原的教室背景"
    hide xy size2 a2 happy
    hide cx size2 a3 happy
    with Dissolve(0.2)
    hide hall with pixellate
    show classroom day with pixellate
    #（此时场景转换，从舞台的背景变成高中教室的背景）

    "伴随着背景音乐的嘈杂声，仿佛我真的回到了在高中的某个课间，正惬意地享受着属于我自己的时间"
    "话说，这个布局看起来就是一个真实的教室. . ."
    "而且站在我面前的，就是一个从高中里走出来的美少女"
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with dissolve
    cq "学长！"
    "初咲站在舞台的另一端，用双手纂成喇叭状向我遥遥地呼喊着"
    "看样子. . .她是把自己当成了我的“学妹”"
    "被初咲以这样的方式呼喊，这种感觉有点微妙，又有点奇怪"
    cq size2 a3 happy"学长，我们一起回家吧？"

    #（前面立绘隐去，此时出现立绘，初咲的微笑脸）

    "面前的初咲，再次用她习惯性盯着我看的眼神打量着我"
    "看样子. . .“元气学妹”这样的标签还真是蛮符合她的"
    cq size2 a4 little_serious"学长，你怎么不理我啊？？"  #（此时浮现出的是撅嘴表情）
    "其实完全是因为还没有习惯这种夸张的表演方式，让尴尬的我一时半会儿不知道该用怎样的语言来答复初咲. . ."
    cq "呐…是不是还在生我的气啊"  #（此时浮现出的是撅嘴表情）
    cq size2 a4 sad"人家上次也不是故意的嘛…还不是学长先…"  #（此时浮现出的是闭眼竖起一根手指的动作）
    ch "喂喂！不要乱说啊！"
    "看起来，不给初咲一点回应的话应该是不会让她消停下来吧. . ."
    "而且. . .舞台下，西野学姐也正在期待着我的演出. . ."
    ch "咳咳"
    ch "那就一起回去吧，刚好今天也没有社团活动，没有值班"
    cq size2 a3 happy"啊...动物终于说话了"
    ch "喂喂！这样的话也太没礼貌了一点吧！还有‘动物’是怎样轻蔑的称呼啊喂！"
    "我把手做成了劈刀状，轻轻地扣在初咲恋柚的脑门上"
    cq size2 a4 sad"哎哟…疼. . ."  #（此时的表情是>_<）
    ch "走吧"
    "我随手抄起舞台上一个书包状的道具，搭在自己的背后，然后慢慢走向投影出的门"
    cq size2 a3 happy"我来了！"
    "初咲从我的身后突然超到了我的面前，还回头调皮地朝我吐了吐舌头"

    hide cx size2 a3 happy with Dissolve(0.2)
    hide classroom day with pixellate
    show street day with pixellate
    #（场景变化：从这个高中教室转换到了街道边的场景）
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with dissolve
    "随着我们走出这道“虚拟的门”后，显示仪上的光束立刻发生了色彩斑斓的变化，场景从室内变换到了室外"
    cq "学长"
    "走在我面前的初咲突然停住了脚步，背对着我这样说道"
    ch "怎么了？"
    cq size2 a4 little_serious"那个. . .我有一句话想和学长说！"
    "初咲的双手在裙摆前不断摩擦着，看上去显得极为不安的样子"
    "未免. . .这也太真实点了吧？"
    ch ". . ."
    ch "你说吧"
    cq "学长明年就会毕业，然后从学校离开对吧？"
    ch "是这样的"
    cq size2 a4 sad"也就是明年. . .我再也不能见到学长了"
    ch ". . . . . ."
    cq size2 a4 little_serious"我. ..我有句很重要的话对学长说！"
    "初咲通红的脸蛋上写满了“犹豫”和“期待”"
    "从她的神情中我似乎猜到了她的下一句话是什么. . ."
    cq size2 a3 happy"要不学长留级一年？"
    ch "蛤？"
    cq "这样我们就可以继续玩耍了！"  #（表情是笑脸）
    ch "这是怎么可能的事情啊喂！"
    "这家伙. . .怎么不按照常规来啊. . ."
    xy "咔！试演第一阶段到此结束"
    hide cx size2 a3 happy
    hide street
    with pixellate
    show hall
    with pixellate
    "很及时地，西野学姐打断了我们的饰演第一幕"
    "因为在演出上还不熟悉初咲的习惯. . .第一幕即兴试演让我不自然地很有些尴尬"
    show xy size2 a2 happy:
        xalign 0.2
        yalign 1.0
        zoom 1.2
    show cx size2 a3 smile:
        xalign 0.8
        yalign 1.0
        zoom 1.3
    with dissolve
    xy "看起来两边都很努力呢，不错不错"
    xy size2 a2 smile"试演效果完全超过了我的预期"
    xy "尤其是初咲同学，你的演出放得很开，应该说. . ."
    xy size2 a2 happy"真的很具有演出天赋"

    cq size2 a3 happy"真的吗？！"
    cq "看来我还是很有希望的呢，哼哼. . ."
    jump episode2_2


