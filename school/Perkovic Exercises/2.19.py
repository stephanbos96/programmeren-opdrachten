answers = ['Y', 'N', 'N', 'Y', 'N','Y', 'Y', 'Y', 'N', 'N', 'N']

numYes = answers.count('Y')
numNo = answers.count('N')
percentYes = numYes / (numYes + numNo) * 100
answers.sort()
f = answers[6]
print(answers.index('Y'))
