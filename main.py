# /run.py
import os
from dotenv import load_dotenv, find_dotenv

from application import main

if __name__ == '__main__':
  port = os.getenv('PORT')
  # run app
  main.run(host='0.0.0.0', port=port)
