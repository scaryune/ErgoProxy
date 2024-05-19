bandit0 bandit0
bandit 1 NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
bandit 2 rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
bandit 3 aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
bandit 4 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
bandit 5 lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
bandit 6 P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
bandit 7 z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
bandit 8 TESKZC0XvTetK0S9xNwm25STk5iWrBvP
bandit 9 EN632PlfYiZbn3PhVK3XOGSlNInNE00t
bandit 10 G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
bandit 11  6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
bandit 12 JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
bandit 13 wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
bandit 14 fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
bandit 15 jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
bandit 16 JQttfApK4SeyHwDlI9SXGR50qclOAil1
bandit 17 - sshkey17.private
bandit 18 hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg
bandit 19 awhqfNnAbc1naukrpqDYcF95h7HoMTrC
bandit 20 VxCazJaVykI6W36BkBU0mJTCM8rR95XT
bandit 21 NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
bandit 22 WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff
bandit 23 QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G
bandit 24 VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar

```
bandit 5
- human-readable
- 1033 bytes in size
- not executable
find . -type f -size 1033c -name "[[:print:]]*" ! -executable
```

```
bandit 6
- owned by user bandit7
- owned by group bandit6
- 33 bytes in size
find . -size 33c -user bandit7 -group bandit6 | grep bandit7
```

```
bandit 7
The password for the next level is stored in the file **data.txt** next to the word **millionth**
du -b data.txt to see how many are
cat data.txt | grep millionth 
```

```
bandit 8
The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once

`sort` command is used to sort a file, arranging the records in a particular order. By default, the sort command sorts file assuming the contents are ASCII. Using options in the sort command can also be used to sort numerically

`uniq` is a command that filters input and writes to the output. Specifically, it filters based on identical lines. It has a flag `-u`, which filters for unique lines (lines that appear only ones). Another interesting functionality is, for example, that it can also count (`-c`) or only return duplicate lines (`-d`).

The command is often used with `sort`. For `uniq` to filter for unique lines, the lines need to be sorted. `sort` sorts the lines of a text file. Furthermore, it has flags for sorting in reverse (`-r`) and sorting numerically (`-n`).

with that you can do:

sort data.txt | uniq -u this will give you : uniq line 
or
sort data.xt | uniq -c this will run and give you all lines with 10
```


```
bandit 9
The password for the next level is stored in the file **data.txt**, which contains base64 encoded data

Base64 is a group of binary-to-text encoding schemes that represent binary data (more specifically, a sequence of 8-bit bytes) in sequences of 24 bits that can be represented by four 6-bit Base64 digits. 

first you do cat data.txt show you the base64 encription you will need to decode it to do that 

cat data.txt | base64 --decode
```


```
bandit 10
The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

ROT13 ("rotate by 13 places", sometimes hyphenated ROT-13) is a simple letter substitution cipher that replaces a letter with the 13th letter after it in the latin alphabet. ROT13 is a special case of the Caesar cipher which was developed in ancient Rome. 

first you do cat data.txt show you the rot13 encription you will need to decode it to do that 
cat data.txt | rot13 --decode
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
if you can't use rot13 you still can do script in python or find decoder rot13 online.
```


/tmp/tmp.ga3EX8ob0o
/tmp/tmp.IDdOAo8R9g bandit23
/tmp/tmp.OxocE6D9zu bandit 24
sshkey.private

bandit 11
bandit 12


