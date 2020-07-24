# Language codes, as defined by ISO 639-1
Scrapes the list of (ISO 639-1) language codes from [wikipedia](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) and saves them to a CSV file.

## Usage
* Install
    ```bash
    git clone git@github.com:mohaseeb/iso_language_codes.git
    cd iso_language_codes
    # create a virtual env (recommended)
    pip install -r requirements.txt
    ```
* Run
    ```bash
    python main.py
    ```

## Scraped language codes
Below is the language codes table (column names and content) printed as valid python (have fun!)
```python
header = ["Language family", "ISO language name", "Native name (endonym)", "639-1", "639-2/T", "639-2/B", "639-3", "Notes"]
body = [
        ["Northwest Caucasian", "Abkhazian", "аҧсуа бызшәа, аҧсшәа", "ab", "abk", "abk", "abk", "also known as Abkhaz"],
        ["Afro-Asiatic", "Afar", "Afaraf", "aa", "aar", "aar", "aar", ""],
        ["Indo-European", "Afrikaans", "Afrikaans", "af", "afr", "afr", "afr", ""],
        ["Niger–Congo", "Akan", "Akan", "ak", "aka", "aka", "aka + 2", "macrolanguage, Twi is [tw/twi], Fanti is [fat]"],
        ["Indo-European", "Albanian", "Shqip", "sq", "sqi", "alb", "sqi + 4", "macrolanguage, "Albanian Phylozone" in 639-6"],
        ["Afro-Asiatic", "Amharic", "አማርኛ", "am", "amh", "amh", "amh", ""],
        ["Afro-Asiatic", "Arabic", "العربية", "ar", "ara", "ara", "ara + 29", "macrolanguage, Standard Arabic is [arb]"],
        ["Indo-European", "Aragonese", "aragonés", "an", "arg", "arg", "arg", ""],
        ["Indo-European", "Armenian", "Հայերեն", "hy", "hye", "arm", "hye", "also known as Հայերէն; ISO 639-3 code "hye" is for Eastern Armenian, "hyw" is for Western Armenian, and "xcl" is for Classical Armenian"],
        ["Indo-European", "Assamese", "অসমীয়া", "as", "asm", "asm", "asm", ""],
        ["Northeast Caucasian", "Avaric", "авар мацӀ, магӀарул мацӀ", "av", "ava", "ava", "ava", "also known as Avar"],
        ["Indo-European", "Avestan", "avesta", "ae", "ave", "ave", "ave", "ancient"],
        ["Aymaran", "Aymara", "aymar aru", "ay", "aym", "aym", "aym + 2", "macrolanguage"],
        ["Turkic", "Azerbaijani", "azərbaycan dili", "az", "aze", "aze", "aze + 2", "macrolanguage"],
        ["Niger–Congo", "Bambara", "bamanankan", "bm", "bam", "bam", "bam", ""],
        ["Turkic", "Bashkir", "башҡорт теле", "ba", "bak", "bak", "bak", ""],
        ["Language isolate", "Basque", "euskara, euskera", "eu", "eus", "baq", "eus", ""],
        ["Indo-European", "Belarusian", "беларуская мова", "be", "bel", "bel", "bel", ""],
        ["Indo-European", "Bengali", "বাংলা", "bn", "ben", "ben", "ben", "also known as Bangla"],
        ["Indo-European", "Bihari languages", "भोजपुरी", "bh", "bih", "bih", "", "collective language code for Bhojpuri, Magahi, and Maithili"],
        ["Creole", "Bislama", "Bislama", "bi", "bis", "bis", "bis", "Language formed from English and Ni-Vanuatu, with some French influence."],
        ["Indo-European", "Bosnian", "bosanski jezik", "bs", "bos", "bos", "bos", ""],
        ["Indo-European", "Breton", "brezhoneg", "br", "bre", "bre", "bre", ""],
        ["Indo-European", "Bulgarian", "български език", "bg", "bul", "bul", "bul", ""],
        ["Sino-Tibetan", "Burmese", "ဗမာစာ", "my", "mya", "bur", "mya", "also known as Myanmar"],
        ["Indo-European", "Catalan, Valencian", "català, valencià", "ca", "cat", "cat", "cat", ""],
        ["Austronesian", "Chamorro", "Chamoru", "ch", "cha", "cha", "cha", ""],
        ["Northeast Caucasian", "Chechen", "нохчийн мотт", "ce", "che", "che", "che", ""],
        ["Niger–Congo", "Chichewa, Chewa, Nyanja", "chiCheŵa, chinyanja", "ny", "nya", "nya", "nya", ""],
        ["Sino-Tibetan", "Chinese", "中文 (Zhōngwén), 汉语, 漢語", "zh", "zho", "chi", "zho + 16", "macrolanguage"],
        ["Turkic", "Chuvash", "чӑваш чӗлхи", "cv", "chv", "chv", "chv", ""],
        ["Indo-European", "Cornish", "Kernewek", "kw", "cor", "cor", "cor", ""],
        ["Indo-European", "Corsican", "corsu, lingua corsa", "co", "cos", "cos", "cos", ""],
        ["Algonquian", "Cree", "ᓀᐦᐃᔭᐍᐏᐣ", "cr", "cre", "cre", "cre + 6", "macrolanguage"],
        ["Indo-European", "Croatian", "hrvatski jezik", "hr", "hrv", "hrv", "hrv", ""],
        ["Indo-European", "Czech", "čeština, český jazyk", "cs", "ces", "cze", "ces", ""],
        ["Indo-European", "Danish", "dansk", "da", "dan", "dan", "dan", ""],
        ["Indo-European", "Divehi, Dhivehi, Maldivian", "ދިވެހި", "dv", "div", "div", "div", ""],
        ["Indo-European", "Dutch, Flemish", "Nederlands, Vlaams", "nl", "nld", "dut", "nld", "Flemish is not to be confused with the closely related West Flemish which is referred to as Vlaams (Dutch for "Flemish") in ISO 639-3 and has the ISO 639-3 code vls"],
        ["Sino-Tibetan", "Dzongkha", "རྫོང་ཁ", "dz", "dzo", "dzo", "dzo", ""],
        ["Indo-European", "English", "English", "en", "eng", "eng", "eng", ""],
        ["Constructed", "Esperanto", "Esperanto", "eo", "epo", "epo", "epo", "constructed, initiated from L.L. Zamenhof, 1887"],
        ["Uralic", "Estonian", "eesti, eesti keel", "et", "est", "est", "est + 2", "macrolanguage"],
        ["Niger–Congo", "Ewe", "Eʋegbe", "ee", "ewe", "ewe", "ewe", ""],
        ["Indo-European", "Faroese", "føroyskt", "fo", "fao", "fao", "fao", ""],
        ["Austronesian", "Fijian", "vosa Vakaviti", "fj", "fij", "fij", "fij", ""],
        ["Uralic", "Finnish", "suomi, suomen kieli", "fi", "fin", "fin", "fin", ""],
        ["Indo-European", "French", "français, langue française", "fr", "fra", "fre", "fra", ""],
        ["Niger–Congo", "Fulah", "Fulfulde, Pulaar, Pular", "ff", "ful", "ful", "ful + 9", "macrolanguage, also known as Fula"],
        ["Indo-European", "Galician", "Galego", "gl", "glg", "glg", "glg", ""],
        ["Kartvelian", "Georgian", "ქართული", "ka", "kat", "geo", "kat", ""],
        ["Indo-European", "German", "Deutsch", "de", "deu", "ger", "deu", ""],
        ["Indo-European", "Greek, Modern (1453–)", "ελληνικά", "el", "ell", "gre", "ell", ""],
        ["Tupian", "Guarani", "Avañe'ẽ", "gn", "grn", "grn", "grn + 5", "macrolanguage"],
        ["Indo-European", "Gujarati", "ગુજરાતી", "gu", "guj", "guj", "guj", ""],
        ["Creole", "Haitian, Haitian Creole", "Kreyòl ayisyen", "ht", "hat", "hat", "hat", ""],
        ["Afro-Asiatic", "Hausa", "(Hausa) هَوُسَ", "ha", "hau", "hau", "hau", ""],
        ["Afro-Asiatic", "Hebrew", "עברית", "he", "heb", "heb", "heb", "Modern Hebrew.  Code changed in 1989 from original ISO 639:1988, iw.[1]"],
        ["Niger–Congo", "Herero", "Otjiherero", "hz", "her", "her", "her", ""],
        ["Indo-European", "Hindi", "हिन्दी, हिंदी", "hi", "hin", "hin", "hin", ""],
        ["Austronesian", "Hiri Motu", "Hiri Motu", "ho", "hmo", "hmo", "hmo", ""],
        ["Uralic", "Hungarian", "magyar", "hu", "hun", "hun", "hun", ""],
        ["Constructed", "Interlingua (International Auxiliary Language Association)", "Interlingua", "ia", "ina", "ina", "ina", "constructed by International Auxiliary Language Association"],
        ["Austronesian", "Indonesian", "Bahasa Indonesia", "id", "ind", "ind", "ind", "Covered by macrolanguage [ms/msa]. Changed in 1989 from original ISO 639:1988, in[1]."],
        ["Constructed", "Interlingue, Occidental", "(originally:) Occidental, (after WWII:) Interlingue", "ie", "ile", "ile", "ile", "constructed by Edgar de Wahl, first published in 1922"],
        ["Indo-European", "Irish", "Gaeilge", "ga", "gle", "gle", "gle", ""],
        ["Niger–Congo", "Igbo", "Asụsụ Igbo", "ig", "ibo", "ibo", "ibo", ""],
        ["Eskimo–Aleut", "Inupiaq", "Iñupiaq, Iñupiatun", "ik", "ipk", "ipk", "ipk + 2", "macrolanguage"],
        ["Constructed", "Ido", "Ido", "io", "ido", "ido", "ido", "constructed by De Beaufront, 1907, as variation of Esperanto"],
        ["Indo-European", "Icelandic", "Íslenska", "is", "isl", "ice", "isl", ""],
        ["Indo-European", "Italian", "Italiano", "it", "ita", "ita", "ita", ""],
        ["Eskimo–Aleut", "Inuktitut", "ᐃᓄᒃᑎᑐᑦ", "iu", "iku", "iku", "iku + 2", "macrolanguage"],
        ["Japonic", "Japanese", "日本語 (にほんご)", "ja", "jpn", "jpn", "jpn", ""],
        ["Austronesian", "Javanese", "ꦧꦱꦗꦮ, Basa Jawa", "jv", "jav", "jav", "jav", ""],
        ["Eskimo–Aleut", "Kalaallisut, Greenlandic", "kalaallisut, kalaallit oqaasii", "kl", "kal", "kal", "kal", ""],
        ["Dravidian", "Kannada", "ಕನ್ನಡ", "kn", "kan", "kan", "kan", ""],
        ["Nilo-Saharan", "Kanuri", "Kanuri", "kr", "kau", "kau", "kau + 3", "macrolanguage"],
        ["Indo-European", "Kashmiri", "कश्मीरी, كشميري‎", "ks", "kas", "kas", "kas", ""],
        ["Turkic", "Kazakh", "қазақ тілі", "kk", "kaz", "kaz", "kaz", ""],
        ["Austroasiatic", "Central Khmer", "ខ្មែរ, ខេមរភាសា, ភាសាខ្មែរ", "km", "khm", "khm", "khm", "also known as Khmer or Cambodian"],
        ["Niger–Congo", "Kikuyu, Gikuyu", "Gĩkũyũ", "ki", "kik", "kik", "kik", ""],
        ["Niger–Congo", "Kinyarwanda", "Ikinyarwanda", "rw", "kin", "kin", "kin", ""],
        ["Turkic", "Kirghiz, Kyrgyz", "Кыргызча, Кыргыз тили", "ky", "kir", "kir", "kir", ""],
        ["Uralic", "Komi", "коми кыв", "kv", "kom", "kom", "kom + 2", "macrolanguage"],
        ["Niger–Congo", "Kongo", "Kikongo", "kg", "kon", "kon", "kon + 3", "macrolanguage"],
        ["Koreanic", "Korean", "한국어", "ko", "kor", "kor", "kor", ""],
        ["Indo-European", "Kurdish", "Kurdî, کوردی‎", "ku", "kur", "kur", "kur + 3", "macrolanguage"],
        ["Niger–Congo", "Kuanyama, Kwanyama", "Kuanyama", "kj", "kua", "kua", "kua", ""],
        ["Indo-European", "Latin", "latine, lingua latina", "la", "lat", "lat", "lat", "ancient"],
        ["Indo-European", "Luxembourgish, Letzeburgesch", "Lëtzebuergesch", "lb", "ltz", "ltz", "ltz", ""],
        ["Niger–Congo", "Ganda", "Luganda", "lg", "lug", "lug", "lug", ""],
        ["Indo-European", "Limburgan, Limburger, Limburgish", "Limburgs", "li", "lim", "lim", "lim", ""],
        ["Niger–Congo", "Lingala", "Lingála", "ln", "lin", "lin", "lin", ""],
        ["Tai–Kadai", "Lao", "ພາສາລາວ", "lo", "lao", "lao", "lao", ""],
        ["Indo-European", "Lithuanian", "lietuvių kalba", "lt", "lit", "lit", "lit", ""],
        ["Niger–Congo", "Luba-Katanga", "Kiluba", "lu", "lub", "lub", "lub", "also known as Luba-Shaba"],
        ["Indo-European", "Latvian", "latviešu valoda", "lv", "lav", "lav", "lav + 2", "macrolanguage"],
        ["Indo-European", "Manx", "Gaelg, Gailck", "gv", "glv", "glv", "glv", ""],
        ["Indo-European", "Macedonian", "македонски јазик", "mk", "mkd", "mac", "mkd", ""],
        ["Austronesian", "Malagasy", "fiteny malagasy", "mg", "mlg", "mlg", "mlg + 11", "macrolanguage"],
        ["Austronesian", "Malay", "Bahasa Melayu, بهاس ملايو‎", "ms", "msa", "may", "msa + 36", "macrolanguage, Standard Malay is [zsm], Indonesian is [id/ind]"],
        ["Dravidian", "Malayalam", "മലയാളം", "ml", "mal", "mal", "mal", ""],
        ["Afro-Asiatic", "Maltese", "Malti", "mt", "mlt", "mlt", "mlt", ""],
        ["Austronesian", "Maori", "te reo Māori", "mi", "mri", "mao", "mri", "also known as Māori"],
        ["Indo-European", "Marathi", "मराठी", "mr", "mar", "mar", "mar", "also known as Marāṭhī"],
        ["Austronesian", "Marshallese", "Kajin M̧ajeļ", "mh", "mah", "mah", "mah", ""],
        ["Mongolic", "Mongolian", "Монгол хэл", "mn", "mon", "mon", "mon + 2", "macrolanguage"],
        ["Austronesian", "Nauru", "Dorerin Naoero", "na", "nau", "nau", "nau", "also known as Nauruan"],
        ["Dené–Yeniseian", "Navajo, Navaho", "Diné bizaad", "nv", "nav", "nav", "nav", ""],
        ["Niger–Congo", "North Ndebele", "isiNdebele", "nd", "nde", "nde", "nde", "also known as Northern Ndebele"],
        ["Indo-European", "Nepali", "नेपाली", "ne", "nep", "nep", "nep + 2", "macrolanguage"],
        ["Niger–Congo", "Ndonga", "Owambo", "ng", "ndo", "ndo", "ndo", ""],
        ["Indo-European", "Norwegian Bokmål", "Norsk Bokmål", "nb", "nob", "nob", "nob", "Covered by macrolanguage [no/nor]"],
        ["Indo-European", "Norwegian Nynorsk", "Norsk Nynorsk", "nn", "nno", "nno", "nno", "Covered by macrolanguage [no/nor]"],
        ["Indo-European", "Norwegian", "Norsk", "no", "nor", "nor", "nor + 2", "macrolanguage, Bokmål is [nb/nob], Nynorsk is [nn/nno]"],
        ["Sino-Tibetan", "Sichuan Yi, Nuosu", "ꆈꌠ꒿ Nuosuhxop", "ii", "iii", "iii", "iii", "Standard form of Yi languages"],
        ["Niger–Congo", "South Ndebele", "isiNdebele", "nr", "nbl", "nbl", "nbl", "also known as Southern Ndebele"],
        ["Indo-European", "Occitan", "occitan, lenga d'òc", "oc", "oci", "oci", "oci", ""],
        ["Algonquian", "Ojibwa", "ᐊᓂᔑᓈᐯᒧᐎᓐ", "oj", "oji", "oji", "oji + 7", "macrolanguage, also known as Ojibwe"],
        ["Indo-European", "Church Slavic, Old Slavonic, Church Slavonic, Old Bulgarian, Old Church Slavonic", "ѩзыкъ словѣньскъ", "cu", "chu", "chu", "chu", "ancient, in use by Orthodox Church"],
        ["Afro-Asiatic", "Oromo", "Afaan Oromoo", "om", "orm", "orm", "orm + 4", "macrolanguage"],
        ["Indo-European", "Oriya", "ଓଡ଼ିଆ", "or", "ori", "ori", "ori + 2", "macrolanguage, also known as Odia"],
        ["Indo-European", "Ossetian, Ossetic", "ирон æвзаг", "os", "oss", "oss", "oss", ""],
        ["Indo-European", "Punjabi, Panjabi", "ਪੰਜਾਬੀ, پنجابی‎", "pa", "pan", "pan", "pan", ""],
        ["Indo-European", "Pali", "पालि, पाळि", "pi", "pli", "pli", "pli", "ancient, also known as Pāli"],
        ["Indo-European", "Persian", "فارسی", "fa", "fas", "per", "fas + 2", "macrolanguage, also known as Farsi"],
        ["Indo-European", "Polish", "język polski, polszczyzna", "pl", "pol", "pol", "pol", ""],
        ["Indo-European", "Pashto, Pushto", "پښتو", "ps", "pus", "pus", "pus + 3", "macrolanguage"],
        ["Indo-European", "Portuguese", "Português", "pt", "por", "por", "por", ""],
        ["Quechuan", "Quechua", "Runa Simi, Kichwa", "qu", "que", "que", "que + 43", "macrolanguage"],
        ["Indo-European", "Romansh", "Rumantsch Grischun", "rm", "roh", "roh", "roh", ""],
        ["Niger–Congo", "Rundi", "Ikirundi", "rn", "run", "run", "run", "also known as Kirundi"],
        ["Indo-European", "Romanian, Moldavian, Moldovan", "Română", "ro", "ron", "rum", "ron", "The identifiers mo and mol are deprecated, leaving ro and ron (639-2/T) and rum (639-2/B) the current language identifiers to be used for the variant of the Romanian language also known as Moldavian and Moldovan in English and moldave in French. The identifiers mo and mol will not be assigned to different items, and recordings using these identifiers will not be invalid."],
        ["Indo-European", "Russian", "русский", "ru", "rus", "rus", "rus", ""],
        ["Indo-European", "Sanskrit", "संस्कृतम्", "sa", "san", "san", "san", "ancient, still spoken, also known as Saṃskṛta"],
        ["Indo-European", "Sardinian", "sardu", "sc", "srd", "srd", "srd + 4", "macrolanguage"],
        ["Indo-European", "Sindhi", "सिन्धी, سنڌي، سندھی‎", "sd", "snd", "snd", "snd", ""],
        ["Uralic", "Northern Sami", "Davvisámegiella", "se", "sme", "sme", "sme", ""],
        ["Austronesian", "Samoan", "gagana fa'a Samoa", "sm", "smo", "smo", "smo", ""],
        ["Creole", "Sango", "yângâ tî sängö", "sg", "sag", "sag", "sag", ""],
        ["Indo-European", "Serbian", "српски језик", "sr", "srp", "srp", "srp", "The ISO 639-2/T code srp deprecated the ISO 639-2/B code scc[2]"],
        ["Indo-European", "Gaelic, Scottish Gaelic", "Gàidhlig", "gd", "gla", "gla", "gla", ""],
        ["Niger–Congo", "Shona", "chiShona", "sn", "sna", "sna", "sna", ""],
        ["Indo-European", "Sinhala, Sinhalese", "සිංහල", "si", "sin", "sin", "sin", ""],
        ["Indo-European", "Slovak", "Slovenčina, Slovenský Jazyk", "sk", "slk", "slo", "slk", ""],
        ["Indo-European", "Slovenian", "Slovenski Jezik, Slovenščina", "sl", "slv", "slv", "slv", "also known as Slovene"],
        ["Afro-Asiatic", "Somali", "Soomaaliga, af Soomaali", "so", "som", "som", "som", ""],
        ["Niger–Congo", "Southern Sotho", "Sesotho", "st", "sot", "sot", "sot", ""],
        ["Indo-European", "Spanish, Castilian", "Español", "es", "spa", "spa", "spa", ""],
        ["Austronesian", "Sundanese", "Basa Sunda", "su", "sun", "sun", "sun", ""],
        ["Niger–Congo", "Swahili", "Kiswahili", "sw", "swa", "swa", "swa + 2", "macrolanguage"],
        ["Niger–Congo", "Swati", "SiSwati", "ss", "ssw", "ssw", "ssw", "also known as Swazi"],
        ["Indo-European", "Swedish", "Svenska", "sv", "swe", "swe", "swe", ""],
        ["Dravidian", "Tamil", "தமிழ்", "ta", "tam", "tam", "tam", ""],
        ["Dravidian", "Telugu", "తెలుగు", "te", "tel", "tel", "tel", ""],
        ["Indo-European", "Tajik", "тоҷикӣ, toçikī, تاجیکی‎", "tg", "tgk", "tgk", "tgk", ""],
        ["Tai–Kadai", "Thai", "ไทย", "th", "tha", "tha", "tha", ""],
        ["Afro-Asiatic", "Tigrinya", "ትግርኛ", "ti", "tir", "tir", "tir", ""],
        ["Sino-Tibetan", "Tibetan", "བོད་ཡིག", "bo", "bod", "tib", "bod", "also known as Standard Tibetan"],
        ["Turkic", "Turkmen", "Türkmen, Түркмен", "tk", "tuk", "tuk", "tuk", ""],
        ["Austronesian", "Tagalog", "Wikang Tagalog", "tl", "tgl", "tgl", "tgl", "Note: Filipino (Pilipino) has the code [fil]"],
        ["Niger–Congo", "Tswana", "Setswana", "tn", "tsn", "tsn", "tsn", ""],
        ["Austronesian", "Tonga (Tonga Islands)", "Faka Tonga", "to", "ton", "ton", "ton", "also known as Tongan"],
        ["Turkic", "Turkish", "Türkçe", "tr", "tur", "tur", "tur", ""],
        ["Niger–Congo", "Tsonga", "Xitsonga", "ts", "tso", "tso", "tso", ""],
        ["Turkic", "Tatar", "татар теле, tatar tele", "tt", "tat", "tat", "tat", ""],
        ["Niger–Congo", "Twi", "Twi", "tw", "twi", "twi", "twi", "Covered by macrolanguage [ak/aka]"],
        ["Austronesian", "Tahitian", "Reo Tahiti", "ty", "tah", "tah", "tah", "One of the Reo Mā`ohi (languages of French Polynesia)"],
        ["Turkic", "Uighur, Uyghur", "ئۇيغۇرچە‎, Uyghurche", "ug", "uig", "uig", "uig", ""],
        ["Indo-European", "Ukrainian", "Українська", "uk", "ukr", "ukr", "ukr", ""],
        ["Indo-European", "Urdu", "اردو", "ur", "urd", "urd", "urd", ""],
        ["Turkic", "Uzbek", "Oʻzbek, Ўзбек, أۇزبېك‎", "uz", "uzb", "uzb", "uzb + 2", "macrolanguage"],
        ["Niger–Congo", "Venda", "Tshivenḓa", "ve", "ven", "ven", "ven", ""],
        ["Austroasiatic", "Vietnamese", "Tiếng Việt", "vi", "vie", "vie", "vie", ""],
        ["Constructed", "Volapük", "Volapük", "vo", "vol", "vol", "vol", "constructed"],
        ["Indo-European", "Walloon", "Walon", "wa", "wln", "wln", "wln", ""],
        ["Indo-European", "Welsh", "Cymraeg", "cy", "cym", "wel", "cym", ""],
        ["Niger–Congo", "Wolof", "Wollof", "wo", "wol", "wol", "wol", ""],
        ["Indo-European", "Western Frisian", "Frysk", "fy", "fry", "fry", "fry", "also known as Frisian"],
        ["Niger–Congo", "Xhosa", "isiXhosa", "xh", "xho", "xho", "xho", ""],
        ["Indo-European", "Yiddish", "ייִדיש", "yi", "yid", "yid", "yid + 2", "macrolanguage. Changed in 1989 from original ISO 639:1988, ji.[1]"],
        ["Niger–Congo", "Yoruba", "Yorùbá", "yo", "yor", "yor", "yor", ""],
        ["Tai–Kadai", "Zhuang, Chuang", "Saɯ cueŋƅ, Saw cuengh", "za", "zha", "zha", "zha + 16", "macrolanguage"],
        ["Niger–Congo", "Zulu", "isiZulu", "zu", "zul", "zul", "zul", ""]
]
```   