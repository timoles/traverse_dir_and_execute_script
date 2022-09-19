#!/usr/bin/env bash
MYPATH=$1
grep -Pon '<script_contents_encoded>(.*?)</script_contents_encoded>' $MYPATH | cut -d '>' -f2 | cut -d '<' -f1 | base64 -d | grep '\-password'
