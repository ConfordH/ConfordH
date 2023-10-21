import pandas as pd

print('part A \n')
#reading the file as csv
DataSet = pd.read_csv('assignment.csv');


#Normalizing dataframe
DataSet.dropna(how='all', axis=1, inplace=True)
DataSet = DataSet.dropna(how='all')


#part a, sum of missing values for each collumn
print('sum of missing values \n',DataSet.isnull().sum())
print('\n')
#part b, number of duplicate recordes

print('part B \n')
print('number of duplicate values \n',DataSet.duplicated().sum())
print('\n')
#part c,
print('part C')
Alive = []
Dead = []
Missing = []
Compared = []
Seedlings= []
Index= []
first = 0
second = 0
third = 0
fourth = 0
thisComp =[]
lastList=[];
lastListind=[];
sum_Cir1 = 0;
sum_Cir_1 = 0;
for idx, row in DataSet.iterrows():
    lastvar = row['gps_difference'];
    if lastvar >150:
        lastList.append(row['gps_difference'])
        lastListind.append(idx)
    Alive.append(row['cycle_1_alive'])
    Dead.append(row['cycle_1_dead'])
    Missing.append(row['cycle_1_missing'])
    Index.append(idx)
    Seedlings.append(row['Seedlings_Planted'])
    compnum = row['cycle_1_alive']+row['cycle_1_dead']+row['cycle_1_missing']
    compnum = row['Seedlings_Planted'] - compnum
    
    thisComp.append(compnum)
    if compnum >= 0:
        sum_Cir1 = sum_Cir1 + compnum
        if compnum >= 10:
            compnum = '> +10'
            Compared.append(compnum)
        else:
            compnum = '< +10'
            Compared.append(compnum)
        
        
    else:
        sum_Cir_1 = sum_Cir_1 + compnum
        if compnum >= 10:
            compnum = '> -10'
            Compared.append(compnum)
        else:
            compnum = '< -10'
            Compared.append(compnum)
            
    if pd.isna(DataSet.cycle_1_alive[idx]) == False:
        first = first + DataSet.cycle_1_alive[idx]
      
    if pd.isna(DataSet.cycle_1_dead[idx]) == False:
        second= second + DataSet.cycle_1_dead[idx]
    
    if pd.isna(DataSet.cycle_1_missing[idx]) == False:
        third = third + DataSet.cycle_1_missing[idx]
    
    if pd.isna(DataSet.Seedlings_Planted[idx]) == False:
        fourth= fourth+ DataSet.Seedlings_Planted[idx]
    
data={'Index':Index,'Seedlings':Seedlings,'Alive':Alive,'Dead':Dead,'Missing':Missing,'Compared':Compared}
Compared_df=pd.DataFrame(data)
print(Compared_df)
print('Total Alive',first)
print('Total Dead',second)
print('Total Missing',third)
print('Total Planted',fourth)

#part D
print('\n')
print('part D')
zAlive = []
zDead = []
zMissing = []
zCompared = []
zSeedlings= []
zIndex= []
zfirst = 0
zsecond = 0
zthird = 0
zfourth = 0
zthisComp = []
sum_Cir2=0
sum_Cir_2=0
for zidx, row in DataSet.iterrows():
    zAlive.append(row['cycle_2_alive'])
    zDead.append(row['cycle_2_dead'])
    zMissing.append(row['cycle_2_missing'])
    zIndex.append(zidx)
    zSeedlings.append(row['Seedlings_Planted'])
    zcompnum = row['cycle_2_alive']+row['cycle_2_dead']+row['cycle_2_missing']
    zcompnum = row['Seedlings_Planted'] - zcompnum
    zthisComp.append(zcompnum)
    
    if zcompnum >= 0:
        sum_Cir2 = sum_Cir2 + zcompnum
        if zcompnum >= 10:
            zcompnum = '> +10'
            zCompared.append(zcompnum)
        else:
            zcompnum = '< +10'
            zCompared.append(zcompnum)
    else:
        sum_Cir_2 = sum_Cir_2 + zcompnum
        if zcompnum >= 10:
            zcompnum = '> -10'
            zCompared.append(zcompnum)
        else:
            zcompnum = '< -10'
            zCompared.append(zcompnum)
            
    if pd.isna(DataSet.cycle_2_alive[zidx]) == False:
        zfirst = zfirst + DataSet.cycle_2_alive[zidx]
      
    if pd.isna(DataSet.cycle_2_dead[zidx]) == False:
        zsecond= zsecond + DataSet.cycle_2_dead[zidx]
    
    if pd.isna(DataSet.cycle_2_missing[zidx]) == False:
        zthird = zthird + DataSet.cycle_2_missing[zidx]
    
    if pd.isna(DataSet.Seedlings_Planted[zidx]) == False:
        zfourth= zfourth+ DataSet.Seedlings_Planted[zidx]
    
zdata={'Index':zIndex,'Seedlings':zSeedlings,'Alive':zAlive,'Dead':zDead,'Missing':zMissing,'Compared':zCompared}
zCompared_df=pd.DataFrame(zdata)
print(zCompared_df)
print('Total Alive',zfirst)
print('Total Dead',zsecond)
print('Total Missing',zthird)
print('Total Planted',zfourth)

#part E

print('\n')
print('part E \n')
print('Circle 1 report, for greater than +10',sum_Cir1)
print('Circle 2 report, for greater than +10',sum_Cir2)
print('Circle 1 report, for greater than -10',sum_Cir_1)
print('Circle 2 report, for greater than -10',sum_Cir_2)

print('\n')
sumCir1 = sum_Cir1 + sum_Cir_1
sumCir2 = sum_Cir2 + sum_Cir_2

sumBothCir = sumCir1 - sumCir2

if sumBothCir > 0:
    if sumBothCir >10:
        print('Circle 1 report greater than Circle 2 report by >+10')
    
    else:
        print('Circle 1 report greater than Circle 2 report by <+10')
        
else:
    
    if sumBothCir > -10:
        print('Circle 1 report less than Circle 2 report by <-10')
    
    else:
        print('Circle 1 report less than Circle 2 report by >-10')
        

print('\n')
#part f cycle 2 GPS greater than 150 m

print('part F \n')
z2data={'Index':lastListind,'gps':lastList}
z2df = pd.DataFrame(z2data)
print(z2df)

print('\n')

DataSet['Campared_Val_Cir1'] = Compared_df['Compared']
DataSet['Campared_Val_Cir2'] = zCompared_df['Compared']

print('question 2')
print('this is the new dataset containing errors of compared cycle values for both cycles \n',' \n',DataSet)

