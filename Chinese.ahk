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
::a``\o::Out("{bs 2}澳") ; Used in 澳大利亚 (àodàlìyà) (Australia)

; bā
::ba-\::Out("{bs 2}八") ; eight; 8

; bái
::ba'\i::Out("{bs 3}拜") ; Used in 拜拜 (báibái) (bye-bye)

; bǎi
::bav\i::Out("{bs 3}百") ; hundred

; bāo
::ba-\o::Out("{bs 3}包") ; bag

; bēi
::be-\i::Out("{bs 3}杯") ; (measure word) glass; cup

; bǐng
::biv\ng::Out("{bs 4}饼") ; Used in 饼干 (bǐnggān) (cookie; biscuit)

; bō
::bo-\::Out("{bs 2}菠") ; Used in 菠萝 (bōluó) (pineapple)

; bù
::bu``\::Out("{bs 2}不") ; not

; chá
::cha'\::Out("{bs 3}茶") ; tea

; chī
::chi-\::Out("{bs 3}吃") ; to eat

; dà
::da``\::Out("{bs 2}大") ; big; large

; dàn
::da`\n::Out("{bs 3}蛋") ; egg (generic)

; dí
::di'\::Out("{bs 2}敌") ; enemy; foe

; dōu
::do-\u::Out("{bs 3}都") ; both; all

; duō
::duo-\::Out("{bs 3}多") ; Used in 多少 (duōshao) (how much); 多少 (duōshǎo) (how much)

; èr
::e``\r::Out("{bs 2}二") ; two; 2

; fàn
::fa`\n::Out("{bs 3}饭") ; Used in 米饭 (mǐfàn) ((cooked) rice)

; fēi
::fe-\i::Out("{bs 3}啡") ; Used in 咖啡 (kāfēi) (coffee)

; gān
::ga-\n::Out("{bs 3}干") ; dry

; gàn
::ga``\n::Out("{bs 3}干")

; gāo
::ga-\o::Out("{bs 3}高")

; gè
::ge``\::Out("{bs 2}个") ; measure word for people or objects in general

; guā
::gua-\::Out("{bs 3}瓜") ; melon

; guó
::guo'\::Out("{bs 3}国") ; country

; guǒ
::guov\::Out("{bs 3}果") ; fruit

; hāi
::ha-\i::Out("{bs 3}嗨") ; hi

; hàn
::ha``\n::Out("{bs 3}汉") ; Chinese (language); Han ethnic group

; hǎo
::hav\o::Out("{bs 3}好") ; good

; hē
::he-\::Out("{bs 2}喝") ; to drink

; hé
::he'\::Out("{bs 2}和") ; and (to link nouns only)

; hēi
::he-\i::Out("{bs 3}嘿") ; hey

; hěn
::hev\n::Out("{bs 3}很")

; huá
::hua'\::Out("{bs 3}华")

; huan
::huan::Out("{bs 4}欢") ; Used in 喜欢 (xǐhuan) (to like)

; huò
::huo``\::Out("{bs 3}货") ; Used in 售货员 (shòuhuòyuán) (salesperson; shop assistant)

; jī
::ji-\::Out("{bs 2}鸡") ; chicken

; jiàn
::jia``\n::Out("{bs 4}见") ; see

; jiāo
::jia-\o::Out("{bs 4}教") ; to teach

; jiǔ
::jiuv\::Out("{bs 3}九") ; nine; 9
::九::Out("{bs 1}酒") ; alcohol; liquor
::酒::Out("{bs 1}九")

; kā
::ka-\::Out("{bs 2}咖") ; Used in 咖啡 (kāfēi) (coffee)

; kě
::kev\::Out("{bs 2}可") ; Used in 可乐 (kělè) (cola); 可以 (kěyǐ) (can; may)

; kuài
::kua``\i::Out("{bs 4}块") ; yuan (currency)

