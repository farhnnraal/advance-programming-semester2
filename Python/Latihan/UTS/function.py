def alphabetScore(numberScore):
    if numberScore >= 80:
        return 'A'
    elif numberScore >= 75 and numberScore < 80:
        return 'A-'
    elif numberScore >= 70 and numberScore < 75:
        return 'B+'
    elif numberScore >= 65 and numberScore < 70:
        return 'B'
    elif numberScore >= 60 and numberScore < 65:
        return 'B-'
    elif numberScore >= 55 and numberScore < 60:
        return 'C+'
    elif numberScore >= 50 and numberScore < 55:
        return 'C'
    elif numberScore >= 45 and numberScore < 50:
        return 'C-'
    elif numberScore >= 40 and numberScore < 45:
        return 'D+'
    elif numberScore >= 35 and numberScore < 40:
        return 'D'
    elif numberScore >= 30 and numberScore < 35:
        return 'D-'
    else:
        return 'E'

def weightDefinition(aplhaScore):
    if aplhaScore == 'A':
        return 4.0
    elif aplhaScore == 'A-':
        return 3.7
    elif aplhaScore == 'B+':
        return 3.5
    elif aplhaScore == 'B':
        return 3.3
    elif aplhaScore == 'B-':
        return 3.0
    elif aplhaScore == 'C+':
        return 2.7
    elif aplhaScore == 'C':
        return 2.5
    elif aplhaScore == 'C-':
        return 2.3
    elif aplhaScore == 'D+':
        return 2.0
    elif aplhaScore == 'D':
        return 1.7
    elif aplhaScore == 'D-':
        return 1.5
    elif aplhaScore == 'E':
        return 1.3
def weightScore(weight_definition, sks):
    weight = weightDefinition(weight_definition)
    
    return weight * sks

def qualityScore(sks, weightScore):
    if weightScore == 0:
        return 0.0
    else:
        return weightScore * sks