#!/usr/bin/bash
source ./venv/bin/activate
python3 delete_oldest_indices.py
deactivate

schmiddim/delete-old-elastic-indices