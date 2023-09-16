; Type the endchar to activate any given Hotstring
#Hotstring EndChars \

; ALT+Z, suspend all hotstrings
#SuspendExempt
!z::Suspend -1
#SuspendExempt False

; Removes the endchar you typed to activate the Hotstring
#Hotstring o

; Hotstring works even if immediately preceded by an alphanumeric character
#Hotstring ?

; Don't erase the hotstring because it won't all be there
#Hotstring B0



; Chinese characters
::za``\i::{bs 3}再
::jia``\n::{bs 4}见
::niv\::{bs 2}你
::hav\o::{bs 3}好
::yua'\n::{bs 4}元
::li'\ng::{bs 4}零
::yi-\::{bs 2}一
::e``\r::{bs 2}二
::sa-\n::{bs 3}三
::si``\::{bs 2}四
::wuv\::{bs 2}五
::liu``\::{bs 3}六
::qi-\::{bs 2}七
::ba-\::{bs 2}八
::jiuv\::{bs 3}九
::shi'\::{bs 3}十
::bav\i::{bs 3}百
::mi'\ng::{bs 4}名
::zi``\::{bs 2}字
::she'\n::{bs 4}什
::me::{bs 2}么
::xi``\ng::{bs 4}姓
::jia``\o::{bs 4}叫
::wov\::{bs 2}我
::ne::{bs 2}呢
::zha-\ng::{bs 5}张
::hua'\::{bs 3}华
::liv\::{bs 2}李
::wa'\ng::{bs 4}王