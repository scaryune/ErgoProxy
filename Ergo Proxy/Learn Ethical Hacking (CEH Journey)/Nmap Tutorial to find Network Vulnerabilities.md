
![[nmap-vulnerability-scan.webp]]

Nmap, or network mapper, is a toolkit for functionality and penetration testing throughout a network, including port scanning and vulnerability detection.

Nmap scripting engine (NSE) Script is one of the most popular and powerful capabilities of Nmap. These Nmap vulnerability scan scripts are used by [penetration testers](https://geekflare.com/web-penetration-testing-tools/) and hackers to examine common known vulnerabilities.

Common Vulnerabilities and Exposures (CVE) is a database of publicly disclosed data security issues. It serves as a reference model for detecting vulnerabilities and threats related to the security of information systems.

In this article, we’ll look at how to use Nmap for Vulnerability Scan.

Let’s get started!

## Nmap Installation

Nmap is pre-installed in almost every Linux distribution. In case it’s missing, you need to install it manually. It can be easily installed with the following command.

```bash
apt-get install nmap
```

And you can also install it by cloning the official [git repository](https://github.com/nmap/nmap).

```bash
git clone https://github.com/nmap/nmap.git
```

Next, navigate to that directory and install the requirements using the below commands.

```bash
./configure
make
make install
```

This software’s most recent version, as well as binary installers for Windows, macOS, and Linux (RPM), are available [here](https://nmap.org/download.html).

## Vulnerability scan with Nmap

**Nmap-vulners**, **vulscan**, and **vuln** are the common and most popular CVE detection scripts in the Nmap search engine. These scripts allow you to discover important information about system security flaws.

### Nmap-vulners

One of the most well-known vulnerability scanners is [Nmap-vulners](https://github.com/vulnersCom/nmap-vulners). Let’s look at how to set up this tool as well as how to run a basic CVE scan. The Nmap script engine searches HTTP responses to identify CPEs for the given script.

#### Installation

To install the Nmap-vulners script, navigate to the Nmap scripts directory using the following command.

```bash
cd /usr/share/nmap/scripts/
```

The Next step is to clone the git repository.

```bash
git clone https://github.com/vulnersCom/nmap-vulners.git
```

After cloning the git repository, you won’t need to do anything else for the configuration. The tool will be automatically installed.

And if you want to see the NSE scripts present in Nmap-vulners database, use `ls` command. It will display all the .nse extension scripts on the terminal.

#### Usage

It’s easy to use NSE scripts. Simply pass the -script argument to our Nmap command to instruct what NSE script to use.

```bash
nmap -sV --script vulners [--script-args mincvss=<arg_val>] <target>
```

Don’t forget to pass “-sV” argument while using NSE scripts. Nmap-vulners will be unable to access the Vulners exploit database if it does not receive any version information from Nmap. So, the -sV parameter is required all the time.

#### Example command

The syntax is quite straightforward. Just call the script with “–script” option and specify the vulners engine and target to begin scanning.

```bash
nmap -sV --script nmap-vulners/ <target>
```

If you wish to scan any specific ports, just add “-p” option to the end of the command and pass the port number you want to scan.

```bash
nmap -sV --script nmap-vulners/ <target> -p80,223
```

### Nmap – vuln

NSE scripts are classified according to a set of predetermined categories to which each script belongs. Authentication, broadcast, brute force, intrusive, malware, safe, version, and vuln are some of the categories. You can find all the category types of NSE scripts and their phases [here](https://nmap.org/book/nse-usage.html).

The scripts which come under the “vuln” category look for specific known vulnerabilities and only report back if any are identified in the target system.

```bash
nmap -sV --script vuln <target>
```

### Nmap-vulscan

[Vulscan](https://github.com/scipag/vulscan) is an NSE script that assists Nmap in detecting vulnerabilities on targets based on services and version detections. vulscan is like a module for Nmap that transforms it into a vulnerability scanner. The Nmap option -sV allows for per-service version detection, which is used to identify potential exploits for the detected vulnerabilities in the system. 

Currently, the following pre-installed databases are available:

- exploitdb.csv
- osvdb.csv
- securitytracker.csv
- openvas.csv
- scipvuldb.csv
- xforce.csv
- securityfocus.csv
- cve.csv

#### Installation

To install the Vulscan, First, go to the Nmap scripts directory by using the following command.

```bash
cd /usr/share/nmap/scripts/
```

The Next step is to clone the git repository and install all the requirements.

```bash
git clone https://github.com/scipag/vulscan.git

ln -s `pwd`/scipag_vulscan /usr/share/nmap/scripts/vulscan 
```

Vulscan makes use of pre-configured databases saved locally on our machine. To update the database, go to the updater directory. Type the following command into a terminal to navigate to the updater directory.

```bash
cd vulscan/utilities/updater/
```

Next, change the permissions of the file to be run in the system.

```bash
chmod +x updateFiles.sh
```

And finally, update the exploit databases with the below command.

```bash
 ./updateFiles.sh
```

#### Usage

Let’s use vulscan to do a Nmap vulnerability scan. The vulscan NSE script can be used in the same way as nmap-vulners.

```bash
nmap -sV --script vulscan <target>
```

By default, Vulscan will search all of the databases simultaneously. It takes a lot of time to query information using all the databases. Using the vulscandb parameter, you can pass only one CVE database at a time.

```bash
--script-args vulscandb=database_name
```

#### Example Command

```bash
nmap -sV --script vulscan --script-args vulscandb=exploit.csv <target> -p 80,233
```

## Individual vulnerability Scanning

Individual vulnerability scans can also be performed utilizing particular scripts within each category. Here is a list of all 600+ [NSE scripts](https://nmap.org/nsedoc/scripts/) and 139 [NSE libraries](https://nmap.org/nsedoc/lib/).

#### Examples

- **http-csrf**: Cross-Site Request Forgery (CSRF) vulnerabilities are detected by this script.

```bash
nmap -sV --script http-csrf <target>
```

- **http-sherlock**: Intends to exploit the “shellshock” vulnerability in web applications.

```bash
nmap -sV --script http-sherlock <target>
```

- **http-slowloris-attack:** Without launching a DoS attack, this script checks a web server or a target system for vulnerability to perform the Slowloris DoS attack.

```bash
nmap -sV --script http-slowloris-check <target>
```

- **http-vmware-path-vuln**: VMWare ESX, ESXi, and Server are all tested for a path-traversal vulnerability

```bash
nmap -sV --script http-vmware-path-vuln <target>
```

- **http-passwd**: Attempts to retrieve /etc/passwd or boot.ini to see if a web server is vulnerable to directory traversal.

```bash
nmap -sV --script http-passwd <target>
```

- **http-internal-ip-disclosure**: When sending an HTTP/1.0 request without a Host header, this check determines if the web server leaks its internal [IP address](https://geekflare.com/find-ip-address-of-router/).

```bash
nmap -sV --script http-internal-ip-disclosure <target>
```

- **http-vuln-cve2013-0156**: Detects Ruby on Rails servers that are vulnerable to [DOS attacks](https://geekflare.com/test-origin-ip-exposed/) and command injection.

```bash
nmap -sV --script http-vuln-cve2013-0156 <target-address>
```

And finally, here is a list of all NSE scripts which come under the “[vuln](https://nmap.org/nsedoc/categories/vuln.html)” category.

## Is your system capable of detecting Nmap scans?

Reconnaissance is the first phase in [ethical hacking](https://geekflare.com/ethical-hacking-courses/) and penetration testing. Hackers use the reconnaissance phase to locate flaws and loopholes in a system to attack. Therefore defense systems should be able to detect them.

You will receive alerts if you use SIEM (Security Information and Event Management )tools, [firewalls](https://geekflare.com/computer-smartphone-personal-firewall/), and other defensive measures. And here is a list of the [best SIEM Tools](https://geekflare.com/best-siem-solutions/) to Secure Your business and organization from Cyberattacks. These tools even help in logging Nmap scans. Vulnerability scans are worthwhile since early identification can avert future damage to the systems.

### Conclusion

I hope you found this article very useful in learning how to use Nmap for vulnerability scan.

You may also be interested in learning the list of [Open Source Web Security Scanners](https://geekflare.com/open-source-web-security-scanner/) to find vulnerabilities.