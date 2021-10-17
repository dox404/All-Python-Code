text=('''According to a recent McAfee survey,
in 2020 we turned to digital alternatives
for our favorite in-person activities,
which increased our exposure to potential
cyberthreads, like phishing and fraud.
''')
word="McAfee"
if word in text:
    print(f'yes they are taking about {word}')
else:
    print(f"they are not taliking about {word}")


