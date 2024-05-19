command strings you can find data

https://www.baeldung.com/linux/find-string-binary-file

## 1. Introduction[](https://www.baeldung.com/linux/find-string-binary-file#introduction)

## [](https://www.baeldung.com/linux/find-string-binary-file#introduction)

[Binary files](https://www.baeldung.com/linux/files-end-with-newlines#1-text-and-binary-files) and [non-ASCII](https://www.baeldung.com/linux/less-show-special-characters#terminal-character-sets-and-special-characters) files can be challenging to work with because they can contain data that isn’t in a human-readable format. However, we might need to search for specific strings or patterns in these [types of files](https://www.baeldung.com/linux/terminal-locales-check-character-encoding#1-file-encoding), particularly in software development or system administration processes.

Luckily, there are several powerful command-line tools available in Linux that can help us. In this tutorial, we’ll discuss how to use some of these tools.

## 2. Preparing the Binary File[](https://www.baeldung.com/linux/find-string-binary-file#preparing-the-binary-file)

## [](https://www.baeldung.com/linux/find-string-binary-file#preparing-the-binary-file)

The first thing we’ll do is prepare a binary file that will serve as our working file throughout this tutorial.

In order to create an executable binary, let’s create a simple C program, _baeldung.c_, and compile it using the GCC compiler:

```bash
$ echo '#include <stdio.h>
 int main() { 
     printf("BAELDUNG!!!\n");
     return 0;
 }' > baeldung.c && gcc -o baeldung baeldung.c
```

This produces a binary file named _baeldung_. Let’s take a look at it with _[cat](https://www.baeldung.com/linux/files-cat-more-less#cat)_ to see what it includes:

```bash
$ cat baeldung
��GNU��e�m= ``�-�=�=X`�-�=�=�888 XXXDDS�td888 P�td   DDQ�tdR�td�-�=�=HH/lib64/ld-linux-x86-64.so.2GNU�GNU��Q�/�{I��7C
            Y h "libc.so.6puts__cxa_finalize__libc_start_mainGLIBC_2.2.5_ITM_deregisterTMCloneTable__gmon_start___ITM_registerTMCloneTableu�i	1�@�?�?�?�?�?�?��H�H��/H�H�=��R/��H�=y/H�r/H9�tH�./H��t%�����H�=I/H�5B/H)�H��H��?H��H�H��tH�/H����fD�����=/u+UH�=�.H��t
                                                                                               H�=�.�����d�����.]������w�����UH��H�=�������]�f.�f���AWL�=;,AVI��AUI��ATA��UH�-,,SL)�H��_���H��t1��L��L��D��A��H��H9�u�H�[]A\A]A^A_�ff.������H�H��BAELDUNG!!!D���x0����@����P���`9����`��������8zRx
                                                                                                                           ����/D$4���� FJ
                                                                                                                                          �?�:*3$"\����t�����a���
RC
D�h���eF�I�E �E(�D0�H8�G@n8A0A(B BB�����@
�������o�p�
�
 �?��������o���o���o����o�=@GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.08X|���	
 
...
```

As we can clearly observe, the content of the output is mostly not human-readable and comprises non-ASCII characters.

## 3. Using the _strings_ Command to Extract the Text[](https://www.baeldung.com/linux/find-string-binary-file#using-the-strings-command-to-extract-the-text)

## [](https://www.baeldung.com/linux/find-string-binary-file#using-the-strings-command-to-extract-the-text)

**Among the most common approaches for extracting human-readable text from binary files** is using the [_strings_](https://www.baeldung.com/linux/make-random-readable-text-file#using-the-strings-command) command-line utility. With _strings_, we can easily get the printable characters inside a binary file:

```bash
$ strings baeldung
/lib64/ld-linux-x86-64.so.2
libc.so.6
puts
__cxa_finalize
__libc_start_main
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u+UH
[]A\A]A^A_
BAELDUNG!!!
GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.8061
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
baeldung.c
__FRAME_END__

...
```

The _strings_ command has several useful options we can utilize:

- _-a_ scans the whole file instead of only specific sections in object files, but this doesn’t make any difference in our executable binary
- _-f_ prints the file names before each text line
- _-n_ helps us specify the minimum length of a sequence of characters to be printed (the default is 4 characters)
- _-t_ prints the offset of the string before each text in a specified format (_d_ means _decimal_)

**Let’s get only the strings that are at least _10_ characters long in our binary and add the filename and offset data before each string**:

```bash
$ strings -t d -f -n 10 baeldung
baeldung:     792 /lib64/ld-linux-x86-64.so.2
baeldung:    1152 __cxa_finalize
baeldung:    1167 __libc_start_main
baeldung:    1185 GLIBC_2.2.5
baeldung:    1197 _ITM_deregisterTMCloneTable
baeldung:    1225 __gmon_start__
baeldung:    1240 _ITM_registerTMCloneTable
baeldung:    4554 []A\A]A^A_
baeldung:    8196 BAELDUNG!!!
baeldung:   12304 GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
baeldung:   13913 crtstuff.c
baeldung:   13924 deregister_tm_clones
baeldung:   13945 __do_global_dtors_aux
baeldung:   13967 completed.8061
baeldung:   13982 __do_global_dtors_aux_fini_array_entry
baeldung:   14021 frame_dummy
baeldung:   14033 __frame_dummy_init_array_entry
baeldung:   14064 baeldung.c
baeldung:   14075 __FRAME_END__

