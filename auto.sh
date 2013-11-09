#!/bin/bash

echo "crawl"
python crawler.py coopist
echo "render"
python render.py coopist

echo "crawl"
python crawler.py hkfood
echo "render"
python render.py hkfood
