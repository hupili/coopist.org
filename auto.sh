#!/bin/bash

echo "crawl"
python crawler.py coopist
echo "render"
python render.py coopist
