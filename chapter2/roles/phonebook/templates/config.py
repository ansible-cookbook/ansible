import os

SQLALCHEMY_DATABASE_URI = "mysql://app:{{ rds_admin_pass }}@{{ groups['phonebook_db'][0] }}/phonebook"
SECRET_KEY = os.urandom(32)
