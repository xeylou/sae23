#!/bin/bash

while true; do
   python3 alexis_code/php/files/api_to_db.py
   
   sleep $[60 * 60]
done