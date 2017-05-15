import pprint
word = ''' I had sworn I wouldn’t write
another poem about my mom
but in the museum there is a room
filled with centuries-old pottery sherds
and it is difficult not to start seeing
symbols everywhere. We walk through
the frigid air toward a reconstructed
temple, likely stolen, I say, and she
looks at me. A rope keeps us from going
further. Who are you texting? she asks
and I want to scream but don’t.
What question could she ask
that wouldn’t make me bristle?
I once called our fights a kind of dance
in a poem I rightly tore up. I won’t
call it anything I tell myself in the poem
I told myself I wouldn’t write.
I’d change the subject but resistance
is a sign to go forward, I tell my students
because something is wrong with me.
So I go forward into what it might mean
to struggle a few hours with the one
who made me, whose dark I once lived
inside. We step into the centuries
between us and the vessels behind glass
which once held water, grain, and now
the silence of a light so gentle
as to not damage the precious things.'''

dict1 = {}
dict2 = {}
for letter in word.upper():
	dict1.setdefault(letter,0)
	dict1[letter] = dict1[letter] + 1
pprint.pprint(dict1)
for let in range(len(word)):
	sample = word[let:let + 3]
	if 'and' in sample:
		dict2.setdefault(sample,0)
		dict2[sample] = dict2[sample] + 1
pprint.pprint(dict2)


