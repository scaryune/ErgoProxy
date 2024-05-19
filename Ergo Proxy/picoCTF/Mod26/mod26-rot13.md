
https://en.wikipedia.org/wiki/ROT13
https://stackoverflow.com/questions/3269686/short-rot13-function-python

ROT13

![[330px-ROT13_table_with_example.svg.png]]


**ROT13** ("**rotate by 13 places**", sometimes hyphenated **ROT-13**) is a simple letter [substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher "Substitution cipher") that replaces a letter with the 13th letter after it in the [latin alphabet](https://en.wikipedia.org/wiki/Latin_alphabet "Latin alphabet"). ROT13 is a special case of the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher "Caesar cipher") which was developed in ancient Rome.

Because there are 26 letters (2×13) in the [basic Latin alphabet](https://en.wikipedia.org/wiki/ISO_basic_Latin_alphabet "ISO basic Latin alphabet"), ROT13 is its own [inverse](https://en.wikipedia.org/wiki/Inverse_function "Inverse function"); that is, to undo ROT13, the same [algorithm](https://en.wikipedia.org/wiki/Algorithm "Algorithm") is applied, so the same action can be used for encoding and decoding. The algorithm provides virtually no [cryptographic](https://en.wikipedia.org/wiki/Cryptography "Cryptography") security, and is often cited as a canonical example of [weak encryption](https://en.wikipedia.org/wiki/Weak_encryption "Weak encryption").[[1]](https://en.wikipedia.org/wiki/ROT13#cite_note-modern-cryptanalysis-1)

ROT13 is used in [online forums](https://en.wikipedia.org/wiki/Online_forum "Online forum") as a means of hiding [spoilers](https://en.wikipedia.org/wiki/Spoiler_(media) "Spoiler (media)"), [punchlines](https://en.wikipedia.org/wiki/Punch_line "Punch line"), puzzle solutions, and [offensive materials](https://en.wikipedia.org/wiki/Profanity "Profanity") from the casual glance. ROT13 has inspired a variety of letter and word games online, and is frequently mentioned in [newsgroup](https://en.wikipedia.org/wiki/Newsgroup "Newsgroup") conversations.


## Description


Applying ROT13 to a piece of text merely requires examining its alphabetic characters and replacing each one by the letter 13 places further along in the [alphabet](https://en.wikipedia.org/wiki/Alphabet "Alphabet"), wrapping back to the beginning if necessary.[[2]](https://en.wikipedia.org/wiki/ROT13#cite_note-schneier-2) A becomes N, B becomes O, and so on up to M, which becomes Z, then the sequence continues at the beginning of the alphabet: N becomes A, O becomes B, and so on to Z, which becomes M. Only those letters which occur in the [English alphabet](https://en.wikipedia.org/wiki/English_alphabet "English alphabet") are affected; numbers, symbols, punctuation, whitespace, and all other characters are left unchanged. Because there are 26 letters in the English alphabet and 26 = 2 × 13, the ROT13 function is its own [inverse](https://en.wikipedia.org/wiki/Inverse_function "Inverse function"):[[2]](https://en.wikipedia.org/wiki/ROT13#cite_note-schneier-2)

ROT 13 ( ROT 13 ( x ) ) = x ![{\mbox{ROT}}_{13}({\mbox{ROT}}_{13}(x))=x](https://wikimedia.org/api/rest_v1/media/math/render/svg/7e658b9deef6d454a5bd70206f0c1029b682e3ae) for any basic Latin-alphabet text _x_.

In other words, two successive applications of ROT13 restore the original text (in [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), this is sometimes called an _[involution](https://en.wikipedia.org/wiki/Involution_(mathematics) "Involution (mathematics)")_; in cryptography, a _[reciprocal cipher](https://en.wikipedia.org/wiki/Reciprocal_cipher "Reciprocal cipher")_).

The transformation can be done using a [lookup table](https://en.wikipedia.org/wiki/Lookup_table "Lookup table"), such as the following:

|   |   |
|---|---|
|Input|ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz|
|Output|NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm|

For example, in the following joke, the punchline has been obscured by ROT13:

Why did the chicken cross the road?

Gb trg gb gur bgure fvqr!

Transforming the entire text via ROT13 form, the answer to the joke is revealed:

Jul qvq gur puvpxra pebff gur ebnq?

To get to the other side!

A second application of ROT13 would restore the original.

## Usage

ROT13 is a special case of the [encryption algorithm](https://en.wikipedia.org/wiki/Encryption_algorithm "Encryption algorithm") known as a [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher "Caesar cipher"), used by [Julius Caesar](https://en.wikipedia.org/wiki/Julius_Caesar "Julius Caesar") in the 1st century BC.[[3]](https://en.wikipedia.org/wiki/ROT13#cite_note-3)

[Johann Ernst Elias Bessler](https://en.wikipedia.org/wiki/Johann_Ernst_Elias_Bessler "Johann Ernst Elias Bessler"), an 18th century clockmaker and constructor of [perpetual motion](https://en.wikipedia.org/wiki/Perpetual_motion "Perpetual motion") machines, pointed out that ROT13 encodes his surname as _Orffyre_. He used its [latinised](https://en.wikipedia.org/wiki/Latinisation_of_names "Latinisation of names") form, _Orffyreus_, as his pseudonym.[[4]](https://en.wikipedia.org/wiki/ROT13#cite_note-4)

ROT13 was in use in the net.jokes [newsgroup](https://en.wikipedia.org/wiki/Newsgroup "Newsgroup") by the early 1980s.[[a]](https://en.wikipedia.org/wiki/ROT13#cite_note-7) It is used to hide potentially offensive jokes, or to obscure an answer to a puzzle or other [spoiler](https://en.wikipedia.org/wiki/Spoiler_(media) "Spoiler (media)").[[2]](https://en.wikipedia.org/wiki/ROT13#cite_note-schneier-2)[[7]](https://en.wikipedia.org/wiki/ROT13#cite_note-jargon-8)[_[unreliable source?](https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources "Wikipedia:Reliable sources")_] A shift of thirteen was chosen over other values, such as three as in the original [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher "Caesar cipher"), because thirteen is the value for which encoding and decoding are equivalent, thereby allowing the convenience of a single command for both.[[7]](https://en.wikipedia.org/wiki/ROT13#cite_note-jargon-8) ROT13 is typically supported as a built-in feature to news reading software.[[7]](https://en.wikipedia.org/wiki/ROT13#cite_note-jargon-8) Email addresses are also sometimes encoded with ROT13 to hide them from less sophisticated [spam bots](https://en.wikipedia.org/wiki/Spam_bots "Spam bots").[[8]](https://en.wikipedia.org/wiki/ROT13#cite_note-9)[_[dubious](https://en.wikipedia.org/wiki/Wikipedia:Accuracy_dispute#Disputed_statement "Wikipedia:Accuracy dispute") – [discuss](https://en.wikipedia.org/wiki/Talk:ROT13#Dubious "Talk:ROT13")_] It is also used to circumvent email screening and spam filtering. By obscuring an email's content, the screening algorithm is unable to identify the email as, for instance, a security risk, and allows it into the recipient's in-box.

In encrypted, normal, English-language text of any significant size, ROT13 is recognizable from some letter/word patterns. The words "n", "V" (capitalized only), and "gur" (ROT13 for "a", "I", and "the"), and words ending in "yl" ("ly") are examples.

ROT13 is not intended to be used where [secrecy](https://en.wikipedia.org/wiki/Confidentiality "Confidentiality") is of any concern—the use of a constant shift means that the encryption effectively has no [key](https://en.wikipedia.org/wiki/Key_(cryptography) "Key (cryptography)"), and decryption requires no more knowledge than the fact that ROT13 is in use. Even without this knowledge, the algorithm is easily broken through [frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis_(cryptanalysis) "Frequency analysis (cryptanalysis)").[[2]](https://en.wikipedia.org/wiki/ROT13#cite_note-schneier-2) Because of its utter unsuitability for real secrecy, ROT13 has become a catchphrase to refer to any conspicuously weak [encryption](https://en.wikipedia.org/wiki/Encryption "Encryption") scheme; a critic might claim that "56-bit [DES](https://en.wikipedia.org/wiki/Data_Encryption_Standard "Data Encryption Standard") is little better than ROT13 these days". Also, in a play on real terms like "double DES", the terms "double ROT13", "ROT26", or "2ROT13" crop up with humorous intent (due to the fact that, since applying ROT13 to an already ROT13-encrypted text restores the original [plaintext](https://en.wikipedia.org/wiki/Plaintext "Plaintext"), ROT26 is equivalent to no encryption at all), including a spoof academic paper entitled "On the 2ROT13 Encryption Algorithm".[[9]](https://en.wikipedia.org/wiki/ROT13#cite_note-10) By extension, triple-ROT13 (used in joking analogy with 3DES) is equivalent to regular ROT13.

In December 1999, it was found that [Netscape Communicator](https://en.wikipedia.org/wiki/Netscape_Communicator "Netscape Communicator") used ROT13 as part of an insecure scheme to store email passwords.[[10]](https://en.wikipedia.org/wiki/ROT13#cite_note-11) In 2001, Russian programmer [Dimitry Sklyarov](https://en.wikipedia.org/wiki/Dimitry_Sklyarov "Dimitry Sklyarov") demonstrated that an eBook vendor, New Paradigm Research Group (NPRG), used ROT13 to encrypt their documents; it has been speculated that NPRG may have mistaken the ROT13 toy example—provided with the [Adobe](https://en.wikipedia.org/wiki/Adobe_Systems "Adobe Systems") eBook [software development kit](https://en.wikipedia.org/wiki/Software_development_kit "Software development kit")—for a serious encryption scheme.[[11]](https://en.wikipedia.org/wiki/ROT13#cite_note-12) Windows XP uses ROT13 on some of its registry keys.[[12]](https://en.wikipedia.org/wiki/ROT13#cite_note-13) ROT13 is also used in the [Unix fortune program](https://en.wikipedia.org/wiki/Fortune_(Unix) "Fortune (Unix)") to conceal potentially offensive [dicta](https://en.wikipedia.org/wiki/Dicta "Dicta").


## Letter games and net culture


ROT13 provides an opportunity for letter games. Some words will, when transformed with ROT13, produce another word. Examples of 7-letter pairs in the [English language](https://en.wikipedia.org/wiki/English_language "English language") are _[abjurer](https://en.wiktionary.org/wiki/abjurer "wiktionary:abjurer")_ and _nowhere_, and _[Chechen](https://en.wikipedia.org/wiki/Chechen_people "Chechen people")_ and _[purpura](https://en.wiktionary.org/wiki/purpura "wiktionary:purpura")_. Other examples of words like these are shown in the table.[[13]](https://en.wikipedia.org/wiki/ROT13#cite_note-14) The pair _[gnat](https://en.wikipedia.org/wiki/Gnat "Gnat")_ and _tang_ is an example of words that are both ROT13 reciprocals and reversals.

The 1989 [International Obfuscated C Code Contest](https://en.wikipedia.org/wiki/International_Obfuscated_C_Code_Contest "International Obfuscated C Code Contest") (IOCCC) included an entry by Brian Westley. Westley's [computer program](https://en.wikipedia.org/wiki/Computer_program "Computer program") can be encoded in ROT13 or reversed and still [compiles](https://en.wikipedia.org/wiki/Compiler "Compiler") correctly. Its operation, when executed, is either to perform ROT13 encoding on, or to reverse its input.[[14]](https://en.wikipedia.org/wiki/ROT13#cite_note-15)

The newsgroup alt.folklore.urban coined a word—_furrfu_—that was the ROT13 encoding of the frequently encoded utterance "[sheesh](https://en.wiktionary.org/wiki/sheesh "wikt:sheesh")". "Furrfu" evolved in mid-1992 as a response to postings repeating [urban myths](https://en.wikipedia.org/wiki/Urban_myth "Urban myth") on alt.folklore.urban, after some posters complained that "Sheesh!" as a response to [newcomers](https://en.wikipedia.org/wiki/Newbie "Newbie") was being overused.[[15]](https://en.wikipedia.org/wiki/ROT13#cite_note-16)

## Variants

ROT5 is a practice similar to ROT13 that applies to numeric digits (0 to 9). ROT13 and ROT5 can be used together in the same message, sometimes called ROT18 (18 = 13 + 5) or ROT13.5.

ROT47 is a derivative of ROT13 which, in addition to scrambling the basic letters, treats numbers and common symbols. Instead of using the sequence A–Z as the alphabet, ROT47 uses a larger set of characters from the common [character encoding](https://en.wikipedia.org/wiki/Character_encoding "Character encoding") known as [ASCII](https://en.wikipedia.org/wiki/ASCII "ASCII"). Specifically, the 7-bit printable characters, excluding space, from decimal 33 '!' through 126 '~', 94 in total, taken in the order of the numerical values of their ASCII codes, are rotated by 47 positions, without special consideration of case. For example, the character A is mapped to p, while a is mapped to 2. The use of a larger alphabet produces a more thorough obfuscation than that of ROT13; for example, a telephone number such as +1-415-839-6885 is not obvious at first sight from the scrambled result Z'\c`d\gbh\eggd. On the other hand, because ROT47 introduces numbers and symbols into the mix without discrimination, it is more immediately obvious that the text has been encoded.

Example:

The Quick Brown Fox Jumps Over The Lazy Dog.

enciphers to

%96 "F:4< qC@H? u@I yF>AD ~G6C %96 {2KJ s@8]

The [GNU C library](https://en.wikipedia.org/wiki/GNU_C_library "GNU C library"), a set of standard routines available for use in [computer programming](https://en.wikipedia.org/wiki/Computer_programming "Computer programming"), contains a [function](https://en.wikipedia.org/wiki/Function_(programming) "Function (programming)")—**memfrob()**[[16]](https://en.wikipedia.org/wiki/ROT13#cite_note-17)—which has a similar purpose to ROT13, although it is intended for use with arbitrary binary data. The function operates by combining each [byte](https://en.wikipedia.org/wiki/Byte "Byte") with the [binary](https://en.wikipedia.org/wiki/Binary_number "Binary number") pattern 00101010 ([42](https://en.wikipedia.org/wiki/42_(number) "42 (number)")) using the [exclusive or](https://en.wikipedia.org/wiki/Exclusive_or "Exclusive or") (XOR) operation. This effects a [simple XOR cipher](https://en.wikipedia.org/wiki/Simple_XOR_cipher "Simple XOR cipher"). Like ROT13, XOR (and therefore memfrob()) is self-reciprocal, and provides a similar, virtually absent, level of security.

