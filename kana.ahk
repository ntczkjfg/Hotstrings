; Required to let one hotstring's output be another hotstring's input
#InputLevel 1

; Type the endchar to activate any given Hotstring
#Hotstring EndChars \
endchar := "\"

; ALT+X, suspend all hotstrings
#SuspendExempt
!x::Suspend -1
#SuspendExempt False

; Removes the endchar you typed to activate the Hotstring
#Hotstring o

; Hotstring works even if immediately preceded by an alphanumeric character
#Hotstring ?

; Makes all hotstrings execute their output instead of sending it
; Usually recommended against but 100% of Hotstrings in this file should execute Out()
#Hotstring X

; Workaround because an auto-replace hotstring's output can't trigger another hotstring, but this can
Out(output) {
	SendEvent output
}

; Romanji to Hiragana
::dzi::Out("ぢ")
::dzu::Out("づ")
::shi::Out("し")
::chi::Out("ち")
::tsu::Out("つ")
::kya::Out("きゃ")
::kyu::Out("きゅ")
::kyo::Out("きょ")
::sha::Out("しゃ")
::shu::Out("しゅ")
::sho::Out("しょ")
::cha::Out("ちゃ")
::chu::Out("ちゅ")
::cho::Out("ちょ")
::nya::Out("にゃ")
::nyu::Out("にゅ")
::nyo::Out("にょ")
::hya::Out("ひゃ")
::hyu::Out("ひゅ")
::hyo::Out("ひょ")
::mya::Out("みゃ")
::myu::Out("みゅ")
::myo::Out("みょ")
::rya::Out("りゃ")
::ryu::Out("りゅ")
::ryo::Out("りょ")
::gya::Out("ぎゃ")
::gyu::Out("ぎゅ")
::gyo::Out("ぎょ")
::bya::Out("びゃ")
::byu::Out("びゅ")
::byo::Out("びょ")
::pya::Out("ぴゃ")
::pyu::Out("ぴゅ")
::pyo::Out("ぴょ")
::ka::Out("か")
::ki::Out("き")
::ku::Out("く")
::ke::Out("け")
::ko::Out("こ")
::sa::Out("さ")
::su::Out("す")
::se::Out("せ")
::so::Out("そ")
::ta::Out("た")
::te::Out("て")
::to::Out("と")
::na::Out("な")
::ni::Out("に")
::nu::Out("ぬ")
::ne::Out("ね")
::no::Out("の")
::ha::Out("は")
::hi::Out("ひ")
::fu::Out("ふ")
::he::Out("へ")
::ho::Out("ほ")
::ma::Out("ま")
::mi::Out("み")
::mu::Out("む")
::me::Out("め")
::mo::Out("も")
::ya::Out("や")
::yu::Out("ゆ")
::yo::Out("よ")
::ra::Out("ら")
::ri::Out("り")
::ru::Out("る")
::re::Out("れ")
::ro::Out("ろ")
::wa::Out("わ")
::wo::Out("を")
::ga::Out("が")
::gi::Out("ぎ")
::gu::Out("ぐ")
::ge::Out("げ")
::go::Out("ご")
::za::Out("ざ")
::ji::Out("じ")
::zu::Out("ず")
::ze::Out("ぜ")
::zo::Out("ぞ")
::da::Out("だ")
::de::Out("で")
::do::Out("ど")
::ba::Out("ば")
::bi::Out("び")
::bu::Out("ぶ")
::be::Out("べ")
::bo::Out("ぼ")
::pa::Out("ぱ")
::pi::Out("ぴ")
::pu::Out("ぷ")
::pe::Out("ぺ")
::po::Out("ぽ")
::ja::Out("じゃ")
::ju::Out("じゅ")
::jo::Out("じょ")
::vu::Out("ゔ")
::va::Out("ゔぁ")
::a::Out("あ")
::i::Out("い")
::u::Out("う")
::e::Out("え")
::o::Out("お")
::n::Out("ん")

