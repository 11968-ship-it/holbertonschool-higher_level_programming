#!/usr/bin/python3
print(int.__doc__[:6] + '-' + type.__doc__[:8] + ' ' +
      str.__doc__[:11] + ' ' + list.__doc__[:11] + ' ' +
      type.__name__)
