import os
import subprocess
import sqlite3
import hashlib

def dangerous_execution(user_input):
    # CRITICAL: Command injection vulnerability
    os.system("ping -c 4 " + user_input)
    
    # CRITICAL: Command injection via subprocess with shell=True
    subprocess.call(f"ls -l {user_input}", shell=True)

def dangerous_eval(user_data):
    # CRITICAL: Arbitrary code execution
    # Never use eval() on untrusted user input
    return eval(user_data)

def insecure_database(username):
    # HIGH: SQL Injection vulnerability
    # Using string concatenation for SQL queries instead of parameterized queries
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
    return cursor.fetchall()

def bad_crypto():
    # MEDIUM: Using a weak, broken cryptographic hash (MD5)
    m = hashlib.md5()
    m.update(b"sensitive data")
    return m.hexdigest()
    
def hardcoded_secrets():
    # HIGH: Hardcoded credentials in source code
    aws_access_key = "AKIAIOSFODNN7EXAMPLE"
    database_password = "super_secret_password_123!"
    return aws_access_key, database_password

def unsafe_deserialization(payload):
    import pickle
    # CRITICAL: Unsafe deserialization which can lead to code execution
    return pickle.loads(payload)
