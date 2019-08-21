#!/bin/sh

cd build
cmake ../
make
if [ -e nqueen ]
then
    ./nqueen
fi