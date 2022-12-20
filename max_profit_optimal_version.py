def maxProfit(cene, k):
    '''Vrne maksimalen dobicek, ki ga lahko ustvarimo
        z nakopom in prodajo dolocene delnice
        z najvec k transakcijami.'''

    st_dni = len(cene)
    
    if st_dni < 2 or k == 0:
        return 0
    
    # k je dovolj velik, da pokrije vse moznosti
    if k >= st_dni / 2:
        return sum(i-j for i, j in zip(cene[1:], cene[:-1]) if i-j > 0)
    
    globalni_dobicek = [0]*st_dni
    for j in range(k):
        lokalni_dobicek = 0
        for i in range(1,st_dni):
            # kupimo delnico na dan i-1, prodamo delnico na dan i
            profit = cene[i] - cene[i-1]
            # primerjamo lokalni dobicek do dneva i-1 + profit z globalnim dobickom
            # na dan i z j-1 transakcijami.
            lokalni_dobicek = max(lokalni_dobicek+profit, globalni_dobicek[i])
            # primerjamo globalni dobicek na dan i-1 z globalnim dobickom na dan i z j transakcijami
            globalni_dobicek[i] = max(globalni_dobicek[i-1], lokalni_dobicek)

    return globalni_dobicek[-1]

#test
print(maxProfit([3,2,6,5,0,3], 2))
print(maxProfit([2,4,1], 2))
print(maxProfit([3,2,6,1,4,2,6], 2))
print(maxProfit([3,2,6], 2))
print(maxProfit([2,2,6], 2))
print(maxProfit([2,2,2], 2))
print(maxProfit([3,2,6,8], 3))

