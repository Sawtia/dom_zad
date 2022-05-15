winter = ['1','2','12']
spring = ['3','4','5']
summer = ['6','7','8']
autumn = ['9','10','11']
season = {'winter' : winter, 'spring' : spring, 'autumn ':autumn, 'summer' : summer}
q = input('witch month?')
for key in season:
    if q in ','.join(season[key]):
        print(key)
        break