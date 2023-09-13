; Type the endchar to activate any given Hotstring
#Hotstring EndChars \
endchar := "\"

; WIN+Z, suspend all hotstrings
#SuspendExempt
#z::Suspend -1
#SuspendExempt False

; Removes the endchar you typed to activate the Hotstring
#Hotstring o

; Hotstring works even if immediately preceded by an alphanumeric character
#Hotstring ?



; Makes Hotstrings case-sensitive
#Hotstring c

; Lowercase Greek
::alpha::α
::beta::β
::gamma::γ
::delta::δ
::epsilon::ε
::zeta::ζ
;::eta::η
::theta::θ
::iota::ι
::kappa::κ
::lambda::λ
::mu::μ
::nu::ν
::xi::ξ
::omicron::ο
::pi::π
::rho::ρ
::sigma::σ
::tau::τ
::upsilon::υ
::phi::φ
::chi::χ
::psi::ψ
::omega::ω



; Uppercase Greek
::Alpha::Α
::Beta::Β
::Gamma::Γ
::Delta::Δ
::Epsilon::Ε
::Zeta::Ζ
::Eta::Η
::Theta::Θ
::Iota::Ι
::Kappa::Κ
::Lambda::Λ
::Mu::Μ
::Nu::Ν
::Xi::Ξ
::Omicron::Ο
::Pi::Π
::Rho::Ρ
::Sigma::Σ
::Tau::Τ
::Upsilon::Υ
::Phi::Φ
::Chi::Χ
::Psi::Ψ
::Omega::Ω



; Superscripts
::^0::⁰
::^1::¹
::^2::²
::^3::³
::^4::⁴
::^5::⁵
::^6::⁶
::^7::⁷
::^8::⁸
::^9::⁹

::^+::⁺
::^-::⁻
::^=::⁼
::^(::⁽
::^)::⁾

::^a::ᵃ
::^b::ᵇ
::^c::ᶜ
::^d::ᵈ
::^e::ᵉ
::^f::ᶠ
::^g::ᵍ
::^h::ʰ
::^i::ⁱ
::^j::ʲ
::^k::ᵏ
::^l::ˡ
::^m::ᵐ
::^n::ⁿ
::^o::ᵒ
::^p::ᵖ
::^r::ʳ
::^s::ˢ
::^t::ᵗ
::^u::ᵘ
::^v::ᵛ
::^w::ʷ
::^x::ˣ
::^y::ʸ
::^z::ᶻ

::^A::ᴬ
::^B::ᴮ
::^D::ᴰ
::^E::ᴱ
::^G::ᴳ
::^H::ᴴ
::^I::ᴵ
::^J::ᴶ
::^K::ᴷ
::^L::ᴸ
::^M::ᴹ
::^N::ᴺ
::^O::ᴼ
::^P::ᴾ
::^R::ᴿ
::^T::ᵀ
::^U::ᵁ
::^V::ⱽ
::^W::ᵂ



; Subscripts
::_0::₀
::_1::₁
::_2::₂
::_3::₃
::_4::₄
::_5::₅
::_6::₆
::_7::₇
::_8::₈
::_9::₉
::_10::⏨

::_+::₊
::_-::₋
::_=::₌
::_(::₍
::_)::₎
::_"::„

::_a::ₐ
::_e::ₑ
::_h::ₕ
::_i::ᵢ
::_j::ⱼ
::_k::ₖ
::_l::ₗ
::_m::ₘ
::_n::ₙ
::_o::ₒ
::_p::ₚ
::_r::ᵣ
::_s::ₛ
::_t::ₜ
::_u::ᵤ
::_v::ᵥ
::_x::ₓ



; Accented characters
::A'::Á
::a'::á
::A``::À
::a``::à
::A^::Â
::a^::â
::Ao::Å
::ao::å
::A**::Ä
::a**::ä
::A~::Ã
::a~::ã
::A-acute::Á
::a-acute::á
::A-grave::À
::a-grave::à
::A-circumflex::Â
::a-circumflex::â
::A-ring::Å
::a-ring::å
::AA::Å
::aa::å
::A-umlaut::Ä
::a-umlaut::ä
::A-tilde::Ã
::a-tilde::ã

::E'::É
::e'::é
::E``::È
::e``::è
::E^::Ê
::e^::ê
::E**::Ë
::e**::ë
::E-acute::É
::e-acute::é
::E-grave::È
::e-grave::è
::E-circumflex::Ê
::e-circumflex::ê
::E-umlaut::Ë
::e-umlaut::ë

::I'::Í
::i'::í
::I``::Ì
::i``::ì
::I^::Î
::i^::î
::I**::Ï
::i**::ï
::I-acute::Í
::i-acute::í
::I-grave::Ì
::i-grave::ì
::I-circumflex::Î
::i-circumflex::î
::I-umlaut::Ï
::i-umlaut::ï

::O'::Ó
::o'::ó
::O``::Ò
::o``::ò
::O^::Ô
::o^::ô
::O**::Ö
::o**::ö
::O/::Ø
::o/::ø
::O-acute::Ó
::o-acute::ó
::O-grave::Ò
::o-grave::ò
::O-circumflex::Ô
::o-circumflex::ô
::O-umlaut::Ö
::o-umlaut::ö
::O-slash::Ø
::o-slash::ø

::U'::Ú
::u'::ú
::U``::Ù
::u``::ù
::U^::Û
::u^::û
::Uo::Ů
::uo::ů
::U**::Ü
::u**::ü
::U-acute::Ú
::u-acute::ú
::U-grave::Ù
::u-grave::ù
::U-circumflex::Û
::u-circumflex::û
::U-ring::Ů
::u-ring::ů
::U-umlaut::Ü
::u-umlaut::ü

::C,::Ç
::c,::ç
::C-cedilla::Ç
::c-cedilla::ç

::N~::Ñ
::n~::ñ
::N-tilde::Ñ
::n-tilde::ñ

::Y'::Ý
::y'::ý
::Y-acute::Ý
::y-acute::ý

::AE::Æ
::ae::æ

::slong::ſ
::Thorn::Þ
::thorn::þ



; Remove case sensitivity
#Hotstring c0



; Generic accent marks
::-'::́
::-``::̀
::-^::̂
::-o::̊
::-,::̧
::-**::̈
::-~::̃
::-acute::́
::-grave::̀
::-circumflex::̂
::-ring::̊
::-cedilla::̧
::-umlaut::̈
::-tilde::̃



; Comparators
::!<::≮
::!<=::≰
::<=::≤
::<<::≪
::!>::≯
::!>=::≱
::>=::≥
::>>::≫
::!=::≠
::!~=::≉
::~=::≈
::proportional::∝
::!congruent::≆
::congruent::≅
::=~::≅
::!===::≢
::===::≡



; Operators
::+-::±
::-+::∓
::composite::∘
::of::∘
::ring::∘
::cuberoot::∛
::fourthroot::∜
::root::√
::sqrt::√
::integral::∫
::del::∇
::nabla::∇
::o+::⊕
::o-::⊖
::ox::⊗
::o\::⊘
::o*::⊙
;::*::•
::partial::∂
::-dot::̇
::-dotdot::̈
::lceil::⌈
::lceiling::⌈
::leftceiling::⌈
::rceil::⌉
::rceiling::⌉
::rightceiling::⌉
::lfloor::⌊
::leftfloor::⌊
::rfloor::⌋
::rightfloor::⌋
::division::÷
::divide::÷
;::/::⁄
::!divides::∤
::divides::∣



; Sets
::!propersubset::⊄
::propersubset::⊂
::!subset::⊈
::subset::⊆
::!propersuperset::⊅
::propersuperset::⊃
::!superset::⊉
::superset::⊇
::!element::∉
::element::∈
;::in::∈
::!exists::∄
::exists::∃
::intersect::⋂
::union::⋃
::forall::∀
::nullset::∅
::null::∅
::emptyset::∅
::empty::∅
::reals::ℝ
::rationals::ℚ
::integers::ℤ
::complex::ℂ
::naturals::ℕ
::universal::𝕌
::universe::𝕌
::powerset::𝒫



; Logic
::therefore::∴
::because::∵
::not::¬
;::and::⋀
::xor::⊕
;::or::⋁
::implies::⇒
::then::⇒
::iff::⇔
::ifandonlyif::⇔



; Arrows
::upleft::↖
::leftup::↖
::upright::↗
::rightup::↗
::downright::↘
::rightdown::↘
::downleft::↙
::leftdown::↙
::<->::↔
::leftright::↔
::rightleft::↔
::horizontal::↔
::<-::←
;::left::←
::->::→
;::right::→
;::up::↑
;::down::↓
::updown::↕
::downup::↕
::vertical::↕
::<==::⇐
::==>::⇒
::<=>::⇔



; Units
::micro::μ
:: degrees::°
::degrees::°
:: degree::°
::degree::°
::deg::°
::degreesC::℃
::degreeC::℃
::degC::℃
::degreesF::℉
::degreeF::℉
::degF::℉
::ohm::Ω



; Astronomical
::sol::☉

::mercury::☿
::venus::♀
::earth::⨁
::earth2::♁
::luna::☾
::mars::♂
::jupiter::♃
::saturn::♄
::uranus::⛢
::uranus2::♅
::neptune::♆
::pluto::♇
::pluto2::⯓

::aries::♈
::taurus::♉
::gemini::♊
::cancer::♋
::leo::♌
::virgo::♍
::libra::♎
::scorpius::♏
::sagittarius::♐
::capricorn::♑
::aquarius::♒
::pisces::♓
::ophiuchus::⛎

::ceres::⚳



; Currency
::usd::$
::cent::¢
::cents::¢
::gbp::£
::currency::¤
::scarab::¤
::yen::¥
::euro::€
::btc::₿
::$p::₽



; Specific numbers
::1/::⅟
::1/2::½
::1/3::⅓
::2/3::⅔
::1/4::¼
::3/4::¾
::1/5::⅕
::2/5::⅖
::3/5::⅗
::4/5::⅘
::1/6::⅙
::5/6::⅚
::1/7::⅐
::1/8::⅛
::3/8::⅜
::5/8::⅝
::7/8::⅞
::1/9::⅑
::1/10::⅒
::infinity::∞



; Punctuation and symbols
::!!::‼
::inverted?!::⸘
::flipped?!::⸘
::flip?!::⸘
::?!::‽
::inverted!::¡
::flipped!::¡
::flip!::¡
::inverted?::¿
::flipped?::¿
::flip?::¿
::numero::№
::No.::№
::copyright::©
::trademark::™
::tm::™
::registered::®
::info::ⓘ
::information::ⓘ
::section::§
::dagger::†
::paragraph::¶
::pilcrow::¶
;::-::–
::--::—
::<"::“
::>"::”
::qed::∎
::_...::⋰
::^...::⋱
::....::⋮
::...::⋯


