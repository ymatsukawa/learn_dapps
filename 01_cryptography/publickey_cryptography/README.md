## Public key cryptography

```
[ original data ] -> encrypt(#public_key) -> decrypt(#private_key) -> [ original data ]
```

* Public key
  * to be shared in public
  * can encrypt original data
* Private key
  * to be kept secret, NEVER in public
  * can decrypt encrypted data
* Both
  * Mathematically linked

## Example

```
# generate mydomain.key with 2048 size
$ openssl genrsa -out mydomain.key 2048

# key includes private and public.
# generate public key from the key
$ openssl rsa -in mydomain.key -pubout -out mydomain_pub.key

# create original data
$ echo "hello this is secret file" > myfile.txt

# and encrypt with public key
$ openss rsautl -in myfile.txt -out myfile.enc -pubin -inkey mydomain_pub.key -encrypt
$ cat myfile.enc
{bin ouput}

# decrypt the encrypted file with private key
$ openssl rsautl -in myfile.enc -out myfile_decrypted.txt -inkey mydomain.key -decrypt
$ cat myfile_decrypted.txt
hello this is secret file
```

## Refs

* thought
  * https://www.tutorialspoint.com/difference-between-private-key-and-public-key
  * https://ssd.eff.org/en/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work
  * https://www.preveil.com/blog/public-and-private-key/
  * https://www.geeksforgeeks.org/difference-between-private-key-and-public-key/
  * https://www.ibm.com/docs/en/ztpf/1.1.0.14?topic=concepts-public-key-cryptography
  * https://www.cloudflare.com/ja-jp/learning/ssl/how-does-public-key-encryption-work/
* implement
  * https://www.digicert.com/kb/ssl-support/openssl-quick-reference-guide.htm
  * https://www.openssl.org/docs/manmaster/man1/openssl-rsautl.html
  * https://gist.github.com/thinkerbot/706137
