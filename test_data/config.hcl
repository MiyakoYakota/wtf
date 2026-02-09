provider "aws" {
  access_key = "AKIAIOSFODNN7EXAMPLE"
  secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
  region     = "us-east-1"
}

resource "database" "main" {
  host     = "db.example.com"
  username = "admin"
  password = "hcl_db_secret"
  ip       = "10.0.0.100"
}

resource "api" "gateway" {
  url      = "https://api.example.com"
  password = "hcl_api_token"
  domain   = "example.com"
}