...
```

Now, **we can find a specific string with the help of [_grep_](https://www.baeldung.com/linux/common-text-search)**:

```bash
$ strings -t d baeldung | grep -i baeldung
   8196 BAELDUNG!!!
  14064 baeldung.c
```

As we can see above, we got the name of the C file and the string we wanted to print in the code.

## 4. Using the _od_ Command[](https://www.baeldung.com/linux/find-string-binary-file#using-the-od-command)

## [](https://www.baeldung.com/linux/find-string-binary-file#using-the-od-command)

Similarly, we can use the [_od_](https://linux.die.net/man/1/od) command to get the string in a binary file. Typically, _od_ displays the contents of a file in octal, decimal, hexadecimal, or ASCII format.

However, we can attach **the _-S_ option to get the strings that contain at least a specified number of characters** in our binary:

```bash
$ od -S 10 baeldung
0001430 /lib64/ld-linux-x86-64.so.2
0002200 __cxa_finalize
0002217 __libc_start_main
0002241 GLIBC_2.2.5
0002255 _ITM_deregisterTMCloneTable
0002311 __gmon_start__
0002330 _ITM_registerTMCloneTable
0020004 BAELDUNG!!!
0030020 GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
0033131 crtstuff.c
0033144 deregister_tm_clones
0033171 __do_global_dtors_aux
0033217 completed.8061
0033236 __do_global_dtors_aux_fini_array_entry
0033305 frame_dummy
0033321 __frame_dummy_init_array_entry
0033360 baeldung.c
0033373 __FRAME_END__

