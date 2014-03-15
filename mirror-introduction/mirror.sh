#!/bin/bash

echo "start" `date` >> log
cd /tmp
wget -r -l2 'http://www.strikingly.com/coopist/'
cd -
cd ../www/
rm -rf www.strikingly.com
mv /tmp/www.strikingly.com .
#ln -s www.strikingly.com/coopist coopist
cd -
echo "end" `date` >> log
