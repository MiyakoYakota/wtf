### TODOs

##### Warning: AI Generated Formatting & Content Ahead

#### - `parsers/stealer_logs.py`

* [ ] Fingerprint file names by hash for quicker processing

  * Add logic to fingerprint file names via hash. This will significantly improve processing times by referencing files via unique identifiers.
* [ ] Update to use `ir.Record()` for yielding returns

  * Refactor the existing code to utilize `ir.Record()` for yielding the results in a structured format. This will standardize outputs and improve code maintainability.
* [x] Logins

  * See commit [0830612](https://github.com/MiyakoYakota/wtf/commit/08306127900aadf6109b62aa0133d1eb5a6a49d3) for the completed implementation.
* [ ] Discord Token

  * Implement parsing logic for extracting Discord tokens from logs. These may be found in specific sections of the logs and need to be captured with proper validation.
* [ ] Machine Information

  * Add a section to extract machine information (OS, hostname, architecture) from logs. This will help correlate events with specific environments.

---

#### - `parsers/csv.py`

* [x] Colon Delimiter

  * Implemented support for colon-delimited CSV files, improving parsing versatility.

* [x] SV Detection Before Using Delimiter

  * Improved speed by detecting the delimiter first, reducing unnecessary checks and optimizing parsing.

  *(Note: Although this feature wasn't used initially, the code has been retained for future enhancements.)*

---

#### - `parsers/pgp.py`

* [x] Implement `get_itr`

  * Successfully integrated the `get_itr` method for better handling of PGP data iteration.

* [x] Follow `ir/record.py` fields
  * Adjusted the parser to adhere to the `ir.Record()` structure, ensuring consistency and improved data management.

* [x] Add More Data to be Pulled
  * [x] Time of Creation: Captured the timestamp of PGP key creation.
  * [x] Subkeys: Included parsing logic for handling PGP subkeys.
  * [x] Signers: Extracted signers associated with the PGP data for enhanced cryptographic traceability.

---

### - `parsers/json.py`
 
 * [ ] Non-structured JSON Extraction 

   * Add support for nd-json that's been pretty-printed ({data}\n{data})


### TODO – Unimplemented Parsers

* [ ] [HTTP Access Logs](/test_data/access.log)
* [ ] [Bitwarden Export (CSV)](/test_data/bitwarden.csv)
* [ ] [Certificate DER](/test_data/cert.der)
* [ ] [Combo Email/Password (TXT)](/test_data/combo_email_pass.txt)
* [ ] [Configuration HCL](/test_data/config.hcl)
* [ ] [CouchDB JSON](/test_data/couchdb.json)
* [ ] [BSON Data](/test_data/data.bson)
* [ ] [INI Configuration](/test_data/data.ini)
* [ ] [MessagePack Data](/test_data/data.msgpack)
* [ ] [Excel Data](/test_data/data.xlsx)
* [ ] [Docker Config JSON](/test_data/docker_config.json)
* [ ] [Oracle Dump SQL](/test_data/dump_oracle.sql)
* [ ] [Firebase JSON](/test_data/firebase.json)
* [ ] [Cypher Query Graph](/test_data/graph.cypher)
* [ ] [Hashlist Salted (TXT)](/test_data/hashlist_salt.txt)
* [ ] [InfluxDB LP Data](/test_data/influxdb.lp)
* [ ] [Keyring ASC](/test_data/keyring.asc)
* [ ] [Thrift Message](/test_data/message.thrift)
* [ ] [Password File (TXT)](/test_data/passwd.txt)
* [ ] [Safari CSV](/test_data/safari.csv)
* [ ] [Syslog (TXT)](/test_data/syslog.txt)
* [ ] [Authorized Keys](/test_data/authorized_keys)
* [ ] [Bitwarden JSON](/test_data/bitwarden.json)
* [ ] [Certificate PEM](/test_data/cert.pem)
* [ ] [Combo Extended (TXT)](/test_data/combo_extended.txt)
* [ ] [Configuration Plist](/test_data/config.plist)
* [ ] [SQLite Database (Creds)](/test_data/creds.sqlite)
* [ ] [CBOR Data](/test_data/data.cbor)
* [ ] [JSON Data](/test_data/data.json)
* [ ] [Parquet Data](/test_data/data.parquet)
* [ ] [YAML Data](/test_data/data.yaml)
* [ ] [Redis Dump RDB](/test_data/dump.rdb)
* [ ] [Postgres Dump SQL](/test_data/dump_postgres.sql)
* [ ] [Firefox JSON](/test_data/firefox.json)
* [ ] [Hashcat Potfile](/test_data/hashcat.pot)
* [ ] [Hashlist User (TXT)](/test_data/hashlist_user.txt)
* [ ] [Journal JSON](/test_data/journal.json)
* [ ] [Kerberos Keytab](/test_data/krb5.keytab)
* [ ] [Nested JSON](/test_data/nested.json)
* [ ] [Passwords (TXT)](/test_data/passwords.txt)
* [ ] [Sample Torrent](/test_data/sample.torrent)
* [ ] [Telegram JSON](/test_data/telegram.json)
* [ ] [AWS Credentials (TXT)](/test_data/aws_credentials.txt)
* [ ] [Bundle P12](/test_data/bundle.p12)
* [ ] [Chrome CSV](/test_data/chrome.csv)
* [ ] [Combo User/Pass (TXT)](/test_data/combo_user_pass.txt)
* [ ] [Contacts VCF](/test_data/contacts.vcf)
* [ ] [Cryptographic Hashes (TXT)](/test_data/crypt_hashes.txt)
* [ ] [CSV Data](/test_data/data.csv)
* [ ] [JSONL Data](/test_data/data.jsonl)
* [ ] [TOML Data](/test_data/data.toml)
* [ ] [LDIF Directory](/test_data/directory.ldif)
* [ ] [MSSQL Dump SQL](/test_data/dump_mssql.sql)
* [ ] [DynamoDB JSON](/test_data/dynamodb.json)
* [ ] [Firestore JSONL](/test_data/firestore.jsonl)
* [ ] [Hashes RT](/test_data/hashes.rt)
* [ ] [HTPasswd (TXT)](/test_data/htpasswd.txt)
* [ ] [JTR Potfile](/test_data/jtr.pot)
* [ ] [LastPass CSV](/test_data/lastpass.csv)
* [ ] [1Password CSV](/test_data/onepassword.csv)
* [ ] [Plaintext Data (TXT)](/test_data/plaintext.txt)
* [ ] [Security EVTX](/test_data/security.evtx)
* [ ] [WiFi Profile XML](/test_data/wifi_profile.xml)
* [ ] [Base64 Credentials (TXT)](/test_data/base64creds.txt)
* [ ] [Cassandra CQL](/test_data/cassandra_cql.txt)
* [ ] [Chrome Logins SQLite](/test_data/chrome_logins.sqlite)
* [ ] [Combo User/Pass URL (TXT)](/test_data/combo_user_pass_url.txt)
* [ ] [Cookies (TXT)](/test_data/cookies.txt)
* [ ] [Avro Data](/test_data/data.avro)
* [ ] [Environment Data (ENV)](/test_data/data.env)
* [ ] [JWT Data](/test_data/data.jwt)
* [ ] [TSV Data](/test_data/data.tsv)
* [ ] [Discord JSON](/test_data/discord.json)
* [ ] [MySQL Dump SQL](/test_data/dump_mysql.sql)
* [ ] [Ethereum Keystore JSON](/test_data/ethereum_keystore.json)
* [ ] [Generic XML](/test_data/generic.xml)
* [ ] [Hashlist Plain (TXT)](/test_data/hashlist_plain.txt)
* [ ] [RSA Private Key (PEM)](/test_data/id_rsa.pem)
* [ ] [KeePass Export XML](/test_data/keepass_export.xml)
* [ ] [Message PB](/test_data/message.pb)
* [ ] [OpenVPN Config](/test_data/openvpn.ovpn)
* [ ] [Redis AOF](/test_data/redis.aof)
* [ ] [Shadow File (TXT)](/test_data/shadow.txt)
* [ ] [WireGuard Config](/test_data/wireguard.conf)