...
```

Like before, we can pipe the output to _grep_ to search for a specific string:

```bash
$ od -S 10 baeldung | grep -i baeldung
0020004 BAELDUNG!!!
0033360 baeldung.c
```

Notably, we get the same result with additional offset information in octal format. Moreover, we can change the offset format to decimal to match the format of our _strings_ example:

[![freestar](https://a.pub.network/core/imgs/fslogo-green.svg)](https://ads.freestar.com/?utm_campaign=branding&utm_medium=lazyLoad&utm_source=baeldung.com&utm_content=baeldung_leaderboard_mid_3)

```bash
$ od -S 10 -A d baeldung | grep -i baeldung
0008196 BAELDUNG!!!
0014064 baeldung.c
```

From the output above, we can verify that the results are the same, as we expected.

## 5. Invoking GNU _grep_ Alone[](https://www.baeldung.com/linux/find-string-binary-file#invoking-gnu-grep-alone)

## [](https://www.baeldung.com/linux/find-string-binary-file#invoking-gnu-grep-alone)

To search for specific non-ASCII strings or patterns in binary files, **we can use the [_grep_](https://www.baeldung.com/linux/common-text-search) command with the _-a_ flag**. This will instruct _grep_ **to handle the binary file as a text file, even if it includes non-ASCII characters**.

Let’s find the same key string in our binary using _grep_:

```bash
$ grep -i -a -o 'baeldung' baeldung
BAELDUNG
baeldung
```

Here, we included **the _-i_ option to enable case-insensitive search and _-o_ to print only the matched parts**.

We can also get the number of matches in our binary file with the _-c_ option:

```perl
$ grep -i -a -c 'baeldung' baeldung
2
```

As shown here, the string _baeldung_ appears twice in the binary file.

## 6. Combining _hexdump_ and _grep_[](https://www.baeldung.com/linux/find-string-binary-file#combining-hexdump-and-grep)

## [](https://www.baeldung.com/linux/find-string-binary-file#combining-hexdump-and-grep)

**To find the instances of a particular byte sequence in a binary file**, we can combine the use of [_hexdump_](https://www.baeldung.com/linux/create-hex-dump#using-hexdump) and _grep_ commands.

We begin by using _hexdump_ to convert the binary file to a hexadecimal dump. Then, we can utilize the output by piping it to _grep_ to locate the desired byte sequence. **To see the ASCII strings, we also need to add the _-C_ option**:

```bash
$ hexdump -C baeldung | grep -i baeldung
00002000  01 00 02 00 42 41 45 4c  44 55 4e 47 21 21 21 00  |....BAELDUNG!!!.|
000036f0  62 61 65 6c 64 75 6e 67  2e 63 00 5f 5f 46 52 41  |baeldung.c.__FRA|
```

From the output above, it’s clear that the string _baeldung_ occurs twice in the executable file.

When we use _hexdump_, **it might be difficult to find a long sequence if it wraps a line**.

## 7. Using _rabin2_[](https://www.baeldung.com/linux/find-string-binary-file#using-rabin2)

## [](https://www.baeldung.com/linux/find-string-binary-file#using-rabin2)

[_rabi__n2_](https://www.baeldung.com/linux/exported-symbols-dll#radare2) is a command-line utility that can analyze and extract information from binary files. It’s commonly used for reverse engineering, analyzing malware, and forensics analysis.

This tool might not be installed by default, so we can use a package manager to install it:

```bash
$ sudo apt install radare2
```

Simply, **we can use the _-zz_ flag to get the strings from the whole binary file**:

```bash
$ rabin2 -zz baeldung
[Strings]
nth paddr      vaddr      len size section   type    string
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
0   0x00000034 0x00000034 4   10             utf16le @8\r@
1   0x00000318 0x00000318 27  28   .interp   ascii   /lib64/ld-linux-x86-64.so.2
2   0x00000471 0x00000471 9   10   .dynstr   ascii   libc.so.6
3   0x0000047b 0x0000047b 4   5    .dynstr   ascii   puts
4   0x00000480 0x00000480 14  15   .dynstr   ascii   __cxa_finalize
5   0x0000048f 0x0000048f 17  18   .dynstr   ascii   __libc_start_main
6   0x000004a1 0x000004a1 11  12   .dynstr   ascii   GLIBC_2.2.5
7   0x000004ad 0x000004ad 27  28   .dynstr   ascii   _ITM_deregisterTMCloneTable
8   0x000004c9 0x000004c9 14  15   .dynstr   ascii   __gmon_start__
9   0x000004d8 0x000004d8 25  26   .dynstr   ascii   _ITM_registerTMCloneTable
10  0x0000110b 0x0000110b 4   5    .text     ascii   u+UH
11  0x000011c9 0x000011c9 11  12   .text     ascii   \b[]A\A]A^A_
12  0x00002004 0x00002004 11  12   .rodata   ascii   BAELDUNG!!!
13  0x00002068 0x00002068 4   5    .eh_frame ascii   \e\f\a\b
14  0x000020a7 0x000020a7 5   6    .eh_frame ascii   :*3$
15  0x000020f9 0x000020f9 4   5    .eh_frame ascii   R\f\a\b
16  0x00003010 0x00000000 42  43   .comment  ascii   GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
17  0x00003659 0x00000001 10  11   .strtab   ascii   crtstuff.c
18  0x00003664 0x0000000c 20  21   .strtab   ascii   deregister_tm_clones
19  0x00003679 0x00000021 21  22   .strtab   ascii   __do_global_dtors_aux
20  0x0000368f 0x00000037 14  15   .strtab   ascii   completed.8061
21  0x0000369e 0x00000046 38  39   .strtab   ascii   __do_global_dtors_aux_fini_array_entry
22  0x000036c5 0x0000006d 11  12   .strtab   ascii   frame_dummy
23  0x000036d1 0x00000079 30  31   .strtab   ascii   __frame_dummy_init_array_entry
24  0x000036f0 0x00000098 10  11   .strtab   ascii   baeldung.c
25  0x000036fb 0x000000a3 13  14   .strtab   ascii   __FRAME_END__

...
```

Above, we can see that the tool prints the strings with a bunch of handy information such as the address of the string, its size, and which section of the binary file it’s located in.

Furthermore, we can retrieve the strings from only the data section in the binary file using the _-z_ option:

```bash
$ rabin2 -z baeldung
[Strings]
nth paddr      vaddr      len size section type  string
―――――――――――――――――――――――――――――――――――――――――――――――――――――――
0   0x00002004 0x00002004 11  12   .rodata ascii BAELDUNG!!!
```

Now, it only outputs the string from the data section of the binary.

## 8. Conclusion[](https://www.baeldung.com/linux/find-string-binary-file#conclusion)

## [](https://www.baeldung.com/linux/find-string-binary-file#conclusion)

In this article, we learned how to extract human-readable text from binary files that contain non-ASCII characters. We started by preparing our binary executable file and then demonstrated how to use **the _strings_ utility, the de facto and most straightforward method** for extracting text from binary files.

We also explored other tools such as the _od_ command and discussed various options that can enhance the capabilities of these tools. Furthermore, we demonstrated how to use _grep_ and _hexdump_ tools to search strings.

Finally, we discussed the use of the _rabin2_ reverse engineering tool, which can provide us with valuable information such as strings and metadata associated with the binary file.