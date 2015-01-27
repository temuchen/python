from sys import argv

script,user_name,sex1,sex2=argv
prompt='>'

print "hi %s,I'm the %s script."%(user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?"%user_name
likes=raw_input(prompt)

print "where do you live %s?"%user_name
lives=raw_input(prompt)

print "Are you a %r or %r?"%(sex1,sex2)
sex=raw_input(prompt)

print "what kind of computer do you have?"
computer=raw_input(prompt)

print """
Alright,so you said %r about liking me.
You live in %r. You air a %r.Not sure where that is.
And you have a %r computer. Nice.
"""%(likes,lives,sex,computer)
