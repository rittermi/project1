#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['COUNT', 'STRANGER', 'LOOK', 'CHURCH', 'CASTLE', 'PICTURE',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['OPEN', 'SILENT', 'STRONG', 'GOOD', 'NARROW', 'NEAR',
              'NEW', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'ANGRY']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', '. ', '. ', '. ', '. ', '. ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[2]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPE', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' NO ', ' EVERY ', '. ', '. ', '. ', '. ', '. ']
operators = ['ANY', 'A CERTAIN', 'ONE', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A APPLE':
        text = 'AN APPLE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[3]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPE', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' NO ', ' EVERY ', '. ', '. ', '. ', '. ', '. ']
operators = ['ANY', 'A CERTAIN', 'ONE', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A APPLE':
        text = 'AN APPLE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[4]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPE', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' NO ', ' EVERY ', '. ', '. ']
operators = ['ANY', 'A CERTAIN', 'ONE', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A APPLE':
        text = 'AN APPLE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[5]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPE', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' NO ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A APPLE':
        text = 'AN APPLE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[6]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPE', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' NOT ', ' EVERY ', '. ', '. ']
operators = ['ANY', 'A CERTAIN', 'ONE', 'A SINGLE']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A APPLE':
        text = 'AN APPLE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[7]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPE', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' NO ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY', 'A']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A APPLE':
        text = 'AN APPLE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[8]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPE', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY', 'A']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A APPLE':
        text = 'AN APPLE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[9]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPE', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY', 'A']

def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'A APPLE':
        text = 'AN APPLE'
    return text + ' IS '

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[10]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPE', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY', 'A']
verb = [' IS ']
def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[11]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY', 'A']
verb = [' IS ']
def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[12]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY', 'A']
verb = [' IS ']
def phrase():
    text = choice(operators) + ' ' + choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[13]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY', 'A']
verb = [' IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[14]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY', 'A']
verb = [' IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[15]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY', 'A']
verb = [' IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[16]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY', 'A']
verb = [' IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(conjunctions() + (phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[17]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY', 'A']
verb = [' IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(conjunctions() + (phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[18]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[19]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[20]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[21]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects) + verb
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + verb

print('')
print((operators() + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[22]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']

def phrase():
    text = choice(subjects) + [' IS ']
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + verb

print('')
print((operators() + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[23]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']

def phrase():
    text = choice(subjects) + [' IS ']
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + verb

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[24]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + verb

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[25]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + verb

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[26]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects) + verb
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + verb

print('')
print((operators() + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[27]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects) + verb
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + verb

print('')
print((operators() + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[28]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(conjunction() + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[29]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(conjunction() + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[30]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(conjunctions() + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[31]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[32]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(opertators) + conjunction() + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[33]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operatators) + conjunction() + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[34]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + conjunction() + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[35]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + choice(conjunction)) + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[36]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + choice(conjunction) + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[37]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + choice(conjunctions) + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[38]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER', 'YOUR', 'HIS', 'MY']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[39]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[40]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[41]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[42]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) +
       phrase() + choice(predicates) + '.')
print('')


# In[43]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[44]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[45]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[46]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[47]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[48]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[49]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[50]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[51]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + choice(verb)

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[52]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[53]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[54]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[55]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[56]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[57]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[58]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[59]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[60]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == ' GRAPES IS ':
        text = ' GRAPES ARE '
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[61]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == ' GRAPES IS ':
        text = ' GRAPES ARE '
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[62]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == ' GRAPES IS ':
        text = ' GRAPES ARE '
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[63]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects) + choice(verb)
    if text == ' GRAPES IS ':
        text = ' GRAPES ARE '
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[64]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = [' IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[65]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[66]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[67]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[68]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[69]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[70]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[71]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[72]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + 'ALWAYS'

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[73]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + 'ALWAYS '

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[74]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text + 'ALWAYS '

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[75]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[76]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[77]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[78]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[79]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[80]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[81]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[82]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[83]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[84]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[85]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[86]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[87]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[88]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[89]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[90]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[91]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[92]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[93]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[94]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[95]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[96]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[97]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[98]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[99]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[100]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')


# In[ ]:


#!/usr/bin/python

# Stochastic Texts, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Theo Lutz, 1959; translation by Helen MacCormack
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

subjects = ['APPLE', 'BANANA', 'LEMON', 'DRAGONFRUIT', 'GRAPEFRUIT', 'LYCHEE',
            'GRAPES', 'RASPBERRY', 'NECTARINE', 'KIWI', 'WATERMELON', 'STRAWBERRY', 'PEAR',
            'MANGO', 'JACKFRUIT', 'STARFRUIT']
predicates = ['ROTTEN', 'SWEET', 'JUICY', 'FUZZY', 'PLUMP', 'RIPE',
              'SOUR', 'TART', 'UNRIPE', 'COLORFUL', 'FRAGRANT', 'FIRM', 'SOFT',
              'HEAVY', 'LIGHT', 'BITTER']
conjunctions = [' THEN ', ' AND ', ' BUT ', '. ', '. ']
operators = ['HER ', 'YOUR ', 'HIS ', 'MY ']
verb = ['IS ']
def phrase():
    text = choice(subjects) + ' ' + choice(verb)
    if text == 'GRAPES IS':
        text = 'GRAPES ARE'
    return text

print('')
print(choice(operators) + phrase() + choice(predicates) + choice(conjunctions) + choice(operators) +
       phrase() + choice(predicates) + '.')
print('')

