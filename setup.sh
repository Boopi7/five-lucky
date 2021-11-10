#!/bin/bash

# Must have a working cardano-cli build
# preferred path: $HOME/.local/bin

# Create main directory
echo "Creating main directory for LuckyFive utilities"
main_dir=$HOME/.luckyfive
mkdir $main_dir

# directory for policy scripts
echo "Creating directory for policy scripts"
mkdir $main_dir/policy

# diretory for payment keys
# TODO: sensitive information, please remove
echo "Creating directory for payment keys"
mkdir $main_dir/payment

# create payment key pair
# TODO

echo "Setup done!"