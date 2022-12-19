def maxProfit(cene, k):
    '''Vrne maksimalen dobicek, ki ga lahko ustvarimo
        z kupovanjem in pordajanjem dolocene delnice
        z najvec k transakcijami.'''

    st_dni = len(cene)
    
    if st_dni < 2 or k == 0:
        return 0
    
    # k je dovolj velik, da pokrije vse moznosti
    # if k > num_days / 2 -> casovna zahtevnost je O(n)
    if k >= st_dni / 2:
        return sum(i-j for i, j in zip(cene[1:], cene[:-1]) if i-j > 0)
    
    
    # casovna zahtevnost je O(k * n-1)
    globalni_dobicek = [0]*st_dni
    for j in range(k):

        lokalni_dobicek = 0
        for i in range(1,st_dni):
            # Kupimo delnico na dan i-1, prodamo delnico na dan i
            profit = cene[i] - cene[i-1]
            # globalni_dobicek[i] -> primerjam z profitom na i-ti dan z j-1 transakcijami
            # lokalni_dobicek+profit -> delnico prodamo na i-ti dan 
            lokalni_dobicek = max(lokalni_dobicek+profit, globalni_dobicek[i])
            # globalni_dobicek[i-1] -> profit z j transakcijami na i-1 dan
            # lokalni_dobicek -> profit na i-ti dan z j transakcijami
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

