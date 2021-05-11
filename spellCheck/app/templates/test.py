from _typeshed import ReadableBuffer
import re

s =  "tối có [] một ( con mèo "
brackets = ReadableBuffer.sub( r'[^(){}[\]]', '', s)
print(brackets)