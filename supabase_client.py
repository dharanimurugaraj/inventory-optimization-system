from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("https://syaoktqtqhknbysrfrsz.supabase.co")
key = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN5YW9rdHF0cWhrbmJ5c3JmcnN6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ1NjMwNDksImV4cCI6MjA2MDEzOTA0OX0.FRffXGKn86pjlg9w6fBBZQhcVLyhdLsm6-pxzQj7c48")

print(f"SUPABASE_URL: {url}")
print(f"SUPABASE_KEY: {key}")

supabase = create_client(url, key)