; la
::la::Out("{bs 2}啦") ; Used in 我走啦 (wǒzǒula) (I'm heading off)

; lán
::la'\n::Out("{bs 3}兰") ; Used in 新西兰 (xīnxīlán) (New Zealand)

; lè
::le``\::Out("{bs 2}乐") ; Used in 可乐 (kělè) (cola)

; le
::le::Out("{bs 2}了")

; lǐ
::liv\::Out("{bs 2}李") ; Used in 哪李 (nǎlǐ) (where)
::李::Out("{bs 1}里")
::里::Out("{bs 1}李")

; lì
::li``\::Out("{bs 2}利") ; Used in 澳大利亚 (àodàlìyà) (Australia)

; li
::li::Out("{bs 2}丽") ; beautiful; pretty

; liàn
::lia``\n::Out("{bs 4}练") ; to practice

; liǎng
::liav\ng::Out("{bs 5}两") ; (before measure words) two; 2

; líng
::li'\ng::Out("{bs 4}零")

; liù
::liu``\::Out("{bs 3}六") ; six; 6

; lóng
::lo'\ng::Out("{bs 4}龙") ; dragon

; luó
::luo'\::Out("{bs 3}萝") ; Used in 菠萝 (bōluó) (pineapple)

; ma
::ma::Out("{bs 2}吗") ; question particle for "yes-no" questions; "question particle for ""yes-no"" questions"; question particle for 'yes-no' questions

; mǎi
::mav\i::Out("{bs 3}买") ; to buy

; màn
::ma``\n::Out("{bs 3}慢") ; slow; slowly

; máng
::ma'\ng::Out("{bs 4}芒") ; Used in 芒果 (mángguǒ) (mango)

; me
::me::Out("{bs 2}么")

; měi
::mev\i::Out("{bs 3}美") ; beautiful

; men
::men::Out("{bs 3}们") ; plural marker for people

; mǐ
::miv\::Out("{bs 2}米") ; Used in 米饭 (mǐfàn) ((cooked) rice)

; miàn
::mia`\n::Out("{bs 4}面") ; flour

; nǎ
::nav\::Out("{bs 2}哪") ; Used in 哪李 (nǎlǐ) (where)

; nǎi
::nav\i::Out("{bs 3}奶") ; milk (generic)

; ne
::ne::Out("{bs 2}呢")

; nǐ
::niv\::Out("{bs 2}你") ; you (singular)

; niú
::niu'\::Out("{bs 3}牛") ; cow; ox

; péng
::pe'\ng::Out("{bs 4}朋") ; Used in 朋友 (péngyǒu) (friend)

; pí
::pi'\::Out("{bs 2}啤") ; Used in 啤酒 (píjiǔ) (beer)

; píng
::pi'\ng::Out("{bs 4}苹") ; apple
::苹::Out("{bs 1}瓶") ; (measure word) bottle
::瓶::Out("{bs 1}苹") ; apple

; qī
::qi-\::Out("{bs 2}七") ; seven; 7

; qián
::qia'\n::Out("{bs 4}钱") ; money

; qíng
::qi'\ng::Out("{bs 4}情") ; Used in 情敌 (qíngdí) (love rival)

; qù
::qu``\::Out("{bs 2}去") ; to go; to leave

; rén
::re'\n::Out("{bs 3}人") ; person; person; people

; rèn
::re``\n::Out("{bs 3}认") ; Used in 认识 (rènshi) (to recognize; to know)

; sān
::sa-\n::Out("{bs 3}三") ; three; 3

; shǎo
::shav\o::Out("{bs 4}少") ; Used in 多少 (duōshǎo) (how much)

; shao
::shao::Out("{bs 4}少") ; Used in 多少 (duōshao) (how much)

; shén
::she'\n::Out("{bs 4}什")

; shēng
::she-\ng::Out("{bs 5}生") ; Used in 大学生 (dàxuéshēng) (college/university student); 学生 (xuéshēng) (student)

; shí
::shi'\::Out("{bs 3}十") ; ten; 10
::十::Out("{bs 1}识") ; Used in 认识 (rènshi) (to recognize; to know)
::识::Out("{bs 1}十")

; shì
::shi``\::Out("{bs 3}是") ; to be

; shi
::shi::Out("{bs 3}识") ; Used in 认识 (rènshi) (to recognize; to know)

; shòu
::sho``\u::Out("{bs 4}售") ; Used in 售货员 (shòuhuòyuán) (salesperson; shop assistant)

; shuǐ
::shuiv\::Out("{bs 4}水") ; water

; shuō
::shuo-\::Out("{bs 4}说") ; to speak; to say

; sì
::si``\::Out("{bs 2}四") ; four; 4

; tā
::ta-\::Out("{bs 2}他") ; he; him
::他::Out("{bs 1}她") ; she; her
::她::Out("{bs 1}它") ; it
::它::Out("{bs 1}他") ; he; him

; tóng
::to'\ng::Out("{bs 4}同") ; Used in 同学 (tóngxué) (classmates; schoolmates)

; wǒ
::wov\::Out("{bs 2}我") ; I; me

; wǔ
::wuv\::Out("{bs 2}五") ; five; 5

; xī
::xi-\::Out("{bs 2}西") ; west; western

; xǐ
::xiv\::Out("{bs 2}喜") ; Used in 喜欢 (xǐhuan) (to like)

; xiǎng
::xiav\ng::Out("{bs 5}想") ; to want

; xiě
::xiev\::Out("{bs 3}写") ; to write

; xīn
::xi-\n::Out("{bs 3}新") ; Used in 新西兰 (xīnxīlán) (New Zealand)

; xìng
::xi``\ng::Out("{bs 4}姓")
::姓::Out("{bs 1}兴")
::兴::Out("{bs 1}姓")

; xué
::xue'\::Out("{bs 3}学") ; to learn; to study

; yà
::ya``\::Out("{bs 2}亚") ; Used in 澳大利亚 (àodàlìyà) (Australia)

; yě
::yev\::Out("{bs 2}也") ; also; too

; yī
::yi-\::Out("{bs 2}一") ; one; 1

; yǐ
::yiv\::Out("{bs 2}以") ; Used in 可以 (kěyǐ) (can; may)

; yīng
::yi-\ng::Out("{bs 4}英") ; heroic; outstanding

; yǒu
::yov\u::Out("{bs 3}友") ; Used in 朋友 (péngyǒu) (friend)

; yǔ
::yuv\::Out("{bs 2}语") ; language

; yuán
::yua'\n::Out("{bs 4}元")
::元::Out("{bs 1}员") ; Used in 售货员 (shòuhuòyuán) (salesperson; shop assistant)
::员::Out("{bs 1}元")

; zài
::za``\i::Out("{bs 3}再") ; again

; zhāng
::zha-\ng::Out("{bs 5}张")

; zhè
::zhe``\::Out("{bs 3}这") ; this

; zhī
::zhi-\::Out("{bs 3}汁") ; juice (generic)

; zhōng
::zho-\ng::Out("{bs 5}中") ; middle

; zì
::zi``\::Out("{bs 2}字") ; character; character or word

; zǒu
::zov\u::Out("{bs 3}走") ; to walk; to go
