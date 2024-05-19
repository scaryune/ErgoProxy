---
aliases: [email, Email]
---
# Email
First invented in the 1970s during #ARPANET by #Ray-Tomlinson
- Email address format:
	- `<user mailbox>@<domain>`

## Formatting and Headers:
Internet Message Format ( #IMF): how email messages are formatted. Email clients/ usually provide the option to view email headers and/or source code.
- source code: displays the HTML which makes up the content of the message
- header: shows the headers attached to the email.
- #RFC-5322 for Internet Message Format

#### Headers:
- From, Subject, Date, & To
	- usually clearly visible in the email client
- Headers viewed in the raw format:
	-  X-Originating IP/ #X-header:
		- the IP the email was sent from
	- Smtp.mailfrom/ header.from: the domain the email was sent from 
	- Reply-to: the email address a reply will be sent to
		- also may be referred to as "Return-Path"
	- Received:
		- most reliable header: lists all of the servers/ computers which the email traveled through
		- Read from top to bottom:
			- first received line (at the top) is the device the email was destined for
	- #domainkey-signature:
	- Message-ID:
		- a unique string assigned to the email by the mail system when it is first created
		- easy to spoof/ forge
	- Content-Type:
		- Tells you the format of the message (HTML or plaintext, etc.)
	- X-Spam-Status:
		- a spam score created by the service or mail client
	- X-Spam-Level:
		- Another spam score created by the service/ client
	- Message Body

The source code of attachments can also be viewed which includes headers:
- May include:
	- Content-Type
	- Content-Disposition: ('attachment', etc)
	- Content-Transfer-Encoding:
		- tells how the attachment is encoded (ex: Base64)

#### Body/ HTML
- #JSON_tokens
- #base-64
	- sed command
	- base64 --> pdf
- HTML

## Delivery:
Uses 3 main protocols:
1. [SMTP](/networking/protocols/SMTP.md): Simple Mail Transfer Protocol
	- handles sending of emails
2. [POP3](/networking/protocols/POP3.md): Post Office Protocol
	- transfers emails b/w client and #mail-server
	- downloads all mail from the server for your inbox ==onto your local computer==
		- emails are available when you're offline
1. [IMAP](/networking/protocols/IMAP.md): Internet Message Access Protocol
	- same as #POP3
		- Difference: syncs your mail client w/ the server
			- emails ==stay on the server==
			- May just sync the email headers so you can see what emails there are, then download the message body when you want to read them
			- available on different devices
				- the device just needs to be able to connect to the mail server where the emails are stored to access them.

![](/networking/networking-pics/email-1.png)
-TryHackMe.com

### Steps:
1. email is composed by `alexa@janedoe.com` addressed to `billy@johndoe.com` w/ her favorite email client
2. the #SMTP server needs to determine where to send the email
	- queries the [DNS](/networking/DNS/DNS.md) for info on `johndoe.com`
3. the #DNS server obtains the info on `johndoe.com` and sends it back to the SMTP server
4. the SMTP server sends the email from Alexa across the interned to Billy's inbox at `johndoe.com`
	- has to pass through firewalls
5. The email passes through multiple SMTP servers 
6. it finally makes it to the destination server
7. Alexa's email is forwarded and sits in the local #POP3/IMAP-server 
8. when Billy logs into his email client, it queries the POP3/IMAP server for new emails in his inbox
9. Alexa's email is copied (IMAP) or downloaded (POP3) to Billy's email client.

==Each protocol has its designated port==
ex: SMTP = #port-25

## Email Client Ports:
Mail clients connect to #mail-servers using either POP3 or IMAP
- INCOMING:
	- IMAP (Secure): ==recommended==
		- #port-993: Secure Transport
			- #SSL is enabled
	- IMAP (Insecure): #port-143 
	- POP3 (Secure):
		- #port-995: SSL enabled
	- POP# (Insecure): #port-110
- OUTGOING:
	- ==SMTP is the default for outgoing email
	- #port-465: (Secure) - SSL enabled
	- #port-587: (Insecure)
- Others:
	- #port-25: SMTP ==outdated/ not recommended==

#### Securing ports with #TLS/SSL:
- login information and messages are encrypted
- mail server is authenticated using #certificates
	- #public-key which matches a #private-key on the email/ POP3/IMAP server

## Security:

See: [phishing-defense](/cybersecurity/defense/phishing-defense.md)
- Using #BCC / Blind Carbon Copy:
	- Protects the privacy of email addresses form the original email (recipients unable to see email addresses listed in the BCC field)
	- 

>[!links]
>Ports and security:
>https://help.dreamhost.com/hc/en-us/articles/215612887-Email-client-protocols-and-port-numbers
>
> Internet Message Format/ #RFC-5322 :
> https://datatracker.ietf.org/doc/html/rfc5322
> 
> Headers:
> https://mediatemple.net/community/products/all/204643950/understanding-an-email-header
