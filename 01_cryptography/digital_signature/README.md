## digital signing

```
[Sender]

* data
* private key
* public key


[Receiver]

* public key of Sender
```

```
[Sender]
#data -> hash function -> hash
hash -> (signature algorithm with private key) -> #signature

-> send #data and #signature

[Receiver]
#data -> hashing function -> #HASH
#signature -> (verification algorithm with Sender's public key) -> #_HASH_

verifies #HASH equals #_HASH_
```

* Sender
  * create
    * `hash` by `data`
    * `signature` by `hash` and `sender's private key` with `signature algorithm`
  * send
    * `data` and `signature`
* Receiver
  * create
    * `hash` by `hashing function` from `data`
    * `sig_hash` by `verification alogirthm` from `signature` and `Sender's public key`
  * verify
    * `hash` equals `sig_hash`

## remarks

signing hash is more efficient than hashing the entire data

## implements

```
# [Sign]
# create private key
$ openssl genrsa -out mysign.key
# create PEM public key
$ openssl rsa -in mysign.key -outform PEM -pubout -out mysign_pub.pem

# create raw data
$ echo "hello my signed data world" > data.txt

# hash data itself
$ openssl dgst -sha256 data.txt > hash_sha256
# create signature from hash with private key
$ openssl dgst -sha256 -sign mysign.key -out mysignature.sig data.txt

# [Verify]
$ openssl dgst -sha256 -verify mysign_pub.pem  -signature mysignature.sig data.txt
Verified OK
```

* https://www.tutorialspoint.com/cryptography/cryptography_digital_signatures.htm
* https://jumpnowtek.com/security/Code-signing-with-openssl.html
* https://stackoverflow.com/questions/10782826/digital-signature-for-a-file-using-openssl
* https://stackoverflow.com/questions/10782826/digital-signature-for-a-file-using-openssl/10783033#10783033
