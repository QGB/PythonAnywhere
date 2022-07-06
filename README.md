# PythonAnywhere
PythonAnywhere  internal stuff

```
(2,
 19,
 'total 0\n'
 'dr-x------ 2 qgbk registered_users  0 Jul  6 03:21 .\n'
 'dr-xr-xr-x 9 qgbk registered_users  0 Jul  6 03:21 ..\n'
 'lr-x------ 1 qgbk registered_users 64 Jul  6 03:21 0 -> /dev/null\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 1 -> socket:[3661584]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 10 -> socket:[3673120]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 11 -> socket:[3678315]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 12 -> socket:[3673122]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 13 -> socket:[3678316]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 14 -> socket:[3678317]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 15 -> anon_inode:[eventpoll]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 16 -> anon_inode:[eventpoll]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 17 -> anon_inode:[eventpoll]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 18 -> socket:[3789198]\n'
 'lr-x------ 1 qgbk registered_users 64 Jul  6 03:27 19 -> pipe:[3789199]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 2 -> socket:[3661584]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 3 -> socket:[3660800]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 4 -> socket:[3678314]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 424 -> socket:[3665838]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 5 -> /dev/null\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 6 -> socket:[3661583]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 7 -> socket:[3661584]\n'
 'lrwx------ 1 qgbk registered_users 64 Jul  6 03:21 8 -> socket:[3673095]\n'
 'l-wx------ 1 qgbk registered_users 64 Jul  6 03:21 9 -> /dev/null\n')


curl -vvvik -H 'Host:consoles-19.pythonanywhere.com' https://127.0.0.1:443   /sj/info

* Uses proxy env variable no_proxy == 'localhost,127.0.0.1,localaddress,.localdomain.com,/var/run/docker.sock'
*   Trying 127.0.0.1:443...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server did not agree to a protocol
* Server certificate:
*  subject: CN=*.pythonanywhere.com
*  start date: Feb 16 00:00:00 2021 GMT
*  expire date: Mar 18 23:59:59 2022 GMT
*  issuer: C=GB; ST=Greater Manchester; L=Salford; O=Sectigo Limited; CN=Sectigo RSA Domain Validation Secure Server CA
*  SSL certificate verify result: certificate has expired (10), continuing anyway.
> GET /sj/info HTTP/1.1
> Host:consoles-19.pythonanywhere.com
> User-Agent: curl/7.68.0
> Accept: */*
> 
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
HTTP/1.1 200 OK
< Server: TornadoServer/4.5.3
Server: TornadoServer/4.5.3
< Content-Type: application/json; charset=UTF-8
Content-Type: application/json; charset=UTF-8
< Date: Wed, 06 Jul 2022 16:46:18 GMT
Date: Wed, 06 Jul 2022 16:46:18 GMT
< Access-Control-Allow-Origin: *
Access-Control-Allow-Origin: *
< Access-Control-Allow-Credentials: true
Access-Control-Allow-Credentials: true
< Cache-Control: no-store, no-cache, must-revalidate, max-age=0
Cache-Control: no-store, no-cache, must-revalidate, max-age=0
< Etag: "91f719d14eed4164e944c877bfc4a523ce94cc72"
Etag: "91f719d14eed4164e944c877bfc4a523ce94cc72"
< Content-Length: 87
Content-Length: 87

< 
* Connection #0 to host 127.0.0.1 left intact
{"websocket":true,"cookie_needed":true,"origins":["*:*"],"entropy":2520243235425503629}
=======================================================

 2022-07-06__16.46.18__.363 127.0.0.1:8000
* Uses proxy env variable no_proxy == 'localhost,127.0.0.1,localaddress,.localdomain.com,/var/run/docker.sock'
*   Trying 127.0.0.1:8000...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8000 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384
* ALPN, server accepted to use http/1.1
* Server certificate:
*  subject: C=GB; ST=Some-State; L=London; O=PythonAnywhere LLP; CN=PythonAnywhere
*  start date: Sep 16 16:59:49 2014 GMT
*  expire date: Jun 30 16:59:49 2288 GMT
*  issuer: C=GB; ST=Some-State; L=London; O=PythonAnywhere LLP; CN=PythonAnywhere
*  SSL certificate verify result: self signed certificate (18), continuing anyway.
> GET /sj/info HTTP/1.1
> Host:consoles-19.pythonanywhere.com
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 401 Unauthorized
HTTP/1.1 401 Unauthorized
< Server: openresty/1.15.8.3
Server: openresty/1.15.8.3
< Date: Wed, 06 Jul 2022 16:46:18 GMT
Date: Wed, 06 Jul 2022 16:46:18 GMT
< Content-Type: text/html
Content-Type: text/html
< Content-Length: 185
Content-Length: 185
< Connection: keep-alive
Connection: keep-alive
< WWW-Authenticate: Basic realm="Restricted"
WWW-Authenticate: Basic realm="Restricted"

< 
<html>
<head><title>401 Authorization Required</title></head>
<body>
<center><h1>401 Authorization Required</h1></center>
<hr><center>openresty/1.15.8.3</center>
</body>
</html>
* Connection #0 to host 127.0.0.1 left intact

===============
 2022-07-06__16.46.18__.389 127.0.0.1:11300
* Uses proxy env variable no_proxy == 'localhost,127.0.0.1,localaddress,.localdomain.com,/var/run/docker.sock'
*   Trying 127.0.0.1:11300...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 11300 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* error:1408F10B:SSL routines:ssl3_get_record:wrong version number
* Closing connection 0
curl: (35) error:1408F10B:SSL routines:ssl3_get_record:wrong version number




```


