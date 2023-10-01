; Turns typed pinyin into Chinese characters.
; Supported characters follow my lessons
; If more than one character corresponds to the same pinyin, 
; then they are chained together such that after typing the
; pinyin, repeatedly pressing the EndChar will loop between
; the valid options.  At present, no major consideration
; is given to the order in which these characters appear.

; Required to let one hotstring's output be another hotstring's input
#InputLevel 1

; Type the endchar to activate any given Hotstring
#Hotstring EndChars \

; ALT+X, suspend all hotstrings
#SuspendExempt
!x::Suspend -1
#SuspendExempt False

; Removes the endchar you typed to activate the Hotstring
#Hotstring o

; Hotstring works even if immediately preceded by an alphanumeric character
#Hotstring ?

; Don't erase the hotstring because it won't all be there - because of intentional interactions with the main Hotstrings file converting pinyin
#Hotstring B0

; Makes all hotstrings execute their output instead of sending it
; Usually recommended against but 100% of Hotstrings in this file should execute Out()
#Hotstring X

; Workaround because an auto-replace hotstring's output can't trigger another hotstring, but this can
Out(output) {
	SendEvent output
}

; Chinese characters

; ào
::a``\o::Out("{bs 2}澳")

; bā
::ba-\::Out("{bs 2}八")

; bǎi
::bav\i::Out("{bs 3}百")

; bài
::ba``\i::Out("{bs 3}拜")

; bāo
::ba-\o::Out("{bs 3}包") ; bag

; bǐng
::biv\ng::Out("{bs 4}饼")

; bō
::bo-\::Out("{bs 2}菠")

; bù
::bu``\::Out("{bs 2}不") ; not

; chá
::cha'\::Out("{bs 3}茶") ; tea

; chī
::chi-\::Out("{bs 3}吃") ; to eat

; dà
::da``\::Out("{bs 2}大")

; dàn
::da`\n::Out("{bs 3}蛋") ; egg (generic)

; dōu
::do-\u::Out("{bs 3}都") ; both; all

; èr
::e``\r::Out("{bs 2}二")

; fēi
::fe-\i::Out("{bs 3}啡")

; gàn
::ga``\n::Out("{bs 3}干")

; gān
::ga-\n::Out("{bs 3}干")

; gāo
::ga-\o::Out("{bs 3}高")

; guā
::gua-\::Out("{bs 3}瓜")

; guó
::guo'\::Out("{bs 3}国") ; country 

; guǒ
::guov\::Out("{bs 3}果") ; fruit

; hāi
::ha-\i::Out("{bs 3}嗨")

; hàn
::ha``\n::Out("{bs 3}汉") ; Chinese (language); Han ethnic group

; hǎo
::hav\o::Out("{bs 3}好") ; good

; hé
::he'\::Out("{bs 2}和") ; and (to link nouns only)

; hē
::he-\::Out("{bs 2}喝") ; to drink

; hēi
::he-\i::Out("{bs 3}嘿")

; hěn
::hev\n::Out("{bs 3}很")

; huá
::hua'\::Out("{bs 3}华")

; huan
::huan::Out("{bs 4}欢")

; jī
::ji-\::Out("{bs 2}鸡") ; chicken

; jiàn
::jia``\n::Out("{bs 4}见") ; see

; jiào
::jia``\o::Out("{bs 4}叫")

; jiǔ
::jiuv\::Out("{bs 3}九")
::九::Out("{bs 1}酒") ; alcohol; liquor
::酒::Out("{bs 1}九")

; kā
::ka-\::Out("{bs 2}咖")

; kě
::kev\::Out("{bs 2}可")

; la
::la::Out("{bs 2}啦")

; lán
::la'\n::Out("{bs 3}兰")

; le
::le::Out("{bs 2}了")

; lè
::le``\::Out("{bs 2}乐")

; lǐ
::liv\::Out("{bs 2}李")
::李::Out("{bs 1}里")
::里::Out("{bs 1}李")

; lì
::li``\::Out("{bs 2}利")

; líng
::li'\ng::Out("{bs 4}零")

; liù
::liu``\::Out("{bs 3}六")

; lóng
::lo'\ng::Out("{bs 4}龙")

; luó
::luo'\::Out("{bs 3}萝")

; ma
::ma::Out("{bs 2}吗") ; question particle for "yes-no" questions

; mǎi
::mav\i::Out("{bs 3}买") ; to buy

; màn
::ma``\n::Out("{bs 3}慢")

; máng
::ma'\ng::Out("{bs 4}芒")

; me
::me::Out("{bs 2}么")

; men
::men::Out("{bs 3}们") ; plural marker for people

; měi
::mev\i::Out("{bs 3}美") ; beautiful

; miàn
::mia`\n::Out("{bs 4}面") ; flour

