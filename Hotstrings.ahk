; Type a backslash to activate any given Hotstring
#Hotstring EndChars \
endchar = \



; WIN+Z, pause hotstrings.ahk
#z::Suspend, Toggle



; Removes the \ you typed to activate the Hotstring
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
:: degreesC::℃
::degreesC::℃
:: degreeC::℃
::degreeC::℃
:: degreesF::℉
::degreesF::℉
:: degreeF::℉
::degreeF::℉
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
::/0::�
::bullet::•
::flat::♭
::sharp::♯


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
:::/::😕
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
::please::🥺
::beg::🥺
::plead::🥺
::cute::🥹
::happytears::🥹
::melting::🫠
::salute::🫡
::monocle::🧐
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
::hearts::💚🤎💙🧡🤍🖤❤️💛💜
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
::check::✔️
::checkmark::✔️
::cross::✝️
::christian::✝️
::jewish::✡️
::starofdavid::✡️
::menorah::🕎
;::x::❌
::zzz::💤
::shootingstar::💫
::dizzy::💫
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
::note::🎵
::plainnote::♪
::textnote::♪
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



; Bulk superscripting
::`^^::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { "+":"⁺", "-":"⁻", "=":"⁼", "(":"⁽", ")":"⁾"
		, 0:"⁰", 1:"¹", 2:"²", 3:"³", 4:"⁴", 5:"⁵", 6:"⁶", 7:"⁷", 8:"⁸", 9:"⁹"
		, a:"ᵃ", b:"ᵇ", c:"ᶜ", d:"ᵈ", e:"ᵉ", f:"ᶠ", g:"ᵍ", h:"ʰ", i:"ⁱ", j:"ʲ", k:"ᵏ", l:"ˡ", m:"ᵐ", n:"ⁿ", o:"ᵒ", p:"ᵖ", r:"ʳ", s:"ˢ", t:"ᵗ", u:"ᵘ", v:"ᵛ", w:"ʷ", x:"ˣ", y:"ʸ", z:"ᶻ" }
	mapUpper := { A:"ᴬ", B:"ᴮ", D:"ᴰ", E:"ᴱ", G:"ᴳ", H:"ᴴ", I:"ᴵ", J:"ᴶ", K:"ᴷ", L:"ᴸ", M:"ᴹ", N:"ᴺ", O:"ᴼ", P:"ᴾ", R:"ᴿ", T:"ᵀ", U:"ᵁ", V:"ⱽ", W:"ᵂ" }
	
	out := ""
	loop, parse, text
		if A_LoopField is upper
			out .= mapUpper.HasKey(A_LoopField) ? mapUpper[A_LoopField] : A_LoopField
		else
			out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk subscripting
::__::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { "+":"₊", "-":"₋", "=":"₌", "(":"₍", ")":"₍"
		, 0:"₀", 1:"₁", 2:"₂", 3:"₃", 4:"₄", 5:"₅", 6:"₆", 7:"₇", 8:"₈", 9:"₉"
		, a:"ₐ", e:"ₑ", h:"ₕ", i:"ᵢ", j:"ⱼ", k:"ₖ", l:"ₗ", m:"ₘ", n:"ₙ", o:"ₒ", p:"ₚ", r:"ᵣ", s:"ₛ", t:"ₜ", u:"ᵤ", v:"ᵥ", x:"ₓ" }
	
	out := ""
	loop, parse, text
		if A_LoopField is upper
			out .= A_LoopField
		else
			out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk upside-down
::flip::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	; Reverse order of input
	StringReplace, text, text, %a_space%, ⠀, All
	tempText := ""
	loop, parse, text
		tempText = %A_LoopField%%tempText%
	text := tempText
	StringReplace, text, text, ⠀, %a_space%, All
	
	map := { "&":"⅋", ">":"<", "<":">", "}":"{", "{":"}", "]":"[", "[":"]", ")":"(", "(":")", "_":"‾", "!":"¡", "?":"¿", ".":"˙", """":",,", "'":",", ",":"'", "^":"v"
			, 0:"0", 1:"Ɩ", 2:"ᄅ", 3:"Ɛ", 4:"ㄣ", 5:"ϛ", 6:"9", 7:"ㄥ", 8:"8", 9:"6"
			, "a":"ɐ", "b":"q", "c":"ɔ", "d":"p", "e":"ǝ", "f":"ɟ", "g":"ƃ", "h":"ɥ", "i":"ᴉ", "j":"ɾ", "k":"ʞ", "l":"l", "m":"ɯ", "n":"u", "o":"o", "p":"d", "q":"b", "r":"ɹ", "s":"s", "t":"ʇ", "u":"n", "v":"ʌ", "w":"ʍ", "x":"x", "y":"ʎ", "z":"z" }
	mapUpper := { "A":"∀", "B":"q", "C":"Ɔ", "D":"p", "E":"Ǝ", "F":"Ⅎ", "G":"פ", "H":"H", "I":"I", "J":"ſ", "K":"ʞ", "L":"˥", "M":"W", "N":"N", "O":"O", "P":"Ԁ", "Q":"Q", "R":"ɹ", "S":"S", "T":"┴", "U":"∩", "V":"Λ", "W":"M", "X":"X", "Y":"⅄", "Z":"Z" }
	
	out := ""
	loop, parse, text
		if A_LoopField is upper
			out .= mapUpper.HasKey(A_LoopField) ? mapUpper[A_LoopField] : A_LoopField
		else
			out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk unbraille code
::unbraille::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, MVL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	; If they didn't type anything, take the text from the clipboard
	if StrLen(text) = 0
	{
		text := clipboard
		if StrLen(text) > 5000
		{
			return
		}
		backspace := 1
	}
	
	; Detects if user pasted text, uses that if so
	else if Asc(text) = 22
	{
		text := clipboard
		if StrLen(text) > 5000
		{
			return
		}
		backspace := StrLen(text) + 1
	}
	else
	{
		backspace := StrLen(text) + 1
	}
	
	map := { "⠠⠁":"A", "⠠⠃":"B", "⠠⠉":"C", "⠠⠙":"D", "⠠⠑":"E", "⠠⠋":"F", "⠠⠛":"G", "⠠⠓":"H", "⠠⠊":"I", "⠠⠚":"J", "⠠⠅":"K", "⠠⠇":"L", "⠠⠍":"M", "⠠⠝":"N", "⠠⠕":"O", "⠠⠏":"P", "⠠⠟":"Q", "⠠⠗":"R", "⠠⠎":"S", "⠠⠞":"T", "⠠⠥":"U", "⠠⠧":"V", "⠠⠺":"W", "⠠⠭":"X", "⠠⠽":"Y", "⠠⠵":"Z"
			, "⠂":",", "⠆":";", "⠒":":", "⠲":".", "⠖":"!", "⠶":"(", "⠶":")", "⠦":"?", "⠦":"""", "⠦":"<", "⠴":">", "⠌":"/", "⠄":"'", "⠤":"-", "⠀":" "
			, "⠁":"a", "⠃":"b", "⠉":"c", "⠙":"d", "⠑":"e", "⠋":"f", "⠛":"g", "⠓":"h", "⠊":"i", "⠚":"j", "⠅":"k", "⠇":"l", "⠍":"m", "⠝":"n", "⠕":"o", "⠏":"p", "⠟":"q", "⠗":"r", "⠎":"s", "⠞":"t", "⠥":"u", "⠧":"v", "⠺":"w", "⠭":"x", "⠽":"y", "⠵":"z"
			, "⠼⠁":"1", "⠼⠃":"2", "⠼⠉":"3", "⠼⠙":"4", "⠼⠑":"5", "⠼⠋":"6", "⠼⠛":"7", "⠼⠓":"8", "⠼⠊":"9", "⠼⠚":"0" }
	
	out := ""
	loop, parse, text
		out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " backspace "}{Raw}" out
return

; Bulk braille
::braille::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { ",":"⠂", ";":"⠆", ":":"⠒", ".":"⠲", "!":"⠖", "(":"⠶", ")":"⠶", "?":"⠦", """":"⠦", "<":"⠦", ">":"⠴", "/":"⠌", "'":"⠄", "-":"⠤", " ":"⠀"
		, 1:"⠼⠁", 2:"⠼⠃", 3:"⠼⠉", 4:"⠼⠙", 5:"⠼⠑", 6:"⠼⠋", 7:"⠼⠛", 8:"⠼⠓", 9:"⠼⠊", 0:"⠼⠚"
		, a:"⠁", b:"⠃", c:"⠉", d:"⠙", e:"⠑", f:"⠋", g:"⠛", h:"⠓", i:"⠊", j:"⠚", k:"⠅", l:"⠇", m:"⠍", n:"⠝", o:"⠕", p:"⠏", q:"⠟", r:"⠗", s:"⠎", t:"⠞", u:"⠥", v:"⠧", w:"⠺", x:"⠭", y:"⠽", z:"⠵" }
	mapUpper := { A:"⠠⠁", B:"⠠⠃", C:"⠠⠉", D:"⠠⠙", E:"⠠⠑", F:"⠠⠋", G:"⠠⠛", H:"⠠⠓", I:"⠠⠊", J:"⠠⠚", K:"⠠⠅", L:"⠠⠇", M:"⠠⠍", N:"⠠⠝", O:"⠠⠕", P:"⠠⠏", Q:"⠠⠟", R:"⠠⠗", S:"⠠⠎", T:"⠠⠞", U:"⠠⠥", V:"⠠⠧", W:"⠠⠺", X:"⠠⠭", Y:"⠠⠽", Z:"⠠⠵" }
	
	out := ""
	loop, parse, text
		if A_LoopField is upper
			out .= mapUpper.HasKey(A_LoopField) ? mapUpper[A_LoopField] : A_LoopField
		else
			out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk unmorse code
::unmorse::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, MVL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	; If they didn't type anything, take the text from the clipboard
	if StrLen(text) = 0
	{
		text := clipboard
		if StrLen(text) > 5000
		{
			return
		}
		backspace := 1
	}
	
	; Detects if user pasted text, uses that if so
	else if Asc(text) = 22
	{
		text := clipboard
		if StrLen(text) > 5000
		{
			return
		}
		backspace := StrLen(text) + 1
	}
	else
	{
		backspace := StrLen(text) + 1
	}
	
	map := { "":" "
			, "•−•−•−":".", "−−••−−":",", "••−−••":"?", "•−−−−•":"'", "−••−•":"/", "−•−−•":"(", "−•−−•−":")", "•−•••":"&", "−−−•••":":", "−•••−":"=", "•−•−•":"+", "−••••−":"-", "•−••−•":"""", "•−−•−•":"@", "•••−••−":"$", "••−−•−":"_", "−•−•−•":";", "−•−•−−":"!"
			, "•−":"A", "−•••":"B", "−•−•":"C", "−••":"D", "•":"E", "••−•":"F", "−−•":"G", "••••":"H", "••":"I", "•−−−":"J", "−•−":"K", "•−••":"L", "−−":"M", "−•":"N", "−−−":"O", "•−−•":"P", "−−•−":"Q", "•−•":"R", "•••":"S", "−":"T", "••−":"U", "•••−":"V", "•−−":"W", "−••−":"X", "−•−−":"Y", "−−••":"Z"
			, "•−−−−":"1", "••−−−":"2", "•••−−":"3", "••••−":"4", "•••••":"5", "−••••":"6", "−−•••":"7", "−−−••":"8", "−−−−•":"9", "−−−−−":"0"
			, ".-.-.-":".", "--..--":",", "..--..":"?", ".----.":"'", "-..-.":"/", "-.--.":"(", "-.--.-":")", ".-...":"&", "---...":":", "-...-":"=", ".-.-.":"+", "-....-":"-", ".-..-.":"""", ".--.-.":"@", "...-..-":"$", "..--.-":"_", "-.-.-.":";", "-.-.--":"!"
			, ".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", "..-.":"F", "--.":"G", "....":"H", "..":"I", ".---":"J", "-.-":"K", ".-..":"L", "--":"M", "-.":"N", "---":"O", ".--.":"P", "--.-":"Q", ".-.":"R", "...":"S", "-":"T", "..-":"U", "...-":"V", ".--":"W", "-..-":"X", "-.--":"Y", "--..":"Z"
			, ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0" }
	
	newText := text
	StringReplace, newText, newText, `r`n, %a_space%, All
	StringReplace, newText, newText,  , %a_space%, All
	StringReplace, newText, newText, %a_space%%a_space%%a_space%, %a_space%%a_space%, All
	out := ""
	loop, parse, newText, %a_space%
		out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " backspace "}{Raw}" out
return

; Bulk morse code
::morse::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { ".":"•−•−•− ", ",":"−−••−− ", "?":"••−−•• ", "'":"•−−−−• ", "/":"−••−• ", "(":"−•−−• ", ")":"−•−−•− ", "&":"•−••• ", ":":"−−−••• ", "=":"−•••− ", "+":"•−•−• ", "-":"−••••− ", """":"•−••−• ", "@":"•−−•−• ", "$":"•••−••− ", "_":"••−−•− ", ";":"−•−•−• ", "!":"−•−•−− ", " ":"  "
		, a:"•− ", b:"−••• ", c:"−•−• ", d:"−•• ", e:"• ", f:"••−• ", g:"−−• ", h:"•••• ", i:"•• ", j:"•−−− ", k:"−•− ", l:"•−•• ", m:"−− ", n:"−• ", o:"−−− ", p:"•−−• ", q:"−−•− ", r:"•−• ", s:"••• ", t:"− ", u:"••− ", v:"•••− ", w:"•−− ", x:"−••− ", y:"−•−− ", z:"−−•• "
		, 1:"•−−−− ", 2:"••−−− ", 3:"•••−− ", 4:"••••− ", 5:"••••• ", 6:"−•••• ", 7:"−−••• ", 8:"−−−•• ", 9:"−−−−• ", 0:"−−−−− " }
	
	out := ""
	loop, parse, text
		out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk morse code, periods and hyphens
::morse2::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { ".":".-.-.- ", ",":"--..-- ", "?":"..--.. ", "'":".----. ", "/":"-..-. ", "(":"-.--. ", ")":"-.--.- ", "&":".-... ", ":":"---... ", "=":"-...- ", "+":".-.-. ", "-":"-....- ", """":".-..-. ", "@":".--.-. ", "$":"...-..- ", "_":"..--.- ", ";":"-.-.-. ", "!":"-.-.-- ", " ":"  "
		, a:".- ", b:"-... ", c:"-.-. ", d:"-.. ", e:". ", f:"..-. ", g:"--. ", h:".... ", i:".. ", j:".--- ", k:"-.- ", l:".-.. ", m:"-- ", n:"-. ", o:"--- ", p:".--. ", q:"--.- ", r:".-. ", s:"... ", t:"- ", u:"..- ", v:"...- ", w:".-- ", x:"-..- ", y:"-.-- ", z:"--.. "
		, 1:".---- ", 2:"..--- ", 3:"...-- ", 4:"....- ", 5:"..... ", 6:"-.... ", 7:"--... ", 8:"---.. ", 9:"----. ", 0: o "----- " }
	
	out := ""
	loop, parse, text
		out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk unrune code (Elder Futhark)
::unrune::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, MVL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	; If they didn't type anything, take the text from the clipboard
	if StrLen(text) = 0
	{
		text := clipboard
		if StrLen(text) > 5000
		{
			return
		}
		backspace := 1
	}
	
	; Detects if user pasted text, uses that if so
	else if Asc(text) = 22
	{
		text := clipboard
		if StrLen(text) > 5000
		{
			return
		}
		backspace := StrLen(text) + 1
	}
	else
	{
		backspace := StrLen(text) + 1
	}
	
	map := { "ᚠ":"f", "ᚢ":"u", "ᛞ":"d", "ᛉ":"z", "ᛒ":"b", "ᛃ":"j", "ᚨ":"a", "ᚹ":"w", "ᚷ":"g", "æ":"ᛇ", "ᚱ":"r", "ᚲ":"k", "ᚺ":"h", "ᚾ":"n", "ᛁ":"i", "ᛖ":"e", "ᛊ":"s", "ᛏ":"t", "ᛈ":"p", "ᛗ":"m", "ᛚ":"l", "ᛟ":"o"}
	
	newText := text
	StringReplace, newText, newText, ᚦ, th, All
	StringReplace, newText, newText, ᛜ, ng, All
	out := ""
	loop, parse, newText
		out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " backspace "}{Raw}" out
return

; Bulk Elder Futhark
::rune::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { "f":"ᚠ", "u":"ᚢ", "a":"ᚨ", "r":"ᚱ", "k":"ᚲ", "g":"ᚷ", "w":"ᚹ", "h":"ᚺ", "n":"ᚾ", "i":"ᛁ", "j":"ᛃ", "æ":"ᛇ", "p":"ᛈ", "z":"ᛉ", "s":"ᛊ", "t":"ᛏ", "b":"ᛒ", "e":"ᛖ", "m":"ᛗ", "l":"ᛚ", "o":"ᛟ", "d":"ᛞ", "v":"ᚠ" }
	
	out := ""
	newText := text
	StringReplace, newText, newText, th, ᚦ, All
	StringReplace, newText, newText, ng, ᛜ, All 
	StringReplace, newText, newText, ae, ᛇ, All 
	loop, parse, newText
		out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send %  "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk unrune code (Younger Futhark)
::unrune2::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, MVL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	; If they didn't type anything, take the text from the clipboard
	if StrLen(text) = 0
	{
		text := clipboard
		if StrLen(text) > 5000
		{
			return
		}
		backspace := 1
	}
	
	; Detects if user pasted text, uses that if so
	else if Asc(text) = 22
	{
		text := clipboard
		if StrLen(text) > 5000
		{
			return
		}
		backspace := StrLen(text) + 1
	}
	else
	{
		backspace := StrLen(text) + 1
	}
	
	newText := text
	StringReplace, newText, newText, ᚦ, th, All
	StringReplace, newText, newText, ᛦ, r, All
	out := ""
	map := { "ᚠ":"f", "ᚢ":"o", "ᚬ":"æ", "ᚱ":"r", "ᚴ":"k", "ᚼ":"h", "ᚾ":"n", "ᛁ":"i", "ᛅ":"e", "ᛋ":"s", "ᛏ":"t", "ᛒ":"p", "ᛘ":"m", "ᛚ":"l"}
	loop, parse, newText
		out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " backspace "}{Raw}" out
return

; Bulk Younger Futhark
::rune2::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { "f":"ᚠ", "u":"ᚢ", "v":"ᚢ", "w":"ᚢ", "y":"ᚢ", "o":"ᚢ", "ø":"ᚢ", "æ":"ᚬ", "r":"ᚱ", "k":"ᚴ", "g":"ᚴ", "h":"ᚼ", "n":"ᚾ", "i":"ᛁ", "e":"ᛅ", "a":"ᛅ", "s":"ᛋ", "t":"ᛏ", "d":"ᛏ", "b":"ᛒ", "p":"ᛒ", "m":"ᛘ", "l":"ᛚ" }
	
	out := ""
	newText := text
	StringReplace, newText, newText, th, ᚦ, All
	StringReplace, newText, newText, rrr, ᛦ, All
	loop, parse, newText
		out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send %  "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk blackboard bold
::bb::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { 0:"𝟘", 1:"𝟙", 2:"𝟚", 3:"𝟛", 4:"𝟜", 5:"𝟝", 6:"𝟞", 7:"𝟟", 8:"𝟠", 9:"𝟡"
			, a:"𝕒", b:"𝕓", c:"𝕔", d:"𝕕", e:"𝕖", f:"𝕗", g:"𝕘", h:"𝕙", i:"𝕚", j:"𝕛", k:"𝕜", l:"𝕝", m:"𝕞", n:"𝕟", o:"𝕠", p:"𝕡", q:"𝕢", r:"𝕣", s:"𝕤", t:"𝕥", u:"𝕦", v:"𝕧", w:"𝕨", x:"𝕩", y:"𝕪", z:"𝕫" }
	mapUpper := { A:"𝔸", B:"𝔹", C:"ℂ", D:"𝔻", E:"𝔼", F:"𝔽", G:"𝔾", H:"ℍ", I:"𝕀", J:"𝕁", K:"𝕂", L:"𝕃", M:"𝕄", N:"ℕ", O:"𝕆", P:"ℙ", Q:"ℚ", R:"ℝ", S:"𝕊", T:"𝕋", U:"𝕌", V:"𝕍", W:"𝕎", X:"𝕏", Y:"𝕐", Z:"ℤ" }
	
	out := ""
	newText := text
	StringCaseSense, on
	StringReplace, newText, newText, Sigma, ⅀, All
	StringReplace, newText, newText, Gamma, ℾ, All
	StringReplace, newText, newText, gamma, ℽ, All
	StringReplace, newText, newText, Pi, ℿ, All
	StringReplace, newText, newText, pi, ℼ, All
	StringCaseSense, off
	loop, parse, newText
		if A_LoopField is upper
			out .= mapUpper.HasKey(A_LoopField) ? mapUpper[A_LoopField] : A_LoopField
		else
			out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk small caps
::smallcaps::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { "A":"ᴀ", "B":"ʙ", "C":"ᴄ", "D":"ᴅ", "E":"ᴇ", "F":"ғ", "G":"ɢ", "H":"ʜ", "I":"ɪ", "J":"ᴊ", "K":"ᴋ", "L":"ʟ", "M":"ᴍ", "N":"ɴ", "O":"ᴏ", "P":"ᴘ", "Q":"ǫ", "R":"ʀ", "S":"s", "T":"ᴛ", "U":"ᴜ", "V":"ᴠ", "W":"ᴡ", "X":"x", "Y":"ʏ", "Z":"ᴢ" }
	
	out := ""
	loop, parse, text
		out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk bold cursive
::boldcursive::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { "a":"𝓪", "b":"𝓫", "c":"𝓬", "d":"𝓭", "e":"𝓮", "f":"𝓯", "g":"𝓰", "h":"𝓱", "i":"𝓲", "j":"𝓳", "k":"𝓴", "l":"𝓵", "m":"𝓶", "n":"𝓷", "o":"𝓸", "p":"𝓹", "q":"𝓺", "r":"𝓻", "s":"𝓼", "t":"𝓽", "u":"𝓾", "v":"𝓿", "w":"𝔀", "x":"𝔁", "y":"𝔂", "z":"𝔃" }
	mapUpper := { "A":"𝓐", "B":"𝓑", "C":"𝓒", "D":"𝓓", "E":"𝓔", "F":"𝓕", "G":"𝓖", "H":"𝓗", "I":"𝓘", "J":"𝓙", "K":"𝓚", "L":"𝓛", "M":"𝓜", "N":"𝓝", "O":"𝓞", "P":"𝓟", "Q":"𝓠", "R":"𝓡", "S":"𝓢", "T":"𝓣", "U":"𝓤", "V":"𝓥", "W":"𝓦", "X":"𝓧", "Y":"𝓨", "Z":"𝓩" }
	
	out := ""
	loop, parse, text
		if A_LoopField is upper
			out .= mapUpper.HasKey(A_LoopField) ? mapUpper[A_LoopField] : A_LoopField
		else
			out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk cursive
::cursive::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { "a":"𝒶", "b":"𝒷", "c":"𝒸", "d":"𝒹", "e":"𝔢", "f":"𝒻", "g":"ℊ", "h":"𝒽", "i":"𝒾", "j":"𝒿", "k":"𝓀", "l":"𝓁", "m":"𝓂", "n":"𝓃", "o":"ℴ", "p":"𝓅", "q":"𝓆", "r":"𝓇", "s":"𝓈", "t":"𝓉", "u":"𝓊", "v":"𝓋", "w":"𝓌", "x":"𝓍", "y":"𝓎", "z":"𝓏" }
	mapUpper := { "A":"𝒜", "B":"ℬ", "C":"𝒞", "D":"𝒟", "E":"ℰ", "F":"ℱ", "G":"𝒢", "H":"ℋ", "I":"ℐ", "J":"𝒥", "K":"𝒦", "L":"ℒ", "M":"ℳ", "N":"𝒩", "O":"𝒪", "P":"𝒫", "Q":"𝒬", "R":"ℛ", "S":"𝒮", "T":"𝒯", "U":"𝒰", "V":"𝒱", "W":"𝒲", "X":"𝒳", "Y":"𝒴", "Z":"𝒵" }
	
	out := ""
	loop, parse, text
		if A_LoopField is upper
			out .= mapUpper.HasKey(A_LoopField) ? mapUpper[A_LoopField] : A_LoopField
		else
			out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk bolditalic
::bolditalic::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { "a":"𝙖", "b":"𝙗", "c":"𝙘", "d":"𝙙", "e":"𝙚", "f":"𝙛", "g":"𝙜", "h":"𝙝", "i":"𝙞", "j":"𝙟", "k":"𝙠", "l":"𝙡", "m":"𝙢", "n":"𝙣", "o":"𝙤", "p":"𝙥", "q":"𝙦", "r":"𝙧", "s":"𝙨", "t":"𝙩", "u":"𝙪", "v":"𝙫", "w":"𝙬", "x":"𝙭", "y":"𝙮", "z":"𝙯" }
	mapUpper := { "A":"𝑨", "B":"𝑩", "C":"𝑪", "D":"𝑫", "E":"𝑬", "F":"𝑭", "G":"𝑮", "H":"𝑯", "I":"𝑰", "J":"𝑱", "K":"𝑲", "L":"𝑳", "M":"𝑴", "N":"𝑵", "O":"𝑶", "P":"𝑷", "Q":"𝑸", "R":"𝑹", "S":"𝑺", "T":"𝑻", "U":"𝑼", "V":"𝑽", "W":"𝑾", "X":"𝑿", "Y":"𝒀", "Z":"𝒁" }
	
	out := ""
	loop, parse, text
		if A_LoopField is upper
			out .= mapUpper.HasKey(A_LoopField) ? mapUpper[A_LoopField] : A_LoopField
		else
			out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk bold
::bold::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { "a":"𝐚", "b":"𝐛", "c":"𝐜", "d":"𝐝", "e":"𝐞", "f":"𝐟", "g":"𝐠", "h":"𝐡", "i":"𝐢", "j":"𝐣", "k":"𝐤", "l":"𝐥", "m":"𝐦", "n":"𝐧", "o":"𝐨", "p":"𝐩", "q":"𝐪", "r":"𝐫", "s":"𝐬", "t":"𝐭", "u":"𝐮", "v":"𝐯", "w":"𝐰", "x":"𝐱", "y":"𝐲", "z":"𝐳" }
	mapUpper := { "A":"𝐀", "B":"𝐁", "C":"𝐂", "D":"𝐃", "E":"𝐄", "F":"𝐅", "G":"𝐆", "H":"𝐇", "I":"𝐈", "J":"𝐉", "K":"𝐊", "L":"𝐋", "M":"𝐌", "N":"𝐍", "O":"𝐎", "P":"𝐏", "Q":"𝐐", "R":"𝐑", "S":"𝐒", "T":"𝐓", "U":"𝐔", "V":"𝐕", "W":"𝐖", "X":"𝐗", "Y":"𝐘", "Z":"𝐙" }
	
	out := ""
	loop, parse, text
		if A_LoopField is upper
			out .= mapUpper.HasKey(A_LoopField) ? mapUpper[A_LoopField] : A_LoopField
		else
			out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk italic
::italic::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { "a":"𝘢", "b":"𝘣", "c":"𝘤", "d":"𝘥", "e":"𝘦", "f":"𝘧", "g":"𝘨", "h":"𝘩", "i":"𝘪", "j":"𝘫", "k":"𝘬", "l":"𝘭", "m":"𝘮", "n":"𝘯", "o":"𝘰", "p":"𝘱", "q":"𝘲", "r":"𝘳", "s":"𝘴", "t":"𝘵", "u":"𝘶", "v":"𝘷", "w":"𝘸", "x":"𝘹", "y":"𝘺", "z":"𝘻" }
	mapUpper := { "A":"𝐴", "B":"𝐵", "C":"𝐶", "D":"𝐷", "E":"𝐸", "F":"𝐹", "G":"𝐺", "H":"𝐻", "I":"𝐼", "J":"𝐽", "K":"𝐾", "L":"𝐿", "M":"𝑀", "N":"𝑁", "O":"𝑂", "P":"𝑃", "Q":"𝑄", "R":"𝑅", "S":"𝑆", "T":"𝑇", "U":"𝑈", "V":"𝑉", "W":"𝑊", "X":"𝑋", "Y":"𝑌", "Z":"𝑍" }
	
	out := ""
	loop, parse, text
		if A_LoopField is upper
			out .= mapUpper.HasKey(A_LoopField) ? mapUpper[A_LoopField] : A_LoopField
		else
			out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk underline
::underline::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}"
	loop, parse, text
		Send ͟%A_LoopField%
return

; Bulk lookalike letters
::lookalike::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, VL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	map := { "a":"а", "b":"ᖯ", "c":"с", "d":"𝖽", "e":"е", "f":"𝖿", "g":"𝗀", "h":"һ", "i":"і", "j":"ј", "k":"𝗄", "l":"ӏ", "m":"ｍ", "n":"𝗇", "o":"о", "p":"р", "q":"𝗊", "r":"𝗋", "s":"ѕ", "t":"𝗍", "u":"𝗎", "v":"ν", "w":"𝗐", "x":"х", "y":"у", "z":"ꮓ", ":":"։", ";":";", "<":"˂", ">":"˃", "=":"᐀", "@":"＠", "!":"ǃ", "$":"＄", "%":"％", "&":"＆", "(":"❨", ")":"❩", "*":"*", "+":"᛭", "-":"˗" }
	mapUpper := { "A":"Α", "B":"Β", "C":"С", "D":"Ꭰ", "E":"Ε", "F":"ꓝ", "G":"Ꮐ", "H":"Η", "I":"l", "J":"Ј", "K":"Κ", "L":"ᒪ", "M":"Μ", "N":"Ν", "O":"Ο", "P":"Ρ", "Q":"ⵕ", "R":"ꓣ", "S":"Ѕ", "T":"Τ", "U":"ꓴ", "V":"Ꮩ", "W":"Ꮃ", "X":"Χ", "Y":"Υ", "Z":"Ζ" }
	
	out := ""
	loop, parse, text
		if A_LoopField is upper
			out .= mapUpper.HasKey(A_LoopField) ? mapUpper[A_LoopField] : A_LoopField
		else
			out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " StrLen(text) + 1 "}{Raw}" out
return

; Bulk rot13 code
::rot13::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, MVL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	; If they didn't type anything, take the text from the clipboard
	if StrLen(text) = 0
	{
		text := clipboard
		if StrLen(text) > 5000
		{
			return
		}
		backspace := 1
	}
	
	; Detects if user pasted text, uses that if so
	else if Asc(text) = 22
	{
		text := clipboard
		if StrLen(text) > 5000
		{
			return
		}
		backspace := StrLen(text) + 1
	}
	else
	{
		backspace := StrLen(text) + 1
	}
	
	map := {"a":"n", "b":"o", "c":"p", "d":"q", "e":"r", "f":"s", "g":"t", "h":"u", "i":"v", "j":"w", "k":"x", "l":"y", "m":"z", "n":"a", "o":"b", "p":"c", "q":"d", "r":"e", "s":"f", "t":"g", "u":"h", "v":"i", "w":"j", "x":"k", "y":"l", "z":"m"}
	mapUpper := {"A":"N", "B":"O", "C":"P", "D":"Q", "E":"R", "F":"S", "G":"T", "H":"U", "I":"V", "J":"W", "K":"X", "L":"Y", "M":"Z", "N":"A", "O":"B", "P":"C", "Q":"D", "R":"E", "S":"F", "T":"G", "U":"H", "V":"I", "W":"J", "X":"K", "Y":"L", "Z":"M"}
	
	out := ""
	loop, parse, text
		if A_LoopField is upper
			out .= mapUpper.HasKey(A_LoopField) ? mapUpper[A_LoopField] : A_LoopField
		else
			out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
	
	; Backspaces typed text, outputs new text
	Send % "{Backspace " backspace "}{Raw}" out
return

; Bulk alternating caps
::mock::
	; Because ahk is weird, breaks suspend otherwise
	Sleep -1
	
	; Collects all input until %endchar%, stores it in the variable 'text'. Give up after L characters or T seconds
	Suspend
	input, text, MVL1000T90, %endchar%
	Suspend
	
	; Just give up if they took too long or typed too much
	if ErrorLevel in Max,Timeout
		return
	
	; If they didn't type anything, take the text from the clipboard
	if StrLen(text) = 0
	{
		text := clipboard
		if StrLen(text) > 5000
		{
			return
		}
		backspace := 1
	}
	
	; Detects if user pasted text, uses that if so
	else if Asc(text) = 22
	{
		text := clipboard
		if StrLen(text) > 5000
		{
			return
		}
		backspace := StrLen(text) + 1
	}
	else
	{
		backspace := StrLen(text) + 1
	}
	
	map := {"a":"a", "b":"b", "c":"c", "d":"d", "e":"e", "f":"f", "g":"g", "h":"h", "i":"i", "j":"j", "k":"k", "l":"l", "m":"m", "n":"n", "o":"o", "p":"p", "q":"q", "r":"r", "s":"s", "t":"t", "u":"u", "v":"v", "w":"w", "x":"x", "y":"y", "z":"z"}
	mapUpper := {"a":"A", "b":"B", "c":"C", "d":"D", "e":"E", "f":"F", "g":"G", "h":"H", "i":"I", "j":"J", "k":"K", "l":"L", "m":"M", "n":"N", "o":"O", "p":"P", "q":"Q", "r":"R", "s":"S", "t":"T", "u":"U", "v":"V", "w":"W", "x":"X", "y":"Y", "z":"Z"}

	
	out := ""
	loop, parse, text
	{
		Random, lowercase, 0, 1
		if lowercase < 0.5
			out .= map.HasKey(A_LoopField) ? map[A_LoopField] : A_LoopField
		else
			out .= mapUpper.HasKey(A_LoopField) ? mapUpper[A_LoopField] : A_LoopField
	}
	; Backspaces typed text, outputs new text
	Send % "{Backspace " backspace "}{Raw}" out
return