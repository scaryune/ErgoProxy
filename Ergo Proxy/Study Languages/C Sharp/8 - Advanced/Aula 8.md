# C# regex

A Regex (**Reg**ular **Ex**pression) is a pattern that is used to check whether a given string matches that pattern. For example,

```
// a regex pattern
"^m.t$"
```

The above pattern indicates a three-letter string where,

- `^` - indicates string starts with `m`
- `.` - indicates any one letter or character
- `$` - indicates string ends with `t`

For example strings like `"mat"` and `"mit"` match the above regex pattern. However, strings like `"mom"` and `"magnet"` don't match because these strings are not **3** letter words that start with `m` and end with `t`.

We will learn about regular expressions in detail below.

---

## C# Regex Class

C# provides a class called `Regex` to use features of a regular expression. Before using the `Regex` class, we need to use `System.Text.RegularExpression` namespace.

Then, we need to create an instance of the `Regex` class:

```
Regex regexName = new Regex(pattern);
```

Here,

- `regexName` - name of the instance of the `Regex` class
- `pattern` - regular expression pattern that we want to pass

---

## Example: C# Regex

```
using System;
using System.Text.RegularExpressions;
class Program
{
    // a regular expression pattern for a five-letter word
    // that starts with "a" and ends with "e"  
    static string pattern = "^a...e$";

    static void Main()
    {
        // create an instance of Regex class and
        //  pass the regular expression (i.e pattern)
        Regex rg = new Regex(pattern);

        // IsMatch() returns true if "apple" matches the regular expression 
        if (rg.IsMatch("apple"))
        {
            Console.WriteLine("String matches the pattern");
        }
        else
        {
            Console.WriteLine("String doesn't match the pattern");
        }
    }
}
```

**Output**

String matches the pattern

In the above example, we have checked whether the string `"apple"` matches the defined regular expression pattern.

The pattern `"^a...e$"` indicates any five-letter string starting with `a` and ending with `e`. Here, the `IsMatch()` method returns `True` if the string that we pass matches the regex pattern.

If we pass another string for example - `"apache"`, it doesn't match with `pattern` because `"apache"` has more than three letters between `a` and `e`.

**Note:** We specify regex as a string. For example,

```
string pattern = "^a...e$";
```

---

## How Regex Works?

In C#, there is an engine called regex engine which internally checks the regex pattern in the given string.

