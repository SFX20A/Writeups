<h1> Overview </h1>
Postman is a typical box with relatively straightforward vulnerabilities which can be identified on the get-go.
The box is similar to what OSCP students would expect when it comes to the certification exam.

The vulnerabiltiies exploited in this box are as follows:
<ol type="1">
  <li>Redis Exploitation</li>
  <li>Webmin Vulnerability</li>
</ol>

<h1> Discovery </h1>
Using a standard nmap command, using default scripts and enumerating versions, resulted in the following output:

<img src="https://user-images.githubusercontent.com/58163840/73636846-d8eee500-4634-11ea-90b7-3ce3471248d2.png" name="nmap">

By observing the nmap output, there are 2 possible exploitable vulnerabilities. Namely Redis and Webmin. As the Webmin vulnerability possibly requires credentials, we first set our sights on exploiting redis to obtain user access.

<h1> Obtaining User </h1>
The redis exploit was discovered in 2019, whereby any unauthenticated user can write its public key into the redis home directory using the redis cli, thus obtaining SSH access.
More information can be found here: 
https://medium.com/@knownsec404team/rce-exploits-of-redis-based-on-master-slave-replication-ef7a664ce1d0

By adding our public key into the redis ssh directory, we obtained ssh access.

<img src="https://user-images.githubusercontent.com/58163840/73633911-e0f75680-462d-11ea-859a-31b9f5e8276d.png" name="redis">
<img src="https://user-images.githubusercontent.com/58163840/73633928-ebb1eb80-462d-11ea-8381-354fa1fca50b.png" name="sshredis"

Examining the history of the redis user, we identified 2 crucial information about the system. This user can su to user "Matt" and there is an id_rsa.bak file which can possibly be the ssh key for user Matt.
By running a find command, we then found the id_rsa.bak file at the /opt folder:
<img src="https://user-images.githubusercontent.com/58163840/73633937-efde0900-462d-11ea-9a94-714ccf92cb1a.png" name="history">
<img src="https://user-images.githubusercontent.com/58163840/73633945-f5d3ea00-462d-11ea-88d4-6ce05952ab6e.png" name="history2">
<img src="https://user-images.githubusercontent.com/58163840/73636781-b5c43580-4634-11ea-98ff-f9101e4df312.png" name="obtainkey">

By using ssh2john to extract the key and using john to extract the passphrase to the ssh key, this passphrase was found to be reused as the password for user "Matt" where we were then able to gain user access as Matt.
<img src="https://user-images.githubusercontent.com/58163840/73636787-bbba1680-4634-11ea-8586-319bb9225172.png" name="ssh2john">
<img src="https://user-images.githubusercontent.com/58163840/73636804-c5437e80-4634-11ea-9100-d7854b7726fb.png" name="suMatt">

The user flag is then found in Matt's home folder.

<h1> Obtaining Root </h1>

As we have obtained the username and password for Matt, we can then exploit the webmin vulnerability, as seen below:

<img src="https://user-images.githubusercontent.com/58163840/73636812-cd032300-4634-11ea-9815-6e34b5716a44.png" name="options">
<img src="https://user-images.githubusercontent.com/58163840/73636841-d5f3f480-4634-11ea-92fd-f41a3a64feb9.png" name="exploit">

The root flag is found in the root home folder.

