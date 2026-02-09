// neo4j credential nodes
CREATE (u:User {email: 'alice@example.com', username: 'alice', password: 'pass123', url: 'https://example.com'})
CREATE (u:User {email: 'bob@example.com', username: 'bob', password: 'secret456'})
CREATE (a:Admin {email: 'admin@corp.net', name: 'Admin User', password: 'admin789', domain: 'corp.net'})
MERGE (s:Service {username: 'svc_account', password: 'svc_pass!', ip: '10.0.0.5', domain: 'internal.net'})