; Hiragana to Katakana
::きゃ::Out("キャ")
::きゅ::Out("キュ")
::きょ::Out("キョ")
::しゃ::Out("シャ")
::しゅ::Out("シュ")
::しょ::Out("ショ")
::ちゃ::Out("チャ")
::ちゅ::Out("チュ")
::ちょ::Out("チョ")
::にゃ::Out("ニャ")
::にゅ::Out("ニュ")
::にょ::Out("ニョ")
::ひゃ::Out("ヒャ")
::ひゅ::Out("ヒュ")
::ひょ::Out("ヒョ")
::みゃ::Out("ミャ")
::みゅ::Out("ミュ")
::みょ::Out("ミョ")
::りゃ::Out("リャ")
::りゅ::Out("リュ")
::りょ::Out("リョ")
::ぎゃ::Out("ギャ")
::ぎゅ::Out("ギュ")
::ぎょ::Out("ギョ")
::びゃ::Out("ビャ")
::びゅ::Out("ビュ")
::びょ::Out("ビョ")
::ぴゃ::Out("ピャ")
::ぴゅ::Out("ピュ")
::ぴょ::Out("ピョ")
::じゃ::Out("ジャ")
::じゅ::Out("ジュ")
::じょ::Out("ジョ")
::ゔぁ::Out("ヴァ")
::ぢ::Out("ヂ")
::づ::Out("ヅ")
::し::Out("シ")
::ち::Out("チ")
::つ::Out("ツ")
::か::Out("カ")
::き::Out("キ")
::く::Out("ク")
::け::Out("ケ")
::こ::Out("コ")
::さ::Out("サ")
::す::Out("ス")
::せ::Out("セ")
::そ::Out("ソ")
::た::Out("タ")
::て::Out("テ")
::と::Out("ト")
::な::Out("ナ")
::に::Out("ニ")
::ぬ::Out("ヌ")
::ね::Out("ネ")
::の::Out("ノ")
::は::Out("ハ")
::ひ::Out("ヒ")
::ふ::Out("フ")
::へ::Out("ヘ")
::ほ::Out("ホ")
::ま::Out("マ")
::み::Out("ミ")
::む::Out("ム")
::め::Out("メ")
::も::Out("モ")
::や::Out("ヤ")
::ゆ::Out("ユ")
::よ::Out("ヨ")
::ら::Out("ラ")
::り::Out("リ")
::る::Out("ル")
::れ::Out("レ")
::ろ::Out("ロ")
::わ::Out("ワ")
::を::Out("ヲ")
::が::Out("ガ")
::ぎ::Out("ギ")
::ぐ::Out("グ")
::げ::Out("ゲ")
::ご::Out("ゴ")
::ざ::Out("ザ")
::じ::Out("ジ")
::ず::Out("ズ")
::ぜ::Out("ゼ")
::ぞ::Out("ゾ")
::だ::Out("ダ")
::で::Out("デ")
::ど::Out("ド")
::ば::Out("バ")
::び::Out("ビ")
::ぶ::Out("ブ")
::べ::Out("ベ")
::ぼ::Out("ボ")
::ぱ::Out("パ")
::ぴ::Out("ピ")
::ぷ::Out("プ")
::ぺ::Out("ペ")
::ぽ::Out("ポ")
::ゔ::Out("ヴ")
::あ::Out("ア")
::い::Out("イ")
::う::Out("ウ")
::え::Out("エ")
::お::Out("オ")
::ん::Out("ン")

; Katakana to Hiragana (For looping effect)
::キャ::Out("きゃ")
::キュ::Out("きゅ")
::キョ::Out("きょ")
::シャ::Out("しゃ")
::シュ::Out("しゅ")
::ショ::Out("しょ")
::チャ::Out("ちゃ")
::チュ::Out("ちゅ")
::チョ::Out("ちょ")
::ニャ::Out("にゃ")
::ニュ::Out("にゅ")
::ニョ::Out("にょ")
::ヒャ::Out("ひゃ")
::ヒュ::Out("ひゅ")
::ヒョ::Out("ひょ")
::ミャ::Out("みゃ")
::ミュ::Out("みゅ")
::ミョ::Out("みょ")
::リャ::Out("りゃ")
::リュ::Out("りゅ")
::リョ::Out("りょ")
::ギャ::Out("ぎゃ")
::ギュ::Out("ぎゅ")
::ギョ::Out("ぎょ")
::ビャ::Out("びゃ")
::ビュ::Out("びゅ")
::ビョ::Out("びょ")
::ピャ::Out("ぴゃ")
::ピュ::Out("ぴゅ")
::ピョ::Out("ぴょ")
::ジャ::Out("じゃ")
::ジュ::Out("じゅ")
::ジョ::Out("じょ")
::ヴァ::Out("ゔぁ")
::ヂ::Out("ぢ")
::ヅ::Out("づ")
::シ::Out("し")
::チ::Out("ち")
::ツ::Out("つ")
::カ::Out("か")
::キ::Out("き")
::ク::Out("く")
::ケ::Out("け")
::コ::Out("こ")
::サ::Out("さ")
::ス::Out("す")
::セ::Out("せ")
::ソ::Out("そ")
::タ::Out("た")
::テ::Out("て")
::ト::Out("と")
::ナ::Out("な")
::ニ::Out("に")
::ヌ::Out("ぬ")
::ネ::Out("ね")
::ノ::Out("の")
::ハ::Out("は")
::ヒ::Out("ひ")
::フ::Out("ふ")
::ヘ::Out("へ")
::ホ::Out("ほ")
::マ::Out("ま")
::ミ::Out("み")
::ム::Out("む")
::メ::Out("め")
::モ::Out("も")
::ヤ::Out("や")
::ユ::Out("ゆ")
::ヨ::Out("よ")
::ラ::Out("ら")
::リ::Out("り")
::ル::Out("る")
::レ::Out("れ")
::ロ::Out("ろ")
::ワ::Out("わ")
::ヲ::Out("を")
::ガ::Out("が")
::ギ::Out("ぎ")
::グ::Out("ぐ")
::ゲ::Out("げ")
::ゴ::Out("ご")
::ザ::Out("ざ")
::ジ::Out("じ")
::ズ::Out("ず")
::ゼ::Out("ぜ")
::ゾ::Out("ぞ")
::ダ::Out("だ")
::デ::Out("で")
::ド::Out("ど")
::バ::Out("ば")
::ビ::Out("び")
::ブ::Out("ぶ")
::ベ::Out("べ")
::ボ::Out("ぼ")
::パ::Out("ぱ")
::ピ::Out("ぴ")
::プ::Out("ぷ")
::ペ::Out("ぺ")
::ポ::Out("ぽ")
::ヴ::Out("ゔ")
::ア::Out("あ")
::イ::Out("い")
::ウ::Out("う")
::エ::Out("え")
::オ::Out("お")
::ン::Out("ん")