; míng
::mi'\ng::Out("{bs 4}名")
::名::Out("{bs 1}明")
::明::Out("{bs 1}名")

; nǎ
::nav\::Out("{bs 2}哪")

; nǎi
::nav\i::Out("{bs 3}奶") ; milk (generic)

; ne
::ne::Out("{bs 2}呢")

; nǐ
::niv\::Out("{bs 2}你") ; you (singular)

; niú
::niu'\::Out("{bs 3}牛") ; cow; ox

; pí
::pi'\::Out("{bs 2}啤")

; píng
::pi'\ng::Out("{bs 4}苹") ; apple

; qī
::qi-\::Out("{bs 2}七")

; qù
::qu``\::Out("{bs 2}去")

; rèn
::re``\n::Out("{bs 3}认")

; rén
::re'\n::Out("{bs 3}人") ; person

; sān
::sa-\n::Out("{bs 3}三")

; shén
::she'\n::Out("{bs 4}什")

; shí
::shi'\::Out("{bs 3}十")
::十::Out("{bs 1}识")
::识::Out("{bs 1}十")

; shì
::shi``\::Out("{bs 3}是") ; to be

; shuǐ
::shuiv\::Out("{bs 4}水") ; water

; shuō
::shuo-\::Out("{bs 4}说") ; to speak; to say

; sì
::si``\::Out("{bs 2}四")

; tā
::ta-\::Out("{bs 2}他") ; he; him
::他::Out("{bs 1}她") ; she; her
::她::Out("{bs 1}它") ; it
::它::Out("{bs 1}他") ; he; him

; wáng
::wa'\ng::Out("{bs 4}王")

; wǒ
::wov\::Out("{bs 2}我") ; I; me

; wǔ
::wuv\::Out("{bs 2}五")

; xī
::xi-\::Out("{bs 2}西") ; west; western

; xǐ
::xiv\::Out("{bs 2}喜")

; xiǎng
::xiav\ng::Out("{bs 5}想") ; to want

; xiě
::xiev\::Out("{bs 3}写") ; to write

; xīn
::xi-\n::Out("{bs 3}新")

; xìng
::xi``\ng::Out("{bs 4}姓")
::姓::Out("{bs 1}兴")
::兴::Out("{bs 1}姓")

; xué
::xue'\::Out("{bs 3}学") ; to learn; to study

; yà
::ya``\::Out("{bs 2}亚")

; yě
::yev\::Out("{bs 2}也") ; also; too

; yī
::yi-\::Out("{bs 2}一")

; yīng
::yi-\ng::Out("{bs 4}英") ; heroic; outstanding

; yǔ
::yuv\::Out("{bs 2}语") ; language

; yuán
::yua'\n::Out("{bs 4}元")

; zài
::za``\i::Out("{bs 3}再") ; again

; zhāng
::zha-\ng::Out("{bs 5}张")

; zhī
::zhi-\::Out("{bs 3}汁") ; juice (generic)

; zhōng
::zho-\ng::Out("{bs 5}中") ; middle

; zì
::zi``\::Out("{bs 2}字") ; character

; zǒu
::zov\u::Out("{bs 3}走")