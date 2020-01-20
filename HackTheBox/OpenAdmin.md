<h1>Overview</h1>

<p>OpenAdmin is a relatively easy machine which provides a good level of exposure of what to expect in a standard penetration test, as well as a good reference of how a standard OSCP machine may be like. </p>

<p>The vulnerabilities exploited in the box are as follows: </p>
<ol type="1">
<li>OpenNetAdmin 18.1.1 Command Injection Exploit - https://www.exploit-db.com/exploits/47772 </li>
<li>Exposure of credentials along with credential reuse</li>
<li>Unintended exposure of SSH keys</li>
<li>Privilege Escalation using sudo</li>
</ol>
<h1>Discovery</h1>
Using a standard nmap command, using default scripts and enumerating versions, resulted in the following output:
<img name="nmapscan" src="https://user-images.githubusercontent.com/58163840/72706282-a1a81080-3b2b-11ea-8d87-cd92ce809ed4.png">

As the machine hosted a webserver, further enumeration was conducted to discover possible hidden web directories, in which a /music directory was found which provided a login screen to OpenNetAdmin.
<img name="ona" src="https://user-images.githubusercontent.com/58163840/72707896-84754100-3b2f-11ea-9c1a-f325a9d8b51f.png">

<h1>Remote Command Execution (RCE)</h1>

By cross checking the OpenNetAdmin version against the list of available exploits in Exploit-DB, there are 2 exploits available, namely:
1. https://www.exploit-db.com/exploits/47772
2. https://www.exploit-db.com/exploits/47691

Both exploits do not require user authentication to exploit, however it is worth to note that guest is automatically logged in as seen in the above screenshot, and credentials admin:admin can be used to login as admin to the portal.

RCE can be obtained using exploit 47772 with the following options on Metasploit (Note: The exploit has to be first uploaded into Metasploit as a custom module).

<img name="msf" src="https://user-images.githubusercontent.com/58163840/72708875-a96ab380-3b31-11ea-9c66-73e701701792.png">

<h1> Obtaining User 1 </h1>
Listing /etc/passwd, there were 2 valid users, jimmy and joanna, in which their home folders are located in /home.

Conducting further enumeration, in the following folder, the following database credentials was found:
<img name="jimmy" src="https://user-images.githubusercontent.com/58163840/72709205-6eb54b00-3b32-11ea-85d4-ab1beb92cc8a.png">
The credentials jimmy:n1nj4W4rri0R! is found to be reusable for jimmy, where ssh login was obtaned for jimmy.
<img name="jimmy2" src="https://user-images.githubusercontent.com/58163840/72709486-16327d80-3b33-11ea-982b-7c0dfa74fcd2.png">

