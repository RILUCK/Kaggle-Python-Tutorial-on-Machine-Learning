# Passengers that survived vs passengers that passed away
print(train['Survived'].value_counts())

# As proportions
print(train['Survived'].value_counts(normalize = True))

# Males that survived vs males that passed away
print(train['Survived'][train['Sex']=='male'].value_counts())

# Females that survived vs Females that passed away
print(train['Survived'][train['Sex']=='female'].value_counts())

# Normalized male survival
print(train['Survived'][train['Sex']=='male'].value_counts(normalize = True))

# Normalized female survival
print(train['Survived'][train['Sex']=='female'].value_counts(normalize = True))
