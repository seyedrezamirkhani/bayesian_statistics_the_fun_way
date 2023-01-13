from math import comb


def calc_prob(k, n, p):
    '''calculate probability mass function for binomial distribution'''
    return comb(n, k) * (p**k) * ((1 - p)**(n - k))


def at_least_k(k, n, p):
    '''calculate sum of probabilities for at least k selections from a binomial distribution'''
    s = 0.0
    for x in range(k, n + 1):
        s += calc_prob(x, n, p)
    return s


# calculate probability of getting at least one
# E.T.Jaynes card for 100 bayes bucks
p_1 = at_least_k(1, 100, (0.0072))
print(
    'probability of getting at least one E.T.Jaynes card for 100 bayes bucks is: {:.3f}'
    .format(p_1))

# Exercise 4
p_2 = at_least_k(2, 7, (1 / 5))
print(
    'probability of getting at least two job offers after 7 interviews is: {:.3f}'
    .format(p_2))

# Exercise 5
p_3 = at_least_k(2, 25, (1 / 10))
print(
    'probability of getting at least two job offers after 25 interviews is: {:.3f}'
    .format(p_3))

if ((p_3 / p_2) < 2):
    print(
        'probability of getting two job offers after 25 interviews is not twice as much as doing 7 interviews. Stick with doing 7 interviews'
    )
else:
    print(
        'probability of getting two job offers after 25 interviews is twice as much as doing 7 interviews. Do 25 interviews'
    )