; Gathers user input and does some processing regarding it.  
; Did they type?  Paste?  Use from the clipboard?  
; Send too much or take too long?  How much needs to be backspaced?  
; Always backspace at least 1 for endchar.  Results are passed by reference so no returning needed.  
GatherInput(&text, &backspaceCount) {
	; Collects all input until endchar. Give up after L characters or T seconds.
	Suspend
	text := InputHook("MVL1000T90", endchar)
	text.Start()
	text.Wait()
	Suspend
	; Just give up if they took too long or typed too much
	If text.EndReason == "Max" Or text.EndReason == "Timeout" {
		text := ""
		backspaceCount := 0
		Return
	}
	text := text.Input
	; Handles pasting
	text := StrReplace(text, Chr(22), A_Clipboard)
	backspaceCount := StrLen(text) + 1
	If StrLen(text) == 0 { ; If they didn't type anything, take the text from the clipboard
		text := A_Clipboard
	}
	len := StrLen(text)
	text := StrReplace(text, "`r", "  ")
	text := StrReplace(text, "`n", "  ")
	If len > 1000 {
		Send "{bs 1}Too much text. Limit: 1000 characters. You sent " . len . ". "
		text := ""
		backspaceCount := 0
		Return
	}
}

::h:: {
	GatherInput(&text, &backspaceCount)
	
	text := StrReplace(text, "dzi", "ぢ")
	text := StrReplace(text, "dzu", "づ")
	text := StrReplace(text, "shi", "し")
	text := StrReplace(text, "chi", "ち")
	text := StrReplace(text, "tsu", "つ")
	text := StrReplace(text, "kya", "きゃ")
	text := StrReplace(text, "kyu", "きゅ")
	text := StrReplace(text, "kyo", "きょ")
	text := StrReplace(text, "sha", "しゃ")
	text := StrReplace(text, "shu", "しゅ")
	text := StrReplace(text, "sho", "しょ")
	text := StrReplace(text, "cha", "ちゃ")
	text := StrReplace(text, "chu", "ちゅ")
	text := StrReplace(text, "cho", "ちょ")
	text := StrReplace(text, "nya", "にゃ")
	text := StrReplace(text, "nyu", "にゅ")
	text := StrReplace(text, "nyo", "にょ")
	text := StrReplace(text, "hya", "ひゃ")
	text := StrReplace(text, "hyu", "ひゅ")
	text := StrReplace(text, "hyo", "ひょ")
	text := StrReplace(text, "mya", "みゃ")
	text := StrReplace(text, "myu", "みゅ")
	text := StrReplace(text, "myo", "みょ")
	text := StrReplace(text, "rya", "りゃ")
	text := StrReplace(text, "ryu", "りゅ")
	text := StrReplace(text, "ryo", "りょ")
	text := StrReplace(text, "gya", "ぎゃ")
	text := StrReplace(text, "gyu", "ぎゅ")
	text := StrReplace(text, "gyo", "ぎょ")
	text := StrReplace(text, "bya", "びゃ")
	text := StrReplace(text, "byu", "びゅ")
	text := StrReplace(text, "byo", "びょ")
	text := StrReplace(text, "pya", "ぴゃ")
	text := StrReplace(text, "pyu", "ぴゅ")
	text := StrReplace(text, "pyo", "ぴょ")
	text := StrReplace(text, "ka", "か")
	text := StrReplace(text, "ki", "き")
	text := StrReplace(text, "ku", "く")
	text := StrReplace(text, "ke", "け")
	text := StrReplace(text, "ko", "こ")
	text := StrReplace(text, "sa", "さ")
	text := StrReplace(text, "su", "す")
	text := StrReplace(text, "se", "せ")
	text := StrReplace(text, "so", "そ")
	text := StrReplace(text, "ta", "た")
	text := StrReplace(text, "te", "て")
	text := StrReplace(text, "to", "と")
	text := StrReplace(text, "na", "な")
	text := StrReplace(text, "ni", "に")
	text := StrReplace(text, "nu", "ぬ")
	text := StrReplace(text, "ne", "ね")
	text := StrReplace(text, "no", "の")
	text := StrReplace(text, "ha", "は")
	text := StrReplace(text, "hi", "ひ")
	text := StrReplace(text, "fu", "ふ")
	text := StrReplace(text, "he", "へ")
	text := StrReplace(text, "ho", "ほ")
	text := StrReplace(text, "ma", "ま")
	text := StrReplace(text, "mi", "み")
	text := StrReplace(text, "mu", "む")
	text := StrReplace(text, "me", "め")
	text := StrReplace(text, "mo", "も")
	text := StrReplace(text, "ya", "や")
	text := StrReplace(text, "yu", "ゆ")
	text := StrReplace(text, "yo", "よ")
	text := StrReplace(text, "ra", "ら")
	text := StrReplace(text, "ri", "り")
	text := StrReplace(text, "ru", "る")
	text := StrReplace(text, "re", "れ")
	text := StrReplace(text, "ro", "ろ")
	text := StrReplace(text, "wa", "わ")
	text := StrReplace(text, "wo", "を")
	text := StrReplace(text, "ga", "が")
	text := StrReplace(text, "gi", "ぎ")
	text := StrReplace(text, "gu", "ぐ")
	text := StrReplace(text, "ge", "げ")
	text := StrReplace(text, "go", "ご")
	text := StrReplace(text, "za", "ざ")
	text := StrReplace(text, "ji", "じ")
	text := StrReplace(text, "zu", "ず")
	text := StrReplace(text, "ze", "ぜ")
	text := StrReplace(text, "zo", "ぞ")
	text := StrReplace(text, "da", "だ")
	text := StrReplace(text, "de", "で")
	text := StrReplace(text, "do", "ど")
	text := StrReplace(text, "ba", "ば")
	text := StrReplace(text, "bi", "び")
	text := StrReplace(text, "bu", "ぶ")
	text := StrReplace(text, "be", "べ")
	text := StrReplace(text, "bo", "ぼ")
	text := StrReplace(text, "pa", "ぱ")
	text := StrReplace(text, "pi", "ぴ")
	text := StrReplace(text, "pu", "ぷ")
	text := StrReplace(text, "pe", "ぺ")
	text := StrReplace(text, "po", "ぽ")
	text := StrReplace(text, "ja", "じゃ")
	text := StrReplace(text, "ju", "じゅ")
	text := StrReplace(text, "jo", "じょ")
	text := StrReplace(text, "vu", "ゔ")
	text := StrReplace(text, "va", "ゔぁ")
	text := StrReplace(text, "a", "あ")
	text := StrReplace(text, "i", "い")
	text := StrReplace(text, "u", "う")
	text := StrReplace(text, "e", "え")
	text := StrReplace(text, "o", "お")
	text := StrReplace(text, "n", "ん")
	text := StrReplace(text, " ")
	
	Send "{bs " . backspaceCount . "}" . text
}