; Kaomoji
::_shrug::¯\_(ツ)_/¯
::_perv::( ͡° ͜ʖ ͡°)
::_unflip::┬─┬ノ( °◡° ノ)
::_flip::(╯°□°）╯︵ ┻━┻
::_disapprove::ಠ_ಠ
::_sunglasses1::( •_•)>⌐■-■
::_sunglasses2::(⌐■_■)
::_pointright::(☞ﾟヮﾟ)☞
::_pointleft::☜(ﾟヮﾟ☜)
::_disappointed::(¬_¬ )
::_hug::༼ つ ◕_◕ ༽つ



; Miscellaneous
::bom::{U+FEFF} ;﻿
::female::♀
::male::♂
::trans::⚧
::perpendicular::⟂
::rightangle::⦜
::triangle::△
::angle::∠
::-bar::̅
::-overscore::̅
::-overline::̅
::-hat::̂
::aleph::ℵ
::0 ::​
::. ::⠀
::nbsp::{U+00A0} ; 
::communism::☭
::hammerandsickle::☭
::censored::█
::redacted::█
::rtl::‏
::ankh::☥
::Rx::℞
::sine::∿
::bullet::•
::flat::♭
::sharp::♯
::#::♯
::natural::♮
::nat::♮


; Emoji
::emoji::️
::EJC::‍

; Heads
:::)::🙂
:::D::😃
::=D::😄
::;)::😉
::^_^::😁
::*_*::🤩
::XD::😆
::B)::😎
:::|::😐
:::/::🫤
::>_<::😖
:::*::😙
:::P::😛
::;P::😜
::>:(::😠
:::(::🙁
::>=(::😠
:::S::🥴
:::')::🥲
:::'(::😢
:::x::😬
::xp::😝
:::O::😮
::unsure::😕
::angel::😇
::devil::😈
::wink::😉
::blush::😊
::inlove::🥰
::love::😍
::love2::🥰
::smirk::😏
::stoic::😐
::kiss::😙
::kiss2::😘
::tongue::😛
::mad::😤
::angry::😠
::bull::😤
::exhale::😤
::nervous::😟
::anxious::😨
::scared::😨
::worried::😰
::relieved::😌
::sleepy::😪
::sob::😭
::shocked::😳
::flush::😳
::flushed::😳
::embarrassed::😳
::surprised::😲
::scream::😱
::astonished::😲
::monocle::🧐
::sleep::😴
::sleeping::😴
::dizzy::😵‍💫
::nomouth::😶
::mask::😷
::upsidedown::🙃
::rolleyes::🙄
::zipper::🤐
::greed::🤑
::greedy::🤑
::sick::🤒
::nerd::🤓
::thinking::🤔
::injured::🤕
::hug::🤗
::cold::🥶
::nauseous::🤢
::disgust::🤢
::laugh::🤣
::drool::🤤
::sneeze::🤧
::eyebrow::🤨
::crazy::🤪
::shh::🤫
::giggle::🤭
::puke::🤮
::vomit::🤮
::mindblown::🤯
::yawn::🥱
::party::🥳
::party2::🎈 🥳 🎂 ✨ 🎉 🎊 🎁
::brushingteeth::😁😆😩😲😬
::please::🥺
::beg::🥺
::plead::🥺
::cute::🥹
::happytears::🥹
::melting::🫠
::salute::🫡
::o7::🫡
::yum::🤤
::tasty::😋
::hot::🥵
::sweat::🥵
::spicy::🥵
::relief::😅
::phew::😅
::baby::👶
::liar::🤥
::lying::🤥
::santa::🎅
::santaclaus::🎅
::mrsclaus::🤶
::fuck::🤬
::weary::😩
::pensive::😔
::cowboy::🤠
::proud::️☺
::skull::💀
::dead::💀
::alien::👽
::robot::🤖

; Poses
::hugging::🫂
::facepalm::🤦
::shrug::🤷
::wave::🙋
::full::🫄
::hair::💁
::bike::🚴
::wizard::🧙
::vampire::🧛
::dracula::🧛
::ghost::👻
::snowman::⛄

; Body parts
::lips::💋
::bitelip::🫦
::mouth::👄
::eyes::👀
::brain::🧠
::dna::🧬
::pray::🙏
::eye::👁️
::ear::👂
::nose::👃
::blood::🩸
::luck::🤞
::pinch::🤏
::small::🤏
::horns::🤘
::callme::🤙
::handshake::🤝
::deal::🤝
::pointup::👆
::pointdown::👇
::pointleft::👈
::pointright::👉
::point::👉
::fist::👊
::ok::👌
::thumbsup::👍
::thumbsdown::👎
::rock::👊
::paper::✋
::scissors::✌️
::spock::🖖
::clap::👏
::fuckyou::🖕
::LLAP::🖖
::hand::✋
::v::✌️

; Hearts
::heartsuit::♥️
::<3::❤️
::</3::💔
::brokenheart::💔
::orangeheart::🧡
::whiteheart::🤍
::brownheart::🤎
::blackheart::🖤
::redheart::❤️
::blueheart::💙
::greenheart::💚
::yellowheart::💛
::goldheart::💛
::goldenheart::💛
::purpleheart::💜
::realheart::🫀
::anatomicalheart::🫀
::flamingheart::❤️‍🔥
::burningheart::❤️‍🔥
::bleedingheart::❣️
::<3!::❣️
::handheart::🫶
::handsheart::🫶
::plainheart::♡
::textheart::♡
::heart::❤️

; Animals and plants
::happycat::😺
::laughcat::😹
::lolcat::😹
::smilecat::😸
::lovecat::😻
::smirkcat::😼
::kisscat::😽
::madcat::😾
::angrycat::😾
::sobcat::😿
::crycat::😿
::sadcat::😿
::screamcat::🙀
::cat::🐈
::seenoevil::🙈
::hearnoevil::🙉
::speaknoevil::🙊
::alligator::🐊
::crocodile::🐊
::croc::🐊
::snake::🐍
::tss::🐍
::bee::🐝
::bat::🦇
::lizard::🦎
::spider::🕷️
::palmtree::🌴
::christmastree::🎄
::tree::🌳
::cactus::🌵
::clover::🍀
::mushroom::🍄
::pumpkin::🎃
::jack-o-lantern::🎃
::jackolantern::🎃

; Food
::taco::🌮
::eggplant::🍆
::peach::🍑
::watermelon::🍉
::banana::🍌
::pineapple::🍍
::apple::🍎
::pizza::🍕
::donut::🍩
::cookie::🍪
::pickle::🥒
::egg::🥚
::broccoli::🥦
::sandwich::🥪
::cheese::🧀
::chocolate::🍫
::candy::🍬
::lollipop::🍭
::bottle::🍼
::milk::🍼
::popcorn::🍿
::cake::🎂

; Nature
::storm::⛈️
::snow::❄️
::snowflake::❄️
;::star::⭐
::rainbow::🌈
::globe1::🌍
::globe::🌎
::globe2::🌎
::globe3::🌏
::moon1::🌑
::moon2::🌒
::moon3::🌓
::moon4::🌔
::moon5::🌕
::moon6::🌖
::moon7::🌗
::moon8::🌘
::moon::🌙
::sun::🌞
::raincloud::🌧️
::fire::🔥
::water::💦
::wet::💦

; Objects
::piano::🎹
::key::🔑
::lock::🔒
::bell::🔔
::knife::🔪
::gun::🔫
::web::🕸️
::sword::🗡️
::rocket::🚀
::bed::🛌
::drum::🥁
::badum::🥁
::sunglasses::🕶
::glasses::👓
::safetypin::🧷
::jab::💉
::hourglass::⏳
::hourglass2::⌛
::umbrella::☂️
::pickaxe::⛏️
::airplane::✈️
::plane::✈️
::gift::🎁
::present::🎁
::balloon::🎈
::diamond::💎
::bomb::💣
::poop::💩
::watch::⌚
::swords::⚔️
::fireworks::🎆
::sparkler::🎇
::popper::🎉
::confetti::🎊
::target::🎯
::pirateflag::🏴‍☠️
::flag::🚩
::jollyroger::🏴‍☠️
::money::💰

; Symbols
::caution::⚠️
::warning::⚠️
::underage::🔞
::18+::🔞
::anger::💢
::100::💯
::radioactive::☢️
::biohazard::☣️
::islam::☪️
::muslim::☪️
::spade::♠️
::club::♣️
::diamondsuit::♦️
::recycle::♻️
::check::✅
::check2::✔️
::checkmark::✔️
::cross::✝️
::christian::✝️
::jewish::✡️
::starofdavid::✡️
::menorah::🕎
;::x::❌
::zzz::💤
::shootingstar::💫
::dizzy2::💫
::no::🚫
::cancel::🚫
::prohibited::🚫
::graphup::📈
::graphdown::📉
::fart::💨
::red::🟥
::orange::🟧
::yellow::🟨
::green::🟩
::blue::🟦
::purple::🟪
::brown::🟫
::black::⬛
::white::⬜
::red2::🔴
::orange2::🟠
::yellow2::🟡
::green2::🟢
::blue2::🔵
::purple2::🟣
::brown2::🟤
::black2::⚫
::white2::⚪
::sound::🔊
::audio::🔊
::mute::🔈
::muted::🔈
::sparkles::✨
::shiny::✨
::music::🎵
::plainnote::♪
::textnote::♪
::note::🎵
::plainstar::★
::textstar::★
::hollowstar::☆
::crossbones::☠️


; Problematic Hotstrings that interrupt other Hotstrings if placed before them in this file.  These appear above but are commented out
::star::⭐
::eta::η
::*::•
::/::⁄
::left::←
::up::↑
::right::→
::down::↓
::in::∈
::and::⋀
::or::⋁
::x::❌
::-::–


; Randomizes the solid colored hearts
::hearts::{
	hearts := ["💚", "🤎", "💙", "🧡", "🤍", "🖤", "❤️", "💛", "💜"]
	newHearts := ""
	while hearts.Length > 0 {
		N := Random(1, hearts.Length)
		newHearts .= hearts[N]
		hearts.RemoveAt(N)
	}
	Send newHearts
}

; Randomizes even more hearts
::hearts2::{
	hearts := ["💚", "🤎", "💙", "🧡", "🤍", "🖤", "❤️", "💛", "💜", "💝", "💘", "💖", "💗", "💓", "💞", "💟", "❣", "💕", "🫀"]
	newHearts := ""
	while hearts.Length > 0 {
		N := Random(1, hearts.Length)
		newHearts .= hearts[N]
		hearts.RemoveAt(N)
	}
	Send newHearts
}


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
	text := StrReplace(text, "`r", "  ")
	text := StrReplace(text, "`n", "  ")
	backspaceCount := StrLen(text) + 1
	If StrLen(text) == 0 { ; If they didn't type anything, take the text from the clipboard
		text := A_Clipboard
	}
}

; Bulk superscripting
::`^^:: {
	GatherInput(&text, &backspaceCount)
	
	charMap := Map()
	charMap.Set( "+","⁺", "-","⁻", "=","⁼", "(","⁽", ")","⁾"
			, "0","⁰", "1","¹", "2","²", "3","³", "4","⁴", "5","⁵", "6","⁶", "7","⁷", "8","⁸", "9","⁹"
			, "a","ᵃ", "b","ᵇ", "c","ᶜ", "d","ᵈ", "e","ᵉ", "f","ᶠ", "g","ᵍ", "h","ʰ", "i","ⁱ", "j","ʲ", "k","ᵏ", "l","ˡ", "m","ᵐ"
			, "n","ⁿ", "o","ᵒ", "p","ᵖ", "r","ʳ", "s","ˢ", "t","ᵗ", "u","ᵘ", "v","ᵛ", "w","ʷ", "x","ˣ", "y","ʸ", "z","ᶻ"
			, "A","ᴬ", "B","ᴮ", "D","ᴰ", "E","ᴱ", "G","ᴳ", "H","ᴴ", "I","ᴵ", "J","ᴶ", "K","ᴷ", "L","ᴸ", "M","ᴹ"
			, "N","ᴺ", "O","ᴼ", "P","ᴾ", "R","ᴿ", "T","ᵀ", "U","ᵁ", "V","ⱽ", "W","ᵂ" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk subscripting
::__:: {
	GatherInput(&text, &backspaceCount)
	
	charMap := Map()
	charMap.Set( "+","₊", "-","₋", "=","₌", "(","₍", ")","₍"
			, "0","₀", "1","₁", "2","₂", "3","₃", "4","₄", "5","₅", "6","₆", "7","₇", "8","₈", "9","₉"
			, "a","ₐ", "e","ₑ", "h","ₕ", "i","ᵢ", "j","ⱼ", "k","ₖ", "l","ₗ", "m","ₘ"
			, "n","ₙ", "o","ₒ", "p","ₚ", "r","ᵣ", "s","ₛ", "t","ₜ", "u","ᵤ", "v","ᵥ", "x","ₓ" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk upside-down
::flip:: {
	GatherInput(&text, &backspaceCount)
	
	; Reverse order of input
	tempText := ""
	Loop Parse text {
		tempText := A_LoopField . tempText
	}
	text := tempText
	
	charMap := Map()
	charMap.Set( "&","⅋", ">","<", "<",">", "}","{", "{","}", "]","[", "[","]", ")","(", "(",")", "_","‾", "!","¡", "?","¿", ".","˙", "`"",",,", "'",",", ",","'", "^","v"
			, "0","0", "1","Ɩ", "2","ᄅ", "3","Ɛ", "4","ㄣ", "5","ϛ", "6","9", "7","ㄥ", "8","8", "9","6"
			, "a","ɐ", "b","q", "c","ɔ", "d","p", "e","ǝ", "f","ɟ", "g","ƃ", "h","ɥ", "i","ᴉ", "j","ɾ", "k","ʞ", "l","l", "m","ɯ"
			, "n","u", "o","o", "p","d", "q","b", "r","ɹ", "s","s", "t","ʇ", "u","n", "v","ʌ", "w","ʍ", "x","x", "y","ʎ", "z","z"
			, "A","∀", "B","q", "C","Ɔ", "D","p", "E","Ǝ", "F","Ⅎ", "G","פ", "H","H", "I","I", "J","ſ", "K","ʞ", "L","˥", "M","W"
			, "N","N", "O","O", "P","Ԁ", "Q","Q", "R","ɹ", "S","S", "T","┴", "U","∩", "V","Λ", "W","M", "X","X", "Y","⅄", "Z","Z" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk unbraille code
::unbraille:: {
	GatherInput(&text, &backspaceCount)
	
	charMap := Map()
	charMap.Set( "⠂",",", "⠆",";", "⠒",":", "⠲",".", "⠖","!", "⠶","(", "⠶",")", "⠦","?", "⠦","`"", "⠦","<", "⠴",">", "⠌","/", "⠄","'", "⠤","-", "⠀"," "
			, "⠁","a", "⠃","b", "⠉","c", "⠙","d", "⠑","e", "⠋","f", "⠛","g", "⠓","h", "⠊","i", "⠚","j", "⠅","k", "⠇","l", "⠍","m"
			, "⠝","n", "⠕","o", "⠏","p", "⠟","q", "⠗","r", "⠎","s", "⠞","t", "⠥","u", "⠧","v", "⠺","w", "⠭","x", "⠽","y", "⠵","z" )
	numMap := Map()
	numMap.Set( "a","1", "b","2", "c","3", "d","4", "e","5", "f","6", "g","7", "h","8", "i","9", "j","0" )
	
	; nextNumber and nextUpper track if the next character is a number or uppercase letter, each of which are expressed with a special prefix character
	nextNumber := False
	nextUpper := False
	out := ""
	Loop Parse text {
		If A_LoopField == "⠠" {
			nextUpper := True
			Continue
		}
		If A_LoopField == "⠼" {
			nextNumber := True
			Continue
		}
		nextChar := charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
		If nextUpper {
			nextChar := StrUpper(nextChar)
			nextUpper := False
		}
		If nextNumber {
			nextChar := numMap.Has(nextChar) ? numMap[nextChar] : nextChar
			nextNumber := False
		}
		out .= nextChar
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk braille
::braille:: {
	GatherInput(&text, &backspaceCount)
	
	charMap := Map()
	charMap.CaseSense := "Off"
	charMap.Set( ",","⠂", ";","⠆", ":","⠒", ".","⠲", "!","⠖", "(","⠶", ")","⠶", "?","⠦", "`"","⠦", "<","⠦", ">","⠴", "/","⠌", "'","⠄", "-","⠤", " ","⠀"
			, "1","⠼⠁", "2","⠼⠃", "3","⠼⠉", "4","⠼⠙", "5","⠼⠑", "6","⠼⠋", "7","⠼⠛", "8","⠼⠓", "9","⠼⠊", "0","⠼⠚"
			, "a","⠁", "b","⠃", "c","⠉", "d","⠙", "e","⠑", "f","⠋", "g","⠛", "h","⠓", "i","⠊", "j","⠚", "k","⠅", "l","⠇", "m","⠍"
			, "n","⠝", "o","⠕", "p","⠏", "q","⠟", "r","⠗", "s","⠎", "t","⠞", "u","⠥", "v","⠧", "w","⠺", "x","⠭", "y","⠽", "z","⠵" )
	
	out := ""
	Loop Parse text {
		If IsUpper(A_LoopField) {
			out .= "⠠"
		}
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk unmorse code
::unmorse:: {
	GatherInput(&text, &backspaceCount)
	
	text := StrReplace(text, " ", " ")
	Loop {
		text := StrReplace(text, "   ", "  ",, &count)
		If count == 0 {
			Break
		}
	}
	
	charMap := Map()
	charMap.Set( ""," "
			, "•−•−•−",".", "−−••−−",",", "••−−••","?", "•−−−−•","'", "−••−•","/", "−•−−•","(", "−•−−•−",")", "•−•••","&", "−−−•••",":", "−•••−","=", "•−•−•","+", "−••••−","-", "•−••−•","`"", "•−−•−•","@", "•••−••−","$", "••−−•−","_", "−•−•−•",";", "−•−•−−","!"
			, "•−","A", "−•••","B", "−•−•","C", "−••","D", "•","E", "••−•","F", "−−•","G", "••••","H", "••","I", "•−−−","J", "−•−","K", "•−••","L", "−−","M"
			, "−•","N", "−−−","O", "•−−•","P", "−−•−","Q", "•−•","R", "•••","S", "−","T", "••−","U", "•••−","V", "•−−","W", "−••−","X", "−•−−","Y", "−−••","Z"
			, "•−−−−","1", "••−−−","2", "•••−−","3", "••••−","4", "•••••","5", "−••••","6", "−−•••","7", "−−−••","8", "−−−−•","9", "−−−−−","0"
			, ".-.-.-",".", "--..--",",", "..--..","?", ".----.","'", "-..-.","/", "-.--.","(", "-.--.-",")", ".-...","&", "---...",":", "-...-","=", ".-.-.","+", "-....-","-", ".-..-.","`"", ".--.-.","@", "...-..-","$", "..--.-","_", "-.-.-.",";", "-.-.--","!"
			, ".-","A", "-...","B", "-.-.","C", "-..","D", ".","E", "..-.","F", "--.","G", "....","H", "..","I", ".---","J", "-.-","K", ".-..","L", "--","M"
			, "-.","N", "---","O", ".--.","P", "--.-","Q", ".-.","R", "...","S", "-","T", "..-","U", "...-","V", ".--","W", "-..-","X", "-.--","Y", "--..","Z"
			, ".----","1", "..---","2", "...--","3", "....-","4", ".....","5", "-....","6", "--...","7", "---..","8", "----.","9", "-----","0" )
	
	out := ""
	Loop Parse text, A_Space {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk morse code
::morse:: {
	GatherInput(&text, &backspaceCount)
	
	charMap := Map()
	charMap.CaseSense := "Off"
	charMap.Set( ".","•−•−•− ", ",","−−••−− ", "?","••−−•• ", "'","•−−−−• ", "/","−••−• ", "(","−•−−• ", ")","−•−−•− ", "&","•−••• ", ":","−−−••• ", "=","−•••− ", "+","•−•−• ", "-","−••••− ", "`"","•−••−• ", "@","•−−•−• ", "$","•••−••− ", "_","••−−•− ", ";","−•−•−• ", "!","−•−•−− ", " ","  "
			, "a","•− ", "b","−••• ", "c","−•−• ", "d","−•• ", "e","• ", "f","••−• ", "g","−−• ", "h","•••• ", "i","•• ", "j","•−−− ", "k","−•− ", "l","•−•• ", "m","−− "
			, "n","−• ", "o","−−− ", "p","•−−• ", "q","−−•− ", "r","•−• ", "s","••• ", "t","− ", "u","••− ", "v","•••− ", "w","•−− ", "x","−••− ", "y","−•−− ", "z","−−•• "
			, "1","•−−−− ", "2","••−−− ", "3","•••−− ", "4","••••− ", "5","••••• ", "6","−•••• ", "7","−−••• ", "8","−−−•• ", "9","−−−−• ", "0","−−−−− " )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk morse code, periods and hyphens
::morse2:: {
	GatherInput(&text, &backspaceCount)
	
	charMap := Map()
	charMap.CaseSense := "Off"
	charMap.Set( ".",".-.-.- ", ",","--..-- ", "?","..--.. ", "'",".----. ", "/","-..-. ", "(","-.--. ", ")","-.--.- ", "&",".-... ", ":","---... ", "=","-...- ", "+",".-.-. ", "-","-....- ", "`"",".-..-. ", "@",".--.-. ", "$","...-..- ", "_","..--.- ", ";","-.-.-. ", "!","-.-.-- ", " ","  "
		, "a",".- ", "b","-... ", "c","-.-. ", "d","-.. ", "e",". ", "f","..-. ", "g","--. ", "h",".... ", "i",".. ", "j",".--- ", "k","-.- ", "l",".-.. ", "m","-- "
		, "n","-. ", "o","--- ", "p",".--. ", "q","--.- ", "r",".-. ", "s","... ", "t","- ", "u","..- ", "v","...- ", "w",".-- ", "x","-..- ", "y","-.-- ", "z","--.. "
		, "1",".---- ", "2","..--- ", "3","...-- ", "4","....- ", "5","..... ", "6","-.... ", "7","--... ", "8","---.. ", "9","----. ", "0","----- " )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk unrune code (Elder Futhark)
::unrune:: {
	GatherInput(&text, &backspaceCount)
	
	text := StrReplace(text, "ᚦ", "th")
	text := StrReplace(text, "ᛜ", "ng")
	
	charMap := Map()
	charMap.Set( "ᚠ","f", "ᚢ","u", "ᛞ","d", "ᛉ","z", "ᛒ","b", "ᛃ","j", "ᚨ","a", "ᚹ","w", "ᚷ","g", "æ","ᛇ", "ᚱ","r", "ᚲ","k", "ᚺ","h", "ᚾ","n", "ᛁ","i", "ᛖ","e", "ᛊ","s", "ᛏ","t", "ᛈ","p", "ᛗ","m", "ᛚ","l", "ᛟ","o" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk Elder Futhark
::rune:: {
	GatherInput(&text, &backspaceCount)
	
	text := StrReplace(text, "th", "ᚦ", 0)
	text := StrReplace(text, "ng", "ᛜ", 0)
	text := StrReplace(text, "ae", "ᛇ", 0)
	
	charMap := Map()
	charMap.CaseSense := "Off"
	charMap.Set( "f","ᚠ", "u","ᚢ", "a","ᚨ", "r","ᚱ", "k","ᚲ", "g","ᚷ", "w","ᚹ", "h","ᚺ", "n","ᚾ", "i","ᛁ", "j","ᛃ", "æ","ᛇ", "p","ᛈ", "z","ᛉ", "s","ᛊ", "t","ᛏ", "b","ᛒ", "e","ᛖ", "m","ᛗ", "l","ᛚ", "o","ᛟ", "d","ᛞ", "v","ᚠ" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk unrune code (Younger Futhark)
::unrune2:: {
	GatherInput(&text, &backspaceCount)
	
	text := StrReplace(text, "ᚦ", "th")
	text := StrReplace(text, "ᛦ", "r")
	
	charMap := Map()
	charMap.Set( "ᚠ","f", "ᚢ","o", "ᚬ","æ", "ᚱ","r", "ᚴ","k", "ᚼ","h", "ᚾ","n", "ᛁ","i", "ᛅ","e", "ᛋ","s", "ᛏ","t", "ᛒ","p", "ᛘ","m", "ᛚ","l" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk Younger Futhark
::rune2:: {
	GatherInput(&text, &backspaceCount)
	
	text := StrReplace(text, "th", "ᚦ", 0)
	text := StrReplace(text, "rrr", "ᛦ", 0)
	
	charMap := Map()
	charMap.CaseSense := "Off"
	charMap.Set( "f","ᚠ", "u","ᚢ", "v","ᚢ", "w","ᚢ", "y","ᚢ", "o","ᚢ", "ø","ᚢ", "æ","ᚬ", "r","ᚱ", "k","ᚴ", "g","ᚴ", "h","ᚼ", "n","ᚾ", "i","ᛁ", "e","ᛅ", "a","ᛅ", "s","ᛋ", "t","ᛏ", "d","ᛏ", "b","ᛒ", "p","ᛒ", "m","ᛘ", "l","ᛚ" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk blackboard bold
::bb:: {
	GatherInput(&text, &backspaceCount)
	
	text := StrReplace(text, "Sigma", "⅀")
	text := StrReplace(text, "Gamma", "ℾ")
	text := StrReplace(text, "gamma", "ℽ")
	text := StrReplace(text, "Pi", "ℿ")
	text := StrReplace(text, "pi", "ℼ")
	
	charMap := Map()
	charMap.Set( "0","𝟘", "1","𝟙", "2","𝟚", "3","𝟛", "4","𝟜", "5","𝟝", "6","𝟞", "7","𝟟", "8","𝟠", "9","𝟡"
			, "a","𝕒", "b","𝕓", "c","𝕔", "d","𝕕", "e","𝕖", "f","𝕗", "g","𝕘", "h","𝕙", "i","𝕚", "j","𝕛", "k","𝕜", "l","𝕝", "m","𝕞"
			, "n","𝕟", "o","𝕠", "p","𝕡", "q","𝕢", "r","𝕣", "s","𝕤", "t","𝕥", "u","𝕦", "v","𝕧", "w","𝕨", "x","𝕩", "y","𝕪", "z","𝕫"
			, "A","𝔸", "B","𝔹", "C","ℂ", "D","𝔻", "E","𝔼", "F","𝔽", "G","𝔾", "H","ℍ", "I","𝕀", "J","𝕁", "K","𝕂", "L","𝕃", "M","𝕄"
			, "N","ℕ", "O","𝕆", "P","ℙ", "Q","ℚ", "R","ℝ", "S","𝕊", "T","𝕋", "U","𝕌", "V","𝕍", "W","𝕎", "X","𝕏", "Y","𝕐", "Z","ℤ" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk small caps
::smallcaps:: {
	GatherInput(&text, &backspaceCount)
	
	charMap := Map()
	charMap.CaseSense := "Off"
	charMap.Set( "A","ᴀ", "B","ʙ", "C","ᴄ", "D","ᴅ", "E","ᴇ", "F","ғ", "G","ɢ", "H","ʜ", "I","ɪ", "J","ᴊ", "K","ᴋ", "L","ʟ", "M","ᴍ"
			, "N","ɴ", "O","ᴏ", "P","ᴘ", "Q","ǫ", "R","ʀ", "S","s", "T","ᴛ", "U","ᴜ", "V","ᴠ", "W","ᴡ", "X","x", "Y","ʏ", "Z","ᴢ" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk bold cursive
::boldcursive:: {
	GatherInput(&text, &backspaceCount)
	
	charMap := Map()
	charMap.Set( "a","𝓪", "b","𝓫", "c","𝓬", "d","𝓭", "e","𝓮", "f","𝓯", "g","𝓰", "h","𝓱", "i","𝓲", "j","𝓳", "k","𝓴", "l","𝓵", "m","𝓶"
			, "n","𝓷", "o","𝓸", "p","𝓹", "q","𝓺", "r","𝓻", "s","𝓼", "t","𝓽", "u","𝓾", "v","𝓿", "w","𝔀", "x","𝔁", "y","𝔂", "z","𝔃"
			, "A","𝓐", "B","𝓑", "C","𝓒", "D","𝓓", "E","𝓔", "F","𝓕", "G","𝓖", "H","𝓗", "I","𝓘", "J","𝓙", "K","𝓚", "L","𝓛", "M","𝓜"
			, "N","𝓝", "O","𝓞", "P","𝓟", "Q","𝓠", "R","𝓡", "S","𝓢", "T","𝓣", "U","𝓤", "V","𝓥", "W","𝓦", "X","𝓧", "Y","𝓨", "Z","𝓩" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk cursive
::cursive:: {
	GatherInput(&text, &backspaceCount)
	
	charMap := Map()
	charMap.Set( "a","𝒶", "b","𝒷", "c","𝒸", "d","𝒹", "e","𝔢", "f","𝒻", "g","ℊ", "h","𝒽", "i","𝒾", "j","𝒿", "k","𝓀", "l","𝓁", "m","𝓂"
			, "n","𝓃", "o","ℴ", "p","𝓅", "q","𝓆", "r","𝓇", "s","𝓈", "t","𝓉", "u","𝓊", "v","𝓋", "w","𝓌", "x","𝓍", "y","𝓎", "z","𝓏"
			, "A","𝒜", "B","ℬ", "C","𝒞", "D","𝒟", "E","ℰ", "F","ℱ", "G","𝒢", "H","ℋ", "I","ℐ", "J","𝒥", "K","𝒦", "L","ℒ", "M","ℳ"
			, "N","𝒩", "O","𝒪", "P","𝒫", "Q","𝒬", "R","ℛ", "S","𝒮", "T","𝒯", "U","𝒰", "V","𝒱", "W","𝒲", "X","𝒳", "Y","𝒴", "Z","𝒵" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk bolditalic
::bolditalic:: {
	GatherInput(&text, &backspaceCount)
	
	charMap := Map()
	charMap.Set( "a","𝙖", "b","𝙗", "c","𝙘", "d","𝙙", "e","𝙚", "f","𝙛", "g","𝙜", "h","𝙝", "i","𝙞", "j","𝙟", "k","𝙠", "l","𝙡", "m","𝙢"
			, "n","𝙣", "o","𝙤", "p","𝙥", "q","𝙦", "r","𝙧", "s","𝙨", "t","𝙩", "u","𝙪", "v","𝙫", "w","𝙬", "x","𝙭", "y","𝙮", "z","𝙯"
			, "A","𝑨", "B","𝑩", "C","𝑪", "D","𝑫", "E","𝑬", "F","𝑭", "G","𝑮", "H","𝑯", "I","𝑰", "J","𝑱", "K","𝑲", "L","𝑳", "M","𝑴"
			, "N","𝑵", "O","𝑶", "P","𝑷", "Q","𝑸", "R","𝑹", "S","𝑺", "T","𝑻", "U","𝑼", "V","𝑽", "W","𝑾", "X","𝑿", "Y","𝒀", "Z","𝒁" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk bold
::bold:: {
	GatherInput(&text, &backspaceCount)
	
	charMap := Map()
	charMap.Set( "a","𝐚", "b","𝐛", "c","𝐜", "d","𝐝", "e","𝐞", "f","𝐟", "g","𝐠", "h","𝐡", "i","𝐢", "j","𝐣", "k","𝐤", "l","𝐥", "m","𝐦"
			, "n","𝐧", "o","𝐨", "p","𝐩", "q","𝐪", "r","𝐫", "s","𝐬", "t","𝐭", "u","𝐮", "v","𝐯", "w","𝐰", "x","𝐱", "y","𝐲", "z","𝐳"
			, "A","𝐀", "B","𝐁", "C","𝐂", "D","𝐃", "E","𝐄", "F","𝐅", "G","𝐆", "H","𝐇", "I","𝐈", "J","𝐉", "K","𝐊", "L","𝐋", "M","𝐌"
			, "N","𝐍", "O","𝐎", "P","𝐏", "Q","𝐐", "R","𝐑", "S","𝐒", "T","𝐓", "U","𝐔", "V","𝐕", "W","𝐖", "X","𝐗", "Y","𝐘", "Z","𝐙" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk italic
::italic:: {
	GatherInput(&text, &backspaceCount)
	
	charMap := Map()
	charMap.Set( "a","𝘢", "b","𝘣", "c","𝘤", "d","𝘥", "e","𝘦", "f","𝘧", "g","𝘨", "h","𝘩", "i","𝘪", "j","𝘫", "k","𝘬", "l","𝘭", "m","𝘮"
			, "n","𝘯", "o","𝘰", "p","𝘱", "q","𝘲", "r","𝘳", "s","𝘴", "t","𝘵", "u","𝘶", "v","𝘷", "w","𝘸", "x","𝘹", "y","𝘺", "z","𝘻"
			, "A","𝐴", "B","𝐵", "C","𝐶", "D","𝐷", "E","𝐸", "F","𝐹", "G","𝐺", "H","𝐻", "I","𝐼", "J","𝐽", "K","𝐾", "L","𝐿", "M","𝑀"
			, "N","𝑁", "O","𝑂", "P","𝑃", "Q","𝑄", "R","𝑅", "S","𝑆", "T","𝑇", "U","𝑈", "V","𝑉", "W","𝑊", "X","𝑋", "Y","𝑌", "Z","𝑍" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk underline
::underline:: {
	GatherInput(&text, &backspaceCount)
	
	out := "͟"
	Loop Parse text {
		out .= A_LoopField . "͟"
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk lookalike letters
::lookalike:: {
	GatherInput(&text, &backspaceCount)
	
	charMap := Map()
	charMap.Set( "a","а", "b","ᖯ", "c","с", "d","𝖽", "e","е", "f","𝖿", "g","𝗀", "h","һ", "i","і", "j","ј", "k","𝗄", "l","ӏ", "m","ｍ"
			, "n","𝗇", "o","о", "p","р", "q","𝗊", "r","𝗋", "s","ѕ", "t","𝗍", "u","𝗎", "v","ν", "w","𝗐", "x","х", "y","у", "z","ꮓ"
			, ":","։", ";",";", "<","˂", ">","˃", "=","᐀", "@","＠", "!","ǃ", "$","＄", "%","％", "&","＆", "(","❨", ")","❩", "*","*", "+","᛭", "-","˗"
			, "A","Α", "B","Β", "C","С", "D","Ꭰ", "E","Ε", "F","ꓝ", "G","Ꮐ", "H","Η", "I","l", "J","Ј", "K","Κ", "L","ᒪ", "M","Μ"
			, "N","Ν", "O","Ο", "P","Ρ", "Q","ⵕ", "R","ꓣ", "S","Ѕ", "T","Τ", "U","ꓴ", "V","Ꮩ", "W","Ꮃ", "X","Χ", "Y","Υ", "Z","Ζ" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk rot13 code
::rot13:: {
	GatherInput(&text, &backspaceCount)
	
	charMap := Map()
	charMap.Set( "a","n", "b","o", "c","p", "d","q", "e","r", "f","s", "g","t", "h","u", "i","v", "j","w", "k","x", "l","y", "m","z"
			, "n","a", "o","b", "p","c", "q","d", "r","e", "s","f", "t","g", "u","h", "v","i", "w","j", "x","k", "y","l", "z","m"
			, "A","N", "B","O", "C","P", "D","Q", "E","R", "F","S", "G","T", "H","U", "I","V", "J","W", "K","X", "L","Y", "M","Z"
			, "N","A", "O","B", "P","C", "Q","D", "R","E", "S","F", "T","G", "U","H", "V","I", "W","J", "X","K", "Y","L", "Z","M" )
	
	out := ""
	Loop Parse text {
		out .= charMap.Has(A_LoopField) ? charMap[A_LoopField] : A_LoopField
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk alternating caps with randomness
::mock:: {
	GatherInput(&text, &backspaceCount)
	
	; bias biases it against long strings in a row where the case doesn't change at all
	bias := 0.0
	out := ""
	Loop Parse text {
		lowercase := Random(0, 1)
		If lowercase < 0.5 + bias {
			If bias > 0 {
				bias := -0.1
			} Else {
				bias -= 0.25
			}
			out .= StrLower(A_LoopField)
		} Else {
			If bias < 0 {
				bias := 0.1
			} Else {
				bias += 0.25
			}
			out .= StrUpper(A_LoopField)
		}
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}

; Bulk alternating caps without randomness
::mock2:: {
	GatherInput(&text, &backspaceCount)
	
	lower := True
	out := ""
	Loop Parse text {
		out .= lower ? StrLower(A_LoopField) : StrUpper(A_LoopField)
		lower := !lower
	}
	
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}



; Mathy features

; Formats user input to make sure it's a
; number, remove leading and trailing
; whitespace, and remove leading 0s.  
; Purposely avoids doing math operations to avoid
; floating point precision errors messing up 
; significant figure calculations
FormatVal(&val) {
	If !IsNumber(val) {
		val := calc(val)
		If !IsNumber(val) {
			val := "NaN"
			Return
		}
	}
	; Trim leading and trailing whitespace
	val := Trim(val)
	; Trim leading 0s
	; Account for leading - in negatives
	val := val < 0 ? "-" . LTrim(SubStr(val, 2), "0") : LTrim(val, "0")
	If val == "" Or val == "-" Or val == "." {
		val := "0"
	}
	; Intentionally allows a trailing decimal to indicate
	; significance of trailing 0s in an integer value
	Return
}

; Determines the number of significant figures in val
DetermineSigFigs(val, &SigFigs) {
	; Ensures val is a well formatted number with nothing extra
	FormatVal(&val)
	; Remove any scientific notation, not relevant here
	If i := InStr(val, "e") {
		val := SubStr(val, 1, i-1)
	}
	; Remove any negatives, not relevant here
	If InStr(val, "-") {
		val := SubStr(val, 2)
	}
	; Number is only an integer
	If !InStr(val, ".") {
		If val == 0 { ; Entire number is 0
			SigFigs := 1
			Return
		}
		; Remove insignificant trailing 0s
		val := RTrim(val, "0")
		SigFigs := StrLen(val)
		Return
	}
	; Number has a decimal point
	SigFigs := 0
	; Split into integer and decimal parts
	splitVal := StrSplit(val, ".")
	If StrLen(splitVal[1]) > 0 And splitVal[1] > 0 {
		; If integer part isn't 0, it's all significant
		SigFigs += StrLen(splitVal[1])
	}
	If SigFigs > 0 {
		; If integer part isn't 0, all of the decimal part is significant
		SigFigs += StrLen(splitVal[2])
	} Else {
		; If integer part is 0, only parts of decimal part from first nonzero entry is significant, unless it's all 0s
		trimmedVal2 := LTrim(splitVal[2], "0")
		If trimmedVal2 == "" {
			SigFigs += StrLen(splitVal[2])
		} Else {
			SigFigs += StrLen(trimmedVal2)
		}
	}
}

; Formats val to have SigFig significant figures
FormatSigFigs(&val, SigFigs) {
	DetermineSigFigs(val, &valSigFigs)
	; Handle scientific notation
	suffix := ""
	If i := InStr(val, "e") {
		suffix := SubStr(val, i)
		val := SubStr(val, 1, i-1)
	}
	If valSigFigs == SigFigs { ; Done!
		val .= suffix
		Return
	} Else If valSigFigs <= SigFigs { ; Just add on 0s until it's good
		If !InStr(val, ".") { ; Add a decimal if it's not already there
			val .= "."
		}
		While valSigFigs <= SigFigs {
			val .= "0"
			valSigFigs += 1
		}
		val .= suffix
		Return
	} Else { ; Too many sig figs - gotta cut back
		; Find index of first sig fig
		firstSigIndex := 1
		Loop Parse val {
			If (IsNumber(A_LoopField) And A_LoopField != "0") {
				Break
			}
			firstSigIndex += 1
		}
		; Find index of first digit after last sig fig
		rightIndex := 1
		sigFigsSeen := 1
		Loop Parse val {
			If rightIndex <= firstSigIndex {
				rightIndex += 1
				Continue
			}
			If sigFigsSeen == SigFigs {
				If IsNumber(A_LoopField) {
					Break
				}
				rightIndex += 1
				Continue
			}
			If IsNumber(A_LoopField) {
				sigFigsSeen += 1
			}
			rightIndex += 1
		}
		; Index of decimal point
		decimalIndex := InStr(val, ".")
		If decimalIndex == 0 { ; Ensure all numbers have a decimal to make logic simpler
			val .= "."
			decimalIndex := StrLen(val)
		}
		; roundPos picks which digit to round on
		; endPos is to chop off floating point precision errors in the end
		If rightIndex > decimalIndex { ; Rounding right of the decimal
			roundPos := rightIndex - decimalIndex - 1
			endPos := rightIndex - 1
		} Else { ; Rounding left of the decimal
			roundPos := rightIndex - decimalIndex
			endPos := decimalIndex - 1
		}
		val := Round(val, roundPos)
		If roundPos == 0 And SubStr(val, -1, 1) == 0 {
			; Rounded to nearest integer and the ones place is 0
			; Show the decimal to indicate the 0 is significant
			val .= "."
		}
		val := SubStr(val, 1, endPos)
		val .= suffix
	}
}

; More of a "less dumb round" - if rounding sends the value to 0 then it
; rounds it to the same number of digits in scientific notation instead
SmartRound(val, digits) {
	rounded := Round(val, digits)
	If rounded != 0 {
		Return rounded
	}
	val := String(Format("{:e}", val))
	i := InStr(val, "e")
	suffix := SubStr(val, i)
	val := SubStr(val, 1, i-1)
	Return Round(val, digits) . suffix
}

; Generic calculation function, alternates between multiplying and adding values to val
; If reverse is True then it performs the inverse calculation instead
Convert(val, params, reverse := False) {
	mult := (reverse And Mod(params.Length, 2) == 0) ? False : True
	index := reverse ? -1 : 1
	diff := reverse ? -1 : 1
	end := reverse ? -params.Length - 1 : params.Length + 1
	While index != end {
		If mult {
			val := reverse ? val / params[index] : val * params[index]
		} Else {
			val := reverse ? val - params[index] : val + params[index]
		}
		mult := !mult
		index += diff
	}
	Return val
}

; Does some cleaning up of user input for ::convert:: below, to match unit alias lists
; Main point was to drastically reduce how many distinct aliases had to be listed
FormatUnit(&unit) {
	unit := StrReplace(unit, "^") ; m^3 -> m3
	unit := StrReplace(unit, " ") ; fluid ounce -> fluidounce
	unit := StrReplace(unit, "uared") ; metersquared -> metersq
	unit := StrReplace(unit, "uare") ; squaremeter -> sqmeter
	unit := StrReplace(unit, "sq", "2") ; sqmeter -> 2meter
	unit := StrReplace(unit, "bic") ; cubicmeter -> cumeter
	unit := StrReplace(unit, "bed") ; metercubed -> metercu
	unit := StrReplace(unit, "be") ; cubemeter -> cumeters
	unit := StrReplace(unit, "cu", "3") ; cumeter -> 3meters
	If IsNumber(num := SubStr(unit, 1, 1)) {
		unit := SubStr(unit, 2) . num ; 3meter -> meters3
		If unit = "p3" { ; cup -> 3p -> cup
			unit := "cup"
		}
	}
	If endsInNumber := IsNumber(endingNum := SubStr(unit, -1, 1)) {
		unit := SubStr(unit, 1, -1) ; meters3 -> meters
	}
	If SubStr(unit, -1, 1) = "s" And StrLen(unit) != 1 {
		unit := SubStr(unit, 1, -1) ; meters -> meter
	}
	If endsInNumber {
		unit .= endingNum ; meter -> meter3
	}
}

; Converts between units.  Format:  `convert\valueToConvert, startingUnit, destinationUnit\
; Temperature: celsius, fahrenheit, kelvin, rankine
; Length: meter, inch, foot, yard, fathom, furlong, mile, nautical mile, astronomical unit, lightyear, parsec
; Area: meter², inch², foot², yard², mile², acre, hectare
; Volume: liter, meter³, teaspoon, tablespoon, fluid ounce, cup, pint, quart, gallon, inch³, foot³, yard³, mile³
; Mass: gram, ounce, pound, stone, ton, metric ton
; Time: second, minute, hour, day, week, fortnight, year, decade, score, century, millennium
; Angular measure: degree, radian, gradian, arcminute, arcsecond
::convert:: {
	GatherInput(&input, &backspaceCount)
	; Backspace input
	Send "{Backspace " . backspaceCount . "}"
	; Break up input by spaces or commas, depending on whether or not commas are present
	input := InStr(input, ",") ? StrSplit(input, ",", " ") : StrSplit(input, " ")
	; All valid input has 3 parts:  value, unit1, and unit2
	If input.Length != 3 {
		Send "Incorrect format"
		Return
	}
	val := input[1]
	unit1 := input[2]
	unit2 := input[3]
	; Precede value with ! to maintain significant figure count
	HonorSigFigs := SubStr(val, 1, 1) == "!" ? (val := SubStr(val, 2), True) : False
	; Postcede value with ! to skip writing the unit after the result
	NoSuffix := SubStr(val, -1, 1) == "!" ? (val := SubStr(val, 1, -1), True) : False
	FormatVal(&val)
	If val == "NaN" {
		Send "NaN"
		Return
	}
	; Inner map's keys double as unit name and as the display unit text when sending results
	; Keys refer to list of lists.  First list is acceptable aliases for that unit (after input parsing)
	; Second list is parameters instructing on how to convert that unit to the base unit for its dimension
	; Base unit for each dimension is first listed
	dimensions := Map("temperature", Map(
						"℃", [["c", "celsiu"], []]
						, "℉", [["f", "fahrenheit"], [1, -32, 5/9]]
						, " K", [["k", "kelvin"], [1, -273.15]]
						, "°R", [["r", "rankine"], [5/9, -273.15]] )
					, "length", Map(
						" meters", [["m", "me", "meter", "metre"], []]
						, '"', [["in", "inch", "inche", '"'], [.0254]]
						, "'", [["ft", "foot", "feet", "'"], [.3048]]
						, " yards", [["y", "yd", "yard"], [.9144]]
						, " fathoms", [["fathom"], [1.8288]]
						, " furlongs", [["furlong"], [201.168]]
						, " miles", [["mi", "mile"], [1609.344]]
						, " nautical miles", [["nauticalmile"], [1852]]
						, " astronomical units", [["au", "astronomical units"], [149597870700]]
						, " lightyears", [["ly", "lightyear"], [9460730472580800]]
						, " parsecs", [["ps", "parsec"], [149597870700*648000/3.14159265358979]] )
					, "area", Map(
						" m²", [["m2", "meter2", "metre2"], []]
						, " in²", [["in2", "inch2", "inche2"], [6.4516/10000]]
						, " ft²", [["ft2", "foot2", "feet2"], [929.0304/10000]]
						, " yd²", [["y2", "yd2", "yard2"], [0.83612736]]
						, " miles²", [["mi2", "mile2"], [2589988.110336]]
						, " acres", [["ac", "acre"], [4046.8564224]]
						, " hectares", [["ha", "hectare"], [10000]] )
					, "volume", Map(
						" liters", [["l", "liter"], []]
						, " m³", [["m3", "meter3", "metre3"], [1000]]
						, " tsp", [["tsp", "teaspoon"], [4.92892159375/1000]]
						, " tbsp", [["tb", "tbsp", "tablespoon"], [3*4.92892159375/1000]]
						, " fluid ounces", [["fl", "fluidounce", "flounce", "fl.ounce", "floz", "fl.oz", "fluidoz"], [.0295735295625]]
						, " cups", [["c", "cup"], [236.5882365/1000]]
						, " pints", [["p", "pint"], [236.5882365/500]]
						, " quarts", [["q", "quart"], [236.5882365/250]]
						, " gallons", [["g", "gal", "gallon"], [3.785411784]]
						, " in³", [["in3", "inch3", "inche3"], [16.387064/1000]]
						, " ft³", [["ft3", "foot3", "feet3"], [28.316846592]]
						, " yd³", [["y3", "yd3", "yard3"], [764.554857984]]
						, " miles³", [["mi3", "mile3"], [5451776000*764.554857984]] )
					, "mass", Map(
						" grams", [["g", "gram"], []]
						, " oz", [["oz", "ounce"], [28.349523125]]
						, " lbs", [["lb", "pound"], [453.59237]]
						, " stones", [["st", "stone", "s"], [6350.29318]]
						, " tons", [["ton"], [907184.74]]
						, " metric tons", [["mt", "metricton"], [1000000]] )
					, "time", Map(
						" seconds", [["s", "sec", "second"], []]
						, " minutes", [["m", "min", "minute"], [60]]
						, " hours", [["h", "hour"], [3600]]
						, " days", [["d", "day"], [86400]]
						, " weeks", [["w", "week"], [604800]]
						, " fortnights", [["fn", "fortnight"], [1209600]]
						, " years", [["y", "year"], [31557600]]
						, " decades", [["dec", "decade"], [315576000]]
						, " scores", [["sc", "score"], [631152000]]
						, " centuries", [["c", "century", "centurie"], [3155760000]]
						, " millenniums", [["mil", "mill", "millennium", "millennia"], [31557600000]] )
					, "angular measure", Map(
						"°", [["d", "deg", "degree"], []]
						, " radians", [["r", "rad", "radian"], [180/3.14159265358979]]
						, "gradians", [["g", "grad", "gradian"], [.9]]
						, "'", [["am", "arcm", "arcmin", "arcminute"], [1/60]]
						, '"', [["as", "arcs", "arcsec", "arcsecond"], [1/3600]] ) )
	; SI prefixes and their associated factors
	metricPrefixes := Map("quetta", 1e30,  "ronna", 1e27,  "yotta", 1e24,  "zetta", 1e21,  "exa", 1e18,  "peta", 1e15,  "tera", 1e12,  "giga", 1e9,  "mega", 1e6,  "kilo", 1e3,  "hecto", 1e2,  "deca", 10,  "deci", 1e-1,  "centi", 1e-2,  "milli", 1e-3,  "micro", 1e-6,  "nano", 1e-9,  "pico", 1e-12,  "femto", 1e-15,  "atto", 1e-18,  "zepto", 1e-21,  "yocto", 1e-24,  "ronto", 1e-27,  "quecto", 1e-30, "Q", 1e30,  "R", 1e27,  "Y", 1e24,  "Z", 1e21,  "E", 1e18,  "P", 1e15,  "T", 1e12,  "G", 1e9,  "M", 1e6,  "k", 1e3,  "h", 1e2,  "da", 10,  "d", 1e-1,  "c", 1e-2,  "m", 1e-3,  "mu", 1e-6,  "μ", 1e-6, "n", 1e-9,  "p", 1e-12,  "f", 1e-15,  "a", 1e-18,  "z", 1e-21,  "y", 1e-24,  "r", 1e-27,  "q", 1e-30)
	
	; SI symbols and the full prefix names they shorten - results always display the long name
	metricSymbols := Map("Q", "quetta",  "R", "ronna",  "Y", "yotta",  "Z", "zetta",  "E", "exa",  "P", "peta",  "T", "tera",  "G", "giga",  "M", "mega",  "k", "kilo",  "h", "hecto",  "da", "deca",  "d", "deci",  "c", "centi",  "m", "milli",  "mu", "micro",  "μ", "micro", "n", "nano",  "p", "pico",  "f", "femto",  "a", "atto",  "z", "zepto",  "y", "yocto",  "r", "ronto",  "q", "quecto")
	
	; Some parsing to simplify user input and fit the formats allowed above
	FormatUnit(&unit1)
	FormatUnit(&unit2)
	; At this point user input will either be a valid match to a unit in the supported units list, perhaps with an SI prefix, or it will be invalid.  
	unit1Matches := []
	unit2Matches := []
	For dimension, units In dimensions {
		For unit, aliases In units {
			For alias In aliases[1] {
				If SubStr(unit1, -StrLen(alias)) = alias {
					; The input ends in a valid unit alias - if that's the full input, or if an SI prefix completes the full input, accept it as a match
					prefix := ""
					If StrLen(unit1) > unitLen := StrLen(alias) {
						prefix := SubStr(unit1, 1, -unitLen)
						; Some prefixe symbols are case-sensitive so be careful.  First see if there's an exact case match, use that if there is
						; Then see if there's a lowercase match - will allow user to type for example "Kilo" for "kilo"
						; Lastly check for an uppercase match - for example if they typed gm instead of Gm for Gigameter
						If !metricPrefixes.Has(prefix) {
							If metricPrefixes.Has(StrLower(prefix)) {
								prefix := StrLower(prefix)
							} Else If metricPrefixes.Has(StrUpper(prefix)) {
								prefix := StrUpper(prefix)
							} Else {
								Continue
							}
						}
					}
					unit1Matches.push([dimension, unit, prefix])
				}
				If SubStr(unit2, -StrLen(alias)) = alias {
					prefix := ""
					If StrLen(unit2) > unitLen := StrLen(alias) {
						prefix := SubStr(unit2, 1, -unitLen)
						If !metricPrefixes.Has(prefix) {
							If metricPrefixes.Has(StrLower(prefix)) {
								prefix := StrLower(prefix)
							} Else If metricPrefixes.Has(StrUpper(prefix)) {
								prefix := StrUpper(prefix)
							} Else {
								Continue
							}
						}
					}
					unit2Matches.push([dimension, unit, prefix])
				}
			}
		}
	}
	; No match found for unit1, unit2
	If unit1Matches.Length == 0 {
		Send "Unknown unit: " . unit1
		Return
	} Else If unit2Matches.Length == 0 {
		Send "Unknown unit: " . unit2
		Return
	}
	matchFound := False
	For match1 In unit1Matches {
		For match2 In unit2Matches {
			If match1[1] == match2[1] {
				; The matches are the same dimension - success
				unit1 := match1
				unit2 := match2
				matchFound := True
				Break
			}
		}
		If matchFound {
			Break
		}
	}
	If !matchFound {
		Send "Dimensional mismatch"
		Return
	}
	; Using a new value because we may need to reference the original if user is respecting sig figs
	newVal := val
	; If we have an SI prefix, use it to convert val to the base unit first - careful with area and volume units
	If (prefix := unit1[3]) != "" {
		If SubStr(unit1[2], -1, 1) == "2" {
			newVal *= metricPrefixes[prefix]**2
		} Else If SubStr(unit1[2], -1, 1) == "3" {
			newVal *= metricPrefixes[prefix]**3
		} Else {
			newVal *= metricPrefixes[prefix]
		}
	}
	; Convert val to the base unit for its dimension
	newVal := Convert(newVal, dimensions[unit1[1]][unit1[2]][2])
	; Now convert it from the base unit to the destination unit
	newVal := Convert(newVal, dimensions[unit2[1]][unit2[2]][2], True)
	; If the destination unit also has an SI prefix, then convert from the base unit to it
	If (prefix := unit2[3]) != "" {
		If SubStr(unit2[2], -1, 1) == "2" {
			newVal /= metricPrefixes[prefix]**2
		} Else If SubStr(unit2[2], -1, 1) == "3" {
			newVal /= metricPrefixes[prefix]**3
		} Else {
			newVal /= metricPrefixes[prefix]
		}
	}
	If HonorSigFigs {
		DetermineSigFigs(val, &SigFigs)
		FormatSigFigs(&newVal, SigFigs)
	} Else {
		newVal := SmartRound(newVal, 2)
		If Integer(newVal) == newVal {
			newVal := Integer(newVal)
		}
	}
	If (prefix := unit2[3]) != "" {
		If metricSymbols.Has(prefix) {
			prefix := metricSymbols[prefix]
		}
		If SubStr(unit2[2], 1, 1) == " " {
			suffix := " " . prefix . SubStr(unit2[2], 2)
		}
	} Else {
		suffix := unit2[2]
	}
	If NoSuffix {
		suffix := ""
	}
	Send newVal . suffix
}



; Below code taken from this reddit comment:
; https://old.reddit.com/r/AutoHotkey/comments/129491b/how_to_force_ahk_to_evaluate_a_string_as_an/jepkhfb/
; Then ported to autohotkey v2 and very heavily modified to fix bugs and expand capability.  
; Evaluates a string.  Allows numbers with and without decimals or in scientific notation, parenthesis (), exponentiation ^
; , multiplication *, division /, floor division //, addition +, subtraction -
; , as well as the functions abs(), ceil(), exp(), floor(), log(), ln(), sqrt(), asin(), acos(), atan(), sin(), cos(), and tan().  
; Correctly follows the order of operations and understands implicit multiplication.  Allows pi and e as constants.  
calc(str, first := True) {
	; Detects numbers like 3, 3., 3.3, 3.3e-3, 3.33e3, 3.01e+4, 3e3, 3.e3, .3e3, .3, and all of those but negative
	; Avoids catching a negative if it's really just subtraction, to avoid concatenation errors
    rgx := {para :"^(.*?)\(([\dN+*/.^-]*?)\)(.*?)$"
            ,num1 :"^(.*?)((?<![\d.])(?:-)?(?:-?\d+\.\d+[Ee][+-]?\d+|-?\.\d+[Ee][-+]?\d+|-?\d+e[-+]?\d+|-?\d+\.e[-+]?\d+|\d+\.\d+|\d+\.|\d+|\.\d+)N?)"
            ,num2 :"((?<![\d.])(?:-)?(?:-?\d+\.\d+[Ee][+-]?\d+|-?\.\d+[Ee][-+]?\d+|-?\d+e[-+]?\d+|-?\d+\.e[-+]?\d+|\d+\.\d+|\d+\.|\d+|\.\d+)N?)(.*?)$"}
    If first {                                                      ; Only do during first time run
		str := RegExReplace(str, "([\d.)])([a-df-zA-DF-Z]|e(?![-+]?\d+))", "$1*$2")  ; Letter dot or close paren followed by a letter is implied multiplication: 3sin -> 3*sin
		str := RegExReplace(str, "([a-df-zA-DF-Z]|e(?!-?\d+))(\d|\.)", "$1*$2")      ; letter followed by digit or dot is implied multiplication: pi3 -> pi*3
		str := StrReplace(str, "pi", "3.141592653589793238")
		str := StrReplace(str, "arc", "a")
		funcs := Map("abs", "{01}", "ceil", "{02}", "exp", "{03}", "floor", "{04}", "log", "{05}", "ln", "{06}", "sqrt", "{07}", "asin", "{08}", "acos", "{09}", "atan", "{10}", "sin", "{11}", "cos", "{12}", "tan", "{13}")
		For key, item In funcs {
			str := StrReplace(str, key, item)
		}
		str := RegExReplace(str, "(?<!\d|\.)[Ee](?!xp|il|-?\d+)", "2.718281828459045235")
		If RegExMatch(str, "[a-df-zA-DF-Z]|(?<!\d|\.)[eE](?![+-]?\d+)") {
			; Above code ensures all valid letters except e in scientific notation are now gone
			; So if any remain, there's an error in user input
			Return "NaN"
		}
		str := RegExReplace(str, "(\d)\(", "$1*(")                  ; Turn 3(4+5) into 3*(4+5) to prevent concatenation
		str := RegExReplace(str, "\)(\d|\.)", ")*$1")               ; Turn (4+5)3 into (4+5)*3 for same reason
		str := RegExReplace(str, "\)\(", ")*(")                     ; Turn (3+4)(5+6) into (3+4)*(5+6) for same reason
		str := RegExReplace(str, "-\(", "-1*(")
        StrReplace(str, "(", "(", 0, &pOpen)                        ; Count open parens
        StrReplace(str, ")", ")", 0, &pClose)                       ; Count close parens
        If (pOpen != pClose) {                                      ; Error if they don't match
			If pClose > pOpen {
				Return "Open/close parentheses mismatch."
			}
			While pOpen > pClose {
				str .= ")"
				pClose += 1
			}
		}
        str := StrReplace(str, " ")                                 ; Remove all spaces
		While InStr(str, "---") {                                   ; Handle manually because rest of code can't
			str := StrReplace(str, "---", "-")
		}
		If SubStr(str, 1, 2) == "--" {                              ; Initial -- confuses the subtract function
			str := SubStr(str, 3)
		}
        While RegExMatch(str, rgx.para, &m) {                 		; If parens still exist
			m.2 := calc(m.2, False)
			func := SubStr(m.1, -4)
			If (m.2 <= 0 And (func == "{05}" Or func == "{06}")) {
				func := func == "{05}" ? "log" : "ln"
				Return "Nonpositive argument for " . func . ": " . m.2
			} Else If (m.2 < 0 And func == "{07}") {
				Return "Negative argument for sqrt: " . m.2
			} Else If (Abs(m.2) > 1 And (func == "{08}" Or func == "{09}")) {
				func := func == "{08}" ? "asin" : "acos"
				Return "Invalid input for " . func . ": " . m.2
			}
			Switch {
				Case func = "{01}": m.1 := SubStr(m.1, 1, -4), m.2 := Abs(m.2)
				Case func = "{02}": m.1 := SubStr(m.1, 1, -4), m.2 := Ceil(m.2)
				Case func = "{03}": m.1 := SubStr(m.1, 1, -4), m.2 := Exp(m.2)
				Case func = "{04}": m.1 := SubStr(m.1, 1, -4), m.2 := Floor(m.2)
				Case func = "{05}": m.1 := SubStr(m.1, 1, -4), m.2 := Log(m.2)
				Case func = "{06}": m.1 := SubStr(m.1, 1, -4), m.2 := Ln(m.2)
				Case func = "{07}": m.1 := SubStr(m.1, 1, -4), m.2 := Sqrt(m.2)
				Case func = "{08}": m.1 := SubStr(m.1, 1, -4), m.2 := Asin(m.2)
				Case func = "{09}": m.1 := SubStr(m.1, 1, -4), m.2 := Acos(m.2)
				Case func = "{10}": m.1 := SubStr(m.1, 1, -4), m.2 := Atan(m.2)
				Case func = "{11}": m.1 := SubStr(m.1, 1, -4), m.2 := Sin(m.2)
				Case func = "{12}": m.1 := SubStr(m.1, 1, -4), m.2 := Cos(m.2)
				Case func = "{13}": m.1 := SubStr(m.1, 1, -4), m.2 := Tan(m.2)
			}
			If SubStr(m.3, 1, 1) == "^" And m.2 < 0 {
				; User did something like "(-4)^x", which won't be allowed for non-integer values of x
				; Later code will just see it as "-4^x", though, which is always allowed
				; So, mark it with an N so the later code can tell the difference and properly return an error if necessary
				; Later code is like 7 lines below this btw
				m.2 := m.2 . "N"
			}
            str := m.1 . m.2 . m.3
		}
    }
	While RegExMatch(str, rgx.num1 . "(\^)" . rgx.num2, &m) { ; While "number sign number" exists
		If SubStr(m.2, -1, 1) == "N" {
			m.2 := SubStr(m.2, 1, -1)
			If m.4 != Integer(m.4) {
				Return "Invalid non-integer exponent for a negative base: (" . m.2 . ")^" . m.4
			}
		}
		If m.2 == 0 And m.4 < 0 {
			Return "Invalid negative exponent for a zero base: 0^" . m.4
		}
		if m.2 > 0 {
			result := m.2**m.4
		} else {
			result := -Abs(m.2)**m.4
		}
		str := m.1 . result . m.5
	}
	While RegExMatch(str, rgx.num1 . "([*/]|//)" . rgx.num2, &m) {
		If m.4 == 0 And (m.3 == "/" or m.3 == "//") {
			Return "Division by zero"
		}
		Switch m.3 {                                                ; Check sign and do appropriate operation
			Case "*"  : str := m.1 . (m.2 * m.4) .  m.5
			Case "//" : str := m.1 . Floor(m.2 / m.4) . m.5
			Case "/"  : str := m.1 . (m.2 / m.4) .  m.5
		}
	}
	While RegExMatch(str, rgx.num1 . "((?<![eE])[+-])" . rgx.num2, &m) {
		Switch m.3 {
			Case "+"  : str := m.1 . (m.2 + m.4) .  m.5
			Case "-"  : str := m.1 . (m.2 - m.4) .  m.5
		}
	}
	If first {
		str := Round(str, 10)                                       ; Because results like 10.800000000000001
	}
	if str == 0 {
		str := 0                                                    ; Weird edge case sometimes gave -0
	}
	If InStr(str, ".") {                                            ; If decimal
        str := RTrim(str, "0")                                      ; Remove trailing 0s
	}
    Return RTrim(str, ".")                                          ; Return after removing trailing decimal
}

::calc:: {
	GatherInput(&text, &backspaceCount)
	; How the user indicates a specific rounding amount
	If i := InStr(text, ",") {
		roundNum := SubStr(text, i+1)
		text := SubStr(text, 1, i-1)
	}
	out := ""
	; If calculation ends in !, write result as an equation
	If SubStr(text, -1, 1) == "!" {
		text := SubStr(text, 1, -1)
		out .= text . " = "
	}
	text := StrReplace(text, " ")
	result := calc(text)
	If i {
		out .= Round(result, roundNum)
	} Else {
		out .= result
	}
	; Below line used to easily create more unit tests
	; out := 'UnitTest("calc", "' . text . '", "' . out . '")'
	Send "{Backspace " . backspaceCount . "}{Raw}" . out
}


; Define a testing function
UnitTest(functionName, input, expectedResult) {
    result := %functionName%(input)
    If result != expectedResult {
        MsgBox("Fail: " . functionName . "('" . input . "') returned '" . result . "', expected '" . expectedResult . "'")
    }
}

::unittest:: {
	UnitTest("calc", "3+4", "7")
	UnitTest("calc", "5-2", "3")
	UnitTest("calc", "6*7", "42")
	UnitTest("calc", "8/2", "4")
	UnitTest("calc", "10//3", "3")
	UnitTest("calc", "9^2", "81")
	UnitTest("calc", "(3+4)*(5-2)", "21")
	UnitTest("calc", "6*(7-2)/2", "15")
	UnitTest("calc", "8/(2*(4-2))", "2")
	UnitTest("calc", "((1+2)*(3+4))/(5+6)", "1.9090909091")
	UnitTest("calc", "3+4*5", "23")
	UnitTest("calc", "2^3+6/2", "11")
	UnitTest("calc", "2*(3+4)^2", "98")
	UnitTest("calc", "(8+1)/(3-2)^2", "9")
	UnitTest("calc", "abs(-5)", "5")
	UnitTest("calc", "ceil(4.3)", "5")
	UnitTest("calc", "exp(2)", "7.3890560989")
	UnitTest("calc", "floor(4.8)", "4")
	UnitTest("calc", "log(10)", "1")
	UnitTest("calc", "ln(2.718)", "0.9998963157")
	UnitTest("calc", "sqrt(16)", "4")
	UnitTest("calc", "e^7-exp(7)", "0")
	UnitTest("calc", "asin(0.5)", "0.5235987756")
	UnitTest("calc", "acos(0.5)", "1.0471975512")
	UnitTest("calc", "atan(1)", "0.7853981634")
	UnitTest("calc", "sin(30)", "-0.9880316241")
	UnitTest("calc", "cos(60)", "-0.9524129804")
	UnitTest("calc", "tan(45)", "1.6197751905")
	UnitTest("calc", "----5", "5")
	UnitTest("calc", "---5", "-5")
	UnitTest("calc", "4--------3", "7")
	UnitTest("calc", "4-------3", "1")
	UnitTest("calc", "2^3*sqrt(25)-(8+1)/((3-2)^2)", "31")
	UnitTest("calc", "3*abs(-4+5)/cos(60)-exp(1)", "-5.8681758993")
	UnitTest("calc", "((2+3)*(4-1))^2/sqrt(16)", "56.25")
	UnitTest("calc", "1+2*(3+4*(5+6*(7+8*(9+10)))/9)/8", "108.3055555556")
	UnitTest("calc", "1+23+45+6", "75")
	UnitTest("calc", "3+4*5/(2+1)", "9.6666666667")
	UnitTest("calc", "(1+2)*(3+4)/(5+6)", "1.9090909091")
	UnitTest("calc", "2^3*(4-1)+sqrt(16)/ln(2)", "29.7707801636")
	UnitTest("calc", "ceil(3.6)*floor(2.8)+exp(1)^2", "15.3890560989")
	UnitTest("calc", "(((2+3)*4)-(1+2))/(5-6)", "-17")
	UnitTest("calc", "sqrt(sqrt(16))", "2")
	UnitTest("calc", "floor(ceil(5.5))", "6")
	UnitTest("calc", "(1+2*(3+(4*(5+(6*(7+(8*9)))))))", "3839")
	UnitTest("calc", "sin(30)+cos(60)", "-1.9404446045")
	UnitTest("calc", "tan(45)-asin(0.5)", "1.0961764149")
	UnitTest("calc", "acos(cos(0.5236))", "0.5236")
	UnitTest("calc", "atan(1)+sin(0.5236)-cos(0.5236)", "0.4193744322")
	UnitTest("calc", "0.5+0.25", "0.75")
	UnitTest("calc", "1.5*2.0/3.333", "0.900090009")
	UnitTest("calc", "0.1^2+0.01^2+0.001^2", "0.010101")
	UnitTest("calc", "sqrt(4.0)/2.5", "0.8")
	UnitTest("calc", "3/4*5", "3.75")
	UnitTest("calc", "2^10*3^5/5^3", "1990.656")
	UnitTest("calc", "-2.e-2+3", "2.98")
	UnitTest("calc", "3+2e4", "20003")
	UnitTest("calc", ".23e6/4", "57500")
	UnitTest("calc", "sqrt(2)^10", "32")
	UnitTest("calc", "sqrt(2)^3*(sin(45)+cos(45))/2.5", "1.5570214287")
	UnitTest("calc", "(1+2*(3+4/2.0))^2", "121")
	UnitTest("calc", "exp(1)^2*3.5-floor(sqrt(9.9))", "22.8616963463")
	UnitTest("calc", "2^0", "1")
	UnitTest("calc", ".9(8+3)", "9.9")
	UnitTest("calc", "0^5", "0")
	UnitTest("calc", "(-2)^3", "-8")
	UnitTest("calc", "4-3*-2", "10")
	UnitTest("calc", "10^-2", "0.01")
	UnitTest("calc", "1.5e2^2", "22500")
	UnitTest("calc", "1.5e+2^2", "22500")
	UnitTest("calc", "exp(2*(1+sin(0.5236)))", "20.0855795191")
	UnitTest("calc", "abs(-5)+ceil(-3.8)+floor(4.2)", "6")
	UnitTest("calc", "3--3", "6")
	UnitTest("calc", "3*-(4+8)", "-36")
	UnitTest("calc", "abs(-1)+ceil(-1)+floor(-1)", "-1")
	UnitTest("calc", "log(0.00001)", "-5")
	UnitTest("calc", "2^3+sqrt(16)*(sin(30)+cos(60))/abs(-5)", "6.4476443164")
	UnitTest("calc", "(1+2*(3+sqrt(16)))/(5-(exp(1)^2))", "-6.2786302953")
	UnitTest("calc", "1.2+(7.2-3)^9.2//17/7+ceil(4.3-exp(2.2))*abs(-8.2)-floor(-9.9)-log(8.443e*ln(sqrt(84)))+asin(.2)-acos(.4)+atan(.8)-sin(1.6)+cos(3.2)-tan(6.4)", "4527.7239284154")
	UnitTest("calc", "(4*3).9", "10.8")
	UnitTest("calc", "sqrt(-8)", "Negative argument for sqrt: -8")
	UnitTest("calc", "ln(-4)", "Nonpositive argument for ln: -4")
	UnitTest("calc", "log(0)", "Nonpositive argument for log: 0")
	UnitTest("calc", "asin(17)", "Invalid input for asin: 17")
	UnitTest("calc", "arccos(-4)", "Invalid input for acos: -4")
	UnitTest("calc", "0^-4.2", "Invalid negative exponent for a zero base: 0^-4.2")
	UnitTest("calc", "(-4)^7.2", "Invalid non-integer exponent for a negative base: (-4)^7.2")
	UnitTest("calc", "-4^2", "-16")
	UnitTest("calc", "1/0", "Division by zero")
	Send "{Raw}Done!"
}