#!/bin/bash

echo  "This is a shellsript file to download an image "

read -p "Do you want to continue download? " prompt

if [ $prompt == Y ] || [ $prompt == y ]
then
  echo "Downloading..."
  wget https://it.wikipedia.org/wiki/File:Atlanta_Zoo_Panda.jpg
  echo "Download complete"
else
  echo "Abort"
fi


