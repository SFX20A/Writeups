<h1> Overview </h1>

Mango offered several leaning opportunities on relatively new technologies which is gaining traction in the recent years, being used on multiple platforms. In which, SQL injection is a well-known vulnerability in this day and age, much less know about at NoSQL injection is possible as well.

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

The above request brings out the first user from the database and automatically authenticates him, successfully bringing us to the website development page. 
                                                                                                                      
                                                                                