::k:: {
	GatherInput(&text, &backspaceCount)
	
	text := StrReplace(text, "dzi", "ヂ")
	text := StrReplace(text, "dzu", "ヅ")
	text := StrReplace(text, "shi", "シ")
	text := StrReplace(text, "chi", "チ")
	text := StrReplace(text, "tsu", "ツ")
	text := StrReplace(text, "kya", "キャ")
	text := StrReplace(text, "kyu", "キュ")
	text := StrReplace(text, "kyo", "キョ")
	text := StrReplace(text, "sha", "シャ")
	text := StrReplace(text, "shu", "シュ")
	text := StrReplace(text, "sho", "ショ")
	text := StrReplace(text, "cha", "チャ")
	text := StrReplace(text, "chu", "チュ")
	text := StrReplace(text, "cho", "チョ")
	text := StrReplace(text, "nya", "ニャ")
	text := StrReplace(text, "nyu", "ニュ")
	text := StrReplace(text, "nyo", "ニョ")
	text := StrReplace(text, "hya", "ヒャ")
	text := StrReplace(text, "hyu", "ヒュ")
	text := StrReplace(text, "hyo", "ヒョ")
	text := StrReplace(text, "mya", "ミャ")
	text := StrReplace(text, "myu", "ミュ")
	text := StrReplace(text, "myo", "ミョ")
	text := StrReplace(text, "rya", "リャ")
	text := StrReplace(text, "ryu", "リュ")
	text := StrReplace(text, "ryo", "リョ")
	text := StrReplace(text, "gya", "ギャ")
	text := StrReplace(text, "gyu", "ギュ")
	text := StrReplace(text, "gyo", "ギョ")
	text := StrReplace(text, "bya", "ビャ")
	text := StrReplace(text, "byu", "ビュ")
	text := StrReplace(text, "byo", "ビョ")
	text := StrReplace(text, "pya", "ピャ")
	text := StrReplace(text, "pyu", "ピュ")
	text := StrReplace(text, "pyo", "ピョ")
	text := StrReplace(text, "ka", "カ")
	text := StrReplace(text, "ki", "キ")
	text := StrReplace(text, "ku", "ク")
	text := StrReplace(text, "ke", "ケ")
	text := StrReplace(text, "ko", "コ")
	text := StrReplace(text, "sa", "サ")
	text := StrReplace(text, "su", "ス")
	text := StrReplace(text, "se", "セ")
	text := StrReplace(text, "so", "ソ")
	text := StrReplace(text, "ta", "タ")
	text := StrReplace(text, "te", "テ")
	text := StrReplace(text, "to", "ト")
	text := StrReplace(text, "na", "ナ")
	text := StrReplace(text, "ni", "ニ")
	text := StrReplace(text, "nu", "ヌ")
	text := StrReplace(text, "ne", "ネ")
	text := StrReplace(text, "no", "ノ")
	text := StrReplace(text, "ha", "ハ")
	text := StrReplace(text, "hi", "ヒ")
	text := StrReplace(text, "fu", "フ")
	text := StrReplace(text, "he", "ヘ")
	text := StrReplace(text, "ho", "ホ")
	text := StrReplace(text, "ma", "マ")
	text := StrReplace(text, "mi", "ミ")
	text := StrReplace(text, "mu", "ム")
	text := StrReplace(text, "me", "メ")
	text := StrReplace(text, "mo", "モ")
	text := StrReplace(text, "ya", "ヤ")
	text := StrReplace(text, "yu", "ユ")
	text := StrReplace(text, "yo", "ヨ")
	text := StrReplace(text, "ra", "ラ")
	text := StrReplace(text, "ri", "リ")
	text := StrReplace(text, "ru", "ル")
	text := StrReplace(text, "re", "レ")
	text := StrReplace(text, "ro", "ロ")
	text := StrReplace(text, "wa", "ワ")
	text := StrReplace(text, "wo", "ヲ")
	text := StrReplace(text, "ga", "ガ")
	text := StrReplace(text, "gi", "ギ")
	text := StrReplace(text, "gu", "グ")
	text := StrReplace(text, "ge", "ゲ")
	text := StrReplace(text, "go", "ゴ")
	text := StrReplace(text, "za", "ザ")
	text := StrReplace(text, "ji", "ジ")
	text := StrReplace(text, "zu", "ズ")
	text := StrReplace(text, "ze", "ゼ")
	text := StrReplace(text, "zo", "ゾ")
	text := StrReplace(text, "da", "ダ")
	text := StrReplace(text, "de", "デ")
	text := StrReplace(text, "do", "ド")
	text := StrReplace(text, "ba", "バ")
	text := StrReplace(text, "bi", "ビ")
	text := StrReplace(text, "bu", "ブ")
	text := StrReplace(text, "be", "ベ")
	text := StrReplace(text, "bo", "ボ")
	text := StrReplace(text, "pa", "パ")
	text := StrReplace(text, "pi", "ピ")
	text := StrReplace(text, "pu", "プ")
	text := StrReplace(text, "pe", "ペ")
	text := StrReplace(text, "po", "ポ")
	text := StrReplace(text, "ja", "ジャ")
	text := StrReplace(text, "ju", "ジュ")
	text := StrReplace(text, "jo", "ジョ")
	text := StrReplace(text, "vu", "ヴ")
	text := StrReplace(text, "va", "ヴァ")
	text := StrReplace(text, "a", "ア")
	text := StrReplace(text, "i", "イ")
	text := StrReplace(text, "u", "ウ")
	text := StrReplace(text, "e", "エ")
	text := StrReplace(text, "o", "オ")
	text := StrReplace(text, "n", "ン")
	text := StrReplace(text, " ")
	
	Send "{bs " . backspaceCount . "}" . text
}

