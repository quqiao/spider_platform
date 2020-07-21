from django.test import TestCase

# Create your tests here.

import re
r = "http://www.longyiyy.com/events-589.html"
m = re.findall("\d+", r)
m1 = ''.join(m)
print(m1)