![regex engine is taking two inputs](https://www.programiz.com/sites/tutorial2program/files/csharp-working-of-regex-engine.png "how regex works")

Working of regex engine

In the above image, the regex engine process the two inputs :

- `^a…e$` - the regex pattern
- `"apple"` - the given string that we want to match

When the regex pattern is passed into the engine, it is interpreted. The engine is then responsible for search operation i.e, matching the regex expression pattern with the input string.

---

## Metacharacters

To specify regular expressions, metacharacters are used. Metacharacters are characters that are interpreted in a special way by a regex engine.

Some of the basic metacharacters are:

- `[]` - square bracket
- `.` - period
- `^` - caret
- `$` - dollar
- `*` - star
- `+` - plus
- `?` - question mark
- `{}` - braces
- `()` - parenthesis
- `|` - alternation

---

### []- Square brackets

`[]` specifies a set of characters you wish to match.

For example,

- regex - `[abc]`
- matches - any string that contains any of the `a`, `b`, or `c`.

Let's check if the following string examples match the regex pattern `[abc]`.

|String|Matched?|Reason|
|---|---|---|
|a|1 Match|string contains `a`|
|ac|2 Match|string contains `a` and `c`|
|jim|0 Match|string doesn't contain any of `a`, `b` or `c`|
|abc|3 Match|string contains all three - `a`, `b` and `c`|

**Note:** You can also specify a range of characters using `-` inside square brackets. For example,

- `[a-e]` is the same as `[abcde]`
- `[0-3]` is the same as `[0123]`

---

### . - Period

A period specifies any single character (except newline `'\n'`).

For example,

- regex - `…`
- matches - strings containing three letters

Let's check if the following string examples match the regex pattern `…`

|String|Matched?|Reason|
|---|---|---|
|abs|1 Match|string contains three letters (`a`, `b`, `s`)|
|ac|0 Match|string doesn't contain three letters|
|jim|1 Match|string contains three letters|
|abcd|1 Match|string contains three letters|
|abcjkl|2 Matches|string contains **6** letters (**3+3**)|

---

### ^ - Caret

The caret symbol `^` specifies the string starts with a certain character.

For example,

- regex - `^m`
- matches - string starting with the letter `"m"`

Let's check if the following string examples match the regex pattern `^m`.

|String|Matched?|Reason|
|---|---|---|
|man|1 Match|`man` starts with `"m"`|
|m|1 Match|`m` starts with `"m"`|
|Man|0 Match|`Man` doesn't start with `"m"`|
|sms|0 Match|`sms` doesn't start with `"m"`|

---

### $ - Dollar

The dollar symbol `$` specifies the string ends with a certain character.

For example,

- regex - `y$`
- matches - string ending with the letter `"y"`

Let's check if the following string examples match the regex pattern `y$`.

|String|Matched?|Reason|
|---|---|---|
|monday|1 Match|`monday` ends with `"y"`|
|say|1 Match|`say` ends with `"y"`|
|myname|0 Match|`myname` doesn't end with `"y"`|

---

### * - Star

The star symbol `*` matches zero or more occurrences of the pattern left to it.

For example,

- regex - `ca*t`
- matches - string that has any number[including zero] of `a` in between `c` and `t`

Let's check if the following string examples match the regex pattern `ca*t`.

|String|Matched?|Reason|
|---|---|---|
|cat|1 Match|`cat` has one `a` between `c` and `t`|
|ct|1 Match|`ct` has zero `a` between `c` and `t`|
|caaaat|1 Match|`caaaat` has three `a` between `c` and `t`|
|crt|0 Match|`crt` has letter `r` (not `a`) between `c` and `t`|
|caatcaaat|2 Matches|`caatcaaat` has `a` in two places (`caat` and `caaat`)|

---

### + - Plus

The plus symbol `+` matches one or more occurrences of the pattern left to it.

For example,

- regex - `ma+t`
- matches - string that has one or more numbers of `a` in between `m` and `t`

Let's check if the following string examples match the regex pattern `ma+t`.

|String|Matched?|Reason|
|---|---|---|
|mat|1 Match|`mat` has one `a` between `m` and `t`|
|mt|0 Match|`mt` doesn't have `a` between `m` and `t`|
|matemaat|2 Matches|`matemaat` has two matching substrings (`mat` and `maat`)|
|mart|0 Match|`a` is not followed by `t` in `mart`|

---

### ? - Question Mark

The question mark symbol `?` matches zero or one occurrence of the pattern left to it.

For example,

- regex - `ma?n`
- matches - string that has one or zero number of `a` in between `m` and `n`

Let's check if the following string examples match the regex pattern `ma?n`.

|String|Matched?|Reason|
|---|---|---|
|man|1 Match|`man` has one `a` between `m` and `n`|
|mn|1 Match|`mn` has zero number of `a` between `m` and `n`|
|maaaaan|0 Match|`maaaaan` has more than one `a` character between `m` and `n`|
|woman|1 Match|`woman` has one `a` between `m` and `n`|

---

### {} - Braces

The braces symbol `{}` is used to specify the range of repetitions of the pattern left to it.

For example,

- regex - `a{2,3}`
- matches - string that has at least **2** `a`'s and at most **3** `a`'s left to it

Let's check if the following string examples match the regex pattern `a{2,3}`.

|String|Matched?|Reason|
|---|---|---|
|abcdat|0 Match|has only one `a` on left of other character|
|abcdaat|1 Match|`abcdaat` has two `a` on left of other character|
|aabc daaat|2 matches|`aabc daaat` has two and three `a` on left of other character|

---

### | - Alternation

The vertical bar `|` is used as `or` operator.

For example,

- regex - `a|b`
- matches - string that has either `a` or `b`

Let's check if the following string examples match the regex pattern `a|b`.

|String|Matched?|Reason|
|---|---|---|
|cde|0 Match|string doesn't have either `a` or `b`|
|ade|1 Match (match at `ade`)|there is `a` in the string|
|acdbea|3 matches (at `acdbea`)|string has two `a` and one `b`|

---

### () - Parenthesis

Parenthesis `()` is used to group sub-patterns.

For example,

- regex - `(a|b|c)xz`
- matches - any string that has either `a` or `b` or `c` followed by `xz`

Let's check if the following string examples match the regex pattern `(a|b|c)xz`.

|String|Matched?|Reason|
|---|---|---|
|abxz|1 Match (match at `abxz`)|`a` or `b` is followed by `xz`|
|ab xz|0 Match|there is a white space between `ab` and `xz`|
|axz cabxz|2 matches (at `axzbc` and `cabxz`)|`a` is followed by `xz` in and `b` is followed by `xz`|

---

## Special Sequences

Special sequences make commonly used patterns easier to write.

Some of the special sequences are:

`**\A**` **- Matches if the specified characters are at the start of a string.**

Let's check if the following string examples match the regex pattern `\Athe`.

|String|Matched?|Reason|
|---|---|---|
|the sun|Match|string starts with `the`|
|In the|No Match|string doesn't start with `the`|

---

`**\b**` **- Matches if the specified characters are at the beginning or end of a word.**

For example,

- regex - `\bfoo`
- matches - any word in a string that has `foo` at the beginning.

Let's check if the following string examples match the regex pattern `\bfoo`.

|String|Matched?|Reason|
|---|---|---|
|football|Match|`foo` is at the beginning of a word (`football`)|
|a football|Match|`foo` is at the beginning of a word (`a` `football`)|
|afootball|No Match|there is `a` at the beginning of the word (`afootball`)|

Take another regex for example,

- regex - `foo\b`
- matches - any word in a string that has `foo` at the end.

Let's check if the following string examples match the regex pattern `foo\b`.

|String|Matched?|Reason|
|---|---|---|
|the foo|Match|`foo` is at the end of a word (`the` `foo`)|
|the afoo test|Match|`foo` is at the end of a word (`the afoo` `test`)|
|the afootest|No Match|there is no `foo` at the end of a word|

---

`**\B**` **- Matches if the specified characters are not at the beginning or end of a word.**

For example,

- regex - `\Bfoo`
- matches - any word in a string that **doesn't have** `foo` at the beginning.

|String|Matched?|Reason|
|---|---|---|
|football|No Match|string has `foo` at the beginning|
|the foo|No Match|string has `foo` at the beginning|
|afootball|Match|string doesn't have `foo` at the beginning|

Take another regex for example,

- regex - `foo\B`
- matches - any word in a string that **doesn't have** `foo` at the end

Let's check if the following string examples match the regex pattern `foo\B`.

|String|Matched?|Reason|
|---|---|---|
|football|Match|string doesn't have `foo` at the end|
|the foo|No Match|string has `foo` at the end|
|afootball|Match|string doesn't have `foo` at the end|

---

`**\d**` **- Matches any decimal digit. Equivalent to** `**[0-9]**`

Let's check if the following string examples match the regex pattern `\d`.

|String|Matched?|Reason|
|---|---|---|
|12abc3|3 matches (at `12abc3`)|there are three decimal digits in the string|
|programming|No Match|there is not any decimal digits in the string|

---

`**\D**` **- Matches any non-decimal digit. Equivalent to** `**[^0-9]**`

Let's check if the following string examples match the regex pattern `\D`.

|String|Matched?|Reason|
|---|---|---|
|12abc3|3 matches (at `12abc3`)|there are three non-decimal digits(`a`, `b` and `c`)|
|1234|No Match|there is not any non-decimal character|

---

`**\s**` **- Matches where a string contains any whitespace character. Equivalent to** `**[ \t\n\r\f\v]**`**.**

Let's check if the following string examples match the regex pattern `\s`.

|String|Matched?|Reason|
|---|---|---|
|program world|1 matches|string contains one white space|
|programworld|No Match|string doesn't contain any white space|

---

`**\S**` **- Matches where a string contains any non-whitespace character. Equivalent to** `**[^ \t\n\r\f\v]**`**.**

Let's check if the following string examples match the regex pattern `\S`.

|String|Matched?|Reason|
|---|---|---|
|a b|2 matches(at `a` `b`)|string contains two non-whitespace characters (`a` and `b`)|
||No Match|string doesn't contain any non-white space|

---

`**\w**` **- Matches any alphanumeric character (digits and alphabets). Equivalent to** `**[a-zA-Z0-9_]**`**.**

Let's check if the following string examples match the regex pattern `\w`.

|String|Matched?|Reason|
|---|---|---|
|a2&": ;c|3 matches (at `12&": ;c`)|string contains three alphanumeric characters (`a`, **2** and **3**)|
|%"> !|No Match||

**Note:** Underscore (`_`) is also considered as an alphanumeric character.

---

`**\W**` **- Matches any non-alphanumeric character. Equivalent to** `**[^a-zA-Z0-9_]**`**.**

Let's check if the following string examples match the regex pattern `\W`.

|String|Matched?|Reason|
|---|---|---|
|a2%c|1 match (at `a2%c`)|string contains one non-alphanumeric character(`%`)|
|apple|No Match|string doesn't contain any non-alphanumeric character|