::r:: {
	GatherInput(&text, &backspaceCount)
	
	text := StrReplace(text, "キャ", "kya")
	text := StrReplace(text, "キュ", "kyu")
	text := StrReplace(text, "キョ", "kyo")
	text := StrReplace(text, "シャ", "sha")
	text := StrReplace(text, "シュ", "shu")
	text := StrReplace(text, "ショ", "sho")
	text := StrReplace(text, "チャ", "cha")
	text := StrReplace(text, "チュ", "chu")
	text := StrReplace(text, "チョ", "cho")
	text := StrReplace(text, "ニャ", "nya")
	text := StrReplace(text, "ニュ", "nyu")
	text := StrReplace(text, "ニョ", "nyo")
	text := StrReplace(text, "ヒャ", "hya")
	text := StrReplace(text, "ヒュ", "hyu")
	text := StrReplace(text, "ヒョ", "hyo")
	text := StrReplace(text, "ミャ", "mya")
	text := StrReplace(text, "ミュ", "myu")
	text := StrReplace(text, "ミョ", "myo")
	text := StrReplace(text, "リャ", "rya")
	text := StrReplace(text, "リュ", "ryu")
	text := StrReplace(text, "リョ", "ryo")
	text := StrReplace(text, "ギャ", "gya")
	text := StrReplace(text, "ギュ", "gyu")
	text := StrReplace(text, "ギョ", "gyo")
	text := StrReplace(text, "ビャ", "bya")
	text := StrReplace(text, "ビュ", "byu")
	text := StrReplace(text, "ビョ", "byo")
	text := StrReplace(text, "ピャ", "pya")
	text := StrReplace(text, "ピュ", "pyu")
	text := StrReplace(text, "ピョ", "pyo")
	text := StrReplace(text, "ジャ", "ja")
	text := StrReplace(text, "ジュ", "ju")
	text := StrReplace(text, "ジョ", "jo")
	text := StrReplace(text, "きゃ", "kya")
	text := StrReplace(text, "きゅ", "kyu")
	text := StrReplace(text, "きょ", "kyo")
	text := StrReplace(text, "しゃ", "sha")
	text := StrReplace(text, "しゅ", "shu")
	text := StrReplace(text, "しょ", "sho")
	text := StrReplace(text, "ちゃ", "cha")
	text := StrReplace(text, "ちゅ", "chu")
	text := StrReplace(text, "ちょ", "cho")
	text := StrReplace(text, "にゃ", "nya")
	text := StrReplace(text, "にゅ", "nyu")
	text := StrReplace(text, "にょ", "nyo")
	text := StrReplace(text, "ひゃ", "hya")
	text := StrReplace(text, "ひゅ", "hyu")
	text := StrReplace(text, "ひょ", "hyo")
	text := StrReplace(text, "みゃ", "mya")
	text := StrReplace(text, "みゅ", "myu")
	text := StrReplace(text, "みょ", "myo")
	text := StrReplace(text, "りゃ", "rya")
	text := StrReplace(text, "りゅ", "ryu")
	text := StrReplace(text, "りょ", "ryo")
	text := StrReplace(text, "ぎゃ", "gya")
	text := StrReplace(text, "ぎゅ", "gyu")
	text := StrReplace(text, "ぎょ", "gyo")
	text := StrReplace(text, "びゃ", "bya")
	text := StrReplace(text, "びゅ", "byu")
	text := StrReplace(text, "びょ", "byo")
	text := StrReplace(text, "ぴゃ", "pya")
	text := StrReplace(text, "ぴゅ", "pyu")
	text := StrReplace(text, "ぴょ", "pyo")
	text := StrReplace(text, "じゃ", "ja")
	text := StrReplace(text, "じゅ", "ju")
	text := StrReplace(text, "じょ", "jo")
	text := StrReplace(text, "ゔぁ", "va")
	text := StrReplace(text, "ヴァ", "va")
	text := StrReplace(text, "ぢ", "dzi")
	text := StrReplace(text, "づ", "dzu")
	text := StrReplace(text, "シ", "shi")
	text := StrReplace(text, "チ", "chi")
	text := StrReplace(text, "ツ", "tsu")
	text := StrReplace(text, "カ", "ka")
	text := StrReplace(text, "キ", "ki")
	text := StrReplace(text, "ク", "ku")
	text := StrReplace(text, "ケ", "ke")
	text := StrReplace(text, "コ", "ko")
	text := StrReplace(text, "サ", "sa")
	text := StrReplace(text, "ス", "su")
	text := StrReplace(text, "セ", "se")
	text := StrReplace(text, "ソ", "so")
	text := StrReplace(text, "タ", "ta")
	text := StrReplace(text, "テ", "te")
	text := StrReplace(text, "ト", "to")
	text := StrReplace(text, "ナ", "na")
	text := StrReplace(text, "ニ", "ni")
	text := StrReplace(text, "ヌ", "nu")
	text := StrReplace(text, "ネ", "ne")
	text := StrReplace(text, "ノ", "no")
	text := StrReplace(text, "ハ", "ha")
	text := StrReplace(text, "ヒ", "hi")
	text := StrReplace(text, "フ", "fu")
	text := StrReplace(text, "ヘ", "he")
	text := StrReplace(text, "ホ", "ho")
	text := StrReplace(text, "マ", "ma")
	text := StrReplace(text, "ミ", "mi")
	text := StrReplace(text, "ム", "mu")
	text := StrReplace(text, "メ", "me")
	text := StrReplace(text, "モ", "mo")
	text := StrReplace(text, "ヤ", "ya")
	text := StrReplace(text, "ユ", "yu")
	text := StrReplace(text, "ヨ", "yo")
	text := StrReplace(text, "ラ", "ra")
	text := StrReplace(text, "リ", "ri")
	text := StrReplace(text, "ル", "ru")
	text := StrReplace(text, "レ", "re")
	text := StrReplace(text, "ロ", "ro")
	text := StrReplace(text, "ワ", "wa")
	text := StrReplace(text, "ヲ", "wo")
	text := StrReplace(text, "ガ", "ga")
	text := StrReplace(text, "ギ", "gi")
	text := StrReplace(text, "グ", "gu")
	text := StrReplace(text, "ゲ", "ge")
	text := StrReplace(text, "ゴ", "go")
	text := StrReplace(text, "ザ", "za")
	text := StrReplace(text, "ジ", "ji")
	text := StrReplace(text, "ズ", "zu")
	text := StrReplace(text, "ゼ", "ze")
	text := StrReplace(text, "ゾ", "zo")
	text := StrReplace(text, "ダ", "da")
	text := StrReplace(text, "デ", "de")
	text := StrReplace(text, "ド", "do")
	text := StrReplace(text, "バ", "ba")
	text := StrReplace(text, "ビ", "bi")
	text := StrReplace(text, "ブ", "bu")
	text := StrReplace(text, "ベ", "be")
	text := StrReplace(text, "ボ", "bo")
	text := StrReplace(text, "パ", "pa")
	text := StrReplace(text, "ピ", "pi")
	text := StrReplace(text, "プ", "pu")
	text := StrReplace(text, "ペ", "pe")
	text := StrReplace(text, "ポ", "po")
	text := StrReplace(text, "ヴ", "vu")
	text := StrReplace(text, "ア", "a")
	text := StrReplace(text, "イ", "i")
	text := StrReplace(text, "ウ", "u")
	text := StrReplace(text, "エ", "e")
	text := StrReplace(text, "オ", "o")
	text := StrReplace(text, "ン", "n")
	text := StrReplace(text, "ヂ", "dzi")
	text := StrReplace(text, "ヅ", "dzu")
	text := StrReplace(text, "し", "shi")
	text := StrReplace(text, "ち", "chi")
	text := StrReplace(text, "つ", "tsu")
	text := StrReplace(text, "か", "ka")
	text := StrReplace(text, "き", "ki")
	text := StrReplace(text, "く", "ku")
	text := StrReplace(text, "け", "ke")
	text := StrReplace(text, "こ", "ko")
	text := StrReplace(text, "さ", "sa")
	text := StrReplace(text, "す", "su")
	text := StrReplace(text, "せ", "se")
	text := StrReplace(text, "そ", "so")
	text := StrReplace(text, "た", "ta")
	text := StrReplace(text, "て", "te")
	text := StrReplace(text, "と", "to")
	text := StrReplace(text, "な", "na")
	text := StrReplace(text, "に", "ni")
	text := StrReplace(text, "ぬ", "nu")
	text := StrReplace(text, "ね", "ne")
	text := StrReplace(text, "の", "no")
	text := StrReplace(text, "は", "ha")
	text := StrReplace(text, "ひ", "hi")
	text := StrReplace(text, "ふ", "fu")
	text := StrReplace(text, "へ", "he")
	text := StrReplace(text, "ほ", "ho")
	text := StrReplace(text, "ま", "ma")
	text := StrReplace(text, "み", "mi")
	text := StrReplace(text, "む", "mu")
	text := StrReplace(text, "め", "me")
	text := StrReplace(text, "も", "mo")
	text := StrReplace(text, "や", "ya")
	text := StrReplace(text, "ゆ", "yu")
	text := StrReplace(text, "よ", "yo")
	text := StrReplace(text, "ら", "ra")
	text := StrReplace(text, "り", "ri")
	text := StrReplace(text, "る", "ru")
	text := StrReplace(text, "れ", "re")
	text := StrReplace(text, "ろ", "ro")
	text := StrReplace(text, "わ", "wa")
	text := StrReplace(text, "を", "wo")
	text := StrReplace(text, "が", "ga")
	text := StrReplace(text, "ぎ", "gi")
	text := StrReplace(text, "ぐ", "gu")
	text := StrReplace(text, "げ", "ge")
	text := StrReplace(text, "ご", "go")
	text := StrReplace(text, "ざ", "za")
	text := StrReplace(text, "じ", "ji")
	text := StrReplace(text, "ず", "zu")
	text := StrReplace(text, "ぜ", "ze")
	text := StrReplace(text, "ぞ", "zo")
	text := StrReplace(text, "だ", "da")
	text := StrReplace(text, "で", "de")
	text := StrReplace(text, "ど", "do")
	text := StrReplace(text, "ば", "ba")
	text := StrReplace(text, "び", "bi")
	text := StrReplace(text, "ぶ", "bu")
	text := StrReplace(text, "べ", "be")
	text := StrReplace(text, "ぼ", "bo")
	text := StrReplace(text, "ぱ", "pa")
	text := StrReplace(text, "ぴ", "pi")
	text := StrReplace(text, "ぷ", "pu")
	text := StrReplace(text, "ぺ", "pe")
	text := StrReplace(text, "ぽ", "po")
	text := StrReplace(text, "ゔ", "vu")
	text := StrReplace(text, "あ", "a")
	text := StrReplace(text, "い", "i")
	text := StrReplace(text, "う", "u")
	text := StrReplace(text, "え", "e")
	text := StrReplace(text, "お", "o")
	text := StrReplace(text, "ん", "n")
	
	Send "{bs " . backspaceCount . "}" . text
}

; The following table contains all supported hiragana, katakana, and romanji characters
; Just in case changes are ever needed
; Goes in order:  Hiragana, Katakana, Romanji
; Basic
; あ ア a
; い イ i
; う ウ u
; え エ e
; お オ o
; か カ ka
; き キ ki
; く ク ku
; け ケ ke
; こ コ ko
; さ サ sa
; し シ shi
; す ス su
; せ セ se
; そ ソ so
; た タ ta
; ち チ chi
; つ ツ tsu
; て テ te
; と ト to
; な ナ na
; に ニ ni
; ぬ ヌ nu
; ね ネ ne
; の ノ no
; は ハ ha
; ひ ヒ hi
; ふ フ fu
; へ ヘ he
; ほ ホ ho
; ま マ ma
; み ミ mi
; む ム mu
; め メ me
; も モ mo
; や ヤ ya
; ゆ ユ yu
; よ ヨ yo
; ら ラ ra
; り リ ri
; る ル ru
; れ レ re
; ろ ロ ro
; わ ワ wa
; を ヲ wo
; ん ン n

; Dakuon
; が ガ ga
; ぎ ギ gi
; ぐ グ gu
; げ ゲ ge
; ご ゴ go
; ざ ザ za
; じ ジ ji
; ず ズ zu
; ぜ ゼ ze
; ぞ ゾ zo
; だ ダ da
; ぢ ヂ dzi
; づ ヅ dzu
; で デ de
; ど ド do
; ば バ ba
; び ビ bi
; ぶ ブ bu
; べ ベ be
; ぼ ボ bo
; ぱ パ pa
; ぴ ピ pi
; ぷ プ pu
; ぺ ペ pe
; ぽ ポ po

; Combo
; きゃ キャ kya
; きゅ キュ kyu
; きょ キョ kyo
; ぎゃ ギャ gya
; ぎゅ ギュ gyu
; ぎょ ギョ gyo
; しゃ シャ sha
; しゅ シュ shu
; しょ ショ sho
; じゃ ジャ ja
; じゅ ジュ ju
; じょ ジョ jo
; ちゃ チャ cha
; ちゅ チュ chu
; ちょ チョ cho
; にゃ ニャ nya
; にゅ ニュ nyu
; にょ ニョ nyo
; ひゃ ヒャ hya
; ひゅ ヒュ hyu
; ひょ ヒョ hyo
; びゃ ビャ bya
; びゅ ビュ byu
; びょ ビョ byo
; ぴゃ ピャ pya
; ぴゅ ピュ pyu
; ぴょ ピョ pyo
; みゃ ミャ mya
; みゅ ミュ myu
; みょ ミョ myo
; りゃ リャ rya
; りゅ リュ ryu
; りょ リョ ryo

; Unofficial
; ゔ ヴ vu
; ゔぁ ヴァ va