<h1>Overview</h1>

<p>OpenAdmin is a relatively easy machine which provides a good level of exposure of what to expect in a standard penetration test, as well as a good reference of how a standard OSCP machine may be like. </p>

<p>The vulnerabilities exploited in the box are as follows:
1. OpenNetAdmin 18.1.1 Command Injection Exploit - https://www.exploit-db.com/exploits/47772
2. Exposure of credentials along with credential reuse
3. Unintended exposure of SSH keys
4. Privilege Escalation using sudo

<h1>Discovery</h1>
Using a standard nmap command, using default scripts and enumerating versions, resulted in the following output:
<img name="nmapscan" src="https://user-images.githubusercontent.com/58163840/72706282-a1a81080-3b2b-11ea-8d87-cd92ce809ed4.png">
