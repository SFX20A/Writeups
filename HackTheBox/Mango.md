<h1> Overview </h1>

Mango offered several learning opportunities on relatively new technologies which is gaining traction in the recent years, being used on multiple platforms. In which, SQL injection is a well-known vulnerability in this day and age, much less know about at NoSQL injection is possible as well.

The vulnerabiltiies exploited in this box are as follows:
<ol type="1">
  <li>NoSQL injection</li>
  <li>Credential Reuse</li>
  <li>Privilege Escalation using jjs</li>
</ol>

<h1> Discovery </h1>
Using a standard nmap command, using default scripts and enumerating versions, resulted in the following output: 
<img src="https://user-images.githubusercontent.com/58163840/73039115-ddd8bb00-3e22-11ea-8c02-73e895b508c1.png" name="nmap">

By looking at the site hosted at port 443, it brings us to a page seemingly familiar and similar to Google's web search page. By investigating its SSL certificate, it belonged to staging-order.mango.htb:
<img src="https://user-images.githubusercontent.com/58163840/73039692-0d88c280-3e25-11ea-9af0-102662cd1ebd.png" name="mango">

By adding the hostname to /etc/hosts, access to the login page of mango is obtained:
<img src="https://user-images.githubusercontent.com/58163840/73039967-dff04900-3e25-11ea-9be8-533ebab993f0.png" name="portal>

<h1> NoSQL Injection </h1>keys
To verify whether the page is susceptible to NoSQL injection, a simple burpsuite request can be fired with NoSQL injection parameters. A short presentation on understanding NoSQL injection can be found here: https://www.owasp.org/images/e/ed/GOD16-NOSQL.pdf

<img src="https://user-images.githubusercontent.com/58163840/73044002-b63f1e00-3e35-11ea-8b82-5ebc6673a669.png" name="burp">

The above request brings out the first user from the database and automatically authenticates him, successfully bringing us to the website development page, confirming that the site is vulnerable to NoSQL injection. To extract the password via NoSQL injection, it is first required to identify the possible usernames, and their length of password.

To identify the possible usernames using burp, just change the above burp request to a possible username. It was then identified that there are 2 usernames that are valid, mango and admin.

To identify the password length, use the following request:
username=admin&password[$regex]=.{1}
Where ".{1}" is the length of the password. 
It was then identified that mango has a 16 character password, and admin has a 12 character password.

The following script was then written to extract the passwords of the 2 users:
<p>https://github.com/SFX20A/Writeups/blob/master/Scripts/nosqlchecker.py

<p>The following credentials were obtained:
<p>mango:h3mXK8RhU~f{]f5H
<p>admin:t9KcS3>!0B#2

<h1>Obtaining user access</h1>
By using the above credentials for mango, we have obtained SSH access as the user reused his credentials for SSH login.
<img src="https://user-images.githubusercontent.com/58163840/73630886-64f91080-4625-11ea-9b40-9214b066a04b.png" name="useraccess">

Further enumeration of /etc/sshd/sshd_config showed that the "AllowUsers" parameter was not included, which is why we could not login via SSH with the user admin. However, using the "su" command, we could then switch to the admin user, providing us with access to the user flag.

<img src="https://user-images.githubusercontent.com/58163840/73631278-81e21380-4626-11ea-9a8a-a5b16b39d6cd.png" name="userflag">

<h1>Obtaining root </h1>
Emunerating the system to identify ways to escalate privileges to root, it was found that the system uses the binary "jjs" which can be ran as a privilege user as the set uid bit was on:

<img src="https://user-images.githubusercontent.com/58163840/73631578-64617980-4627-11ea-8359-b57f03e68bf9.png" name="jjs">

By manipulating the file writer in the "jjs" binary as seen in GTFOBins:
https://gtfobins.github.io/gtfobins/jjs/

We can then insert our own public SSH key into the file, so that we can SSH as root into the system.
<img src="https://user-images.githubusercontent.com/58163840/73631984-7bed3200-4628-11ea-9187-2d00c24d8d47.png" name="filewrite">
<img src="https://user-images.githubusercontent.com/58163840/73631993-80b1e600-4628-11ea-9ecf-d71d28f0ba24.png" name="root">

The root flag is then found the root home folder.


                                                                                                                      
                                                                                
