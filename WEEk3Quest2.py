def answer_two():
    energy = pd.read_excel('Energy Indicators.xls')
    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    GDP = pd.read_csv('world_bank.csv')
    k3 = energy.count().sum()
    del energy['Unnamed: 0']
    del energy['Unnamed: 1']
    energy = energy.drop(energy.index[0:16])
    energy = energy.drop(energy.index[243:])
    energy = energy.reset_index()
    del energy['index']
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy =energy.drop(energy.index[227:243])
    
    energy = energy.replace('...', np.nan)

    energy['Country'][214] = 'United Kingdom'
    energy['Country'][216] = 'United States'
    energy['Country'][43] = 'Hong Kong'
    energy['Country'][24] = 'Bolivia'
    energy['Country'][58] = 'Denmark'
    energy['Country'][70] = 'Falkland Islands'
    energy['Country'][44] = 'China, Macao Special Administrative Region'
    energy['Country'][42] = 'China'
    energy['Country'][97] = 'Indonesia'
    energy['Country'][98] = 'Iran'
    energy['Country'][103] = 'Italy'
    energy['Country'][105] = 'Japan'
    energy['Country'][111] = 'Kuwait'
    energy['Country'][143] = 'Netherlands'
    energy['Country'][133] = 'Micronesia'
    energy['Country'][161] = 'Portugal'
    energy['Country'][177] = 'Saudi Arabia'
    energy['Country'][179] = 'Serbia'
    energy['Country'][183] = 'Sint Maarten'
    energy['Country'][190] = 'Spain'
    energy['Country'][197] = 'Switzerland'
    energy['Country'][212] = 'Ukraine'
    energy['Country'][221] = 'Venezuela'
    energy['Country'][11] = 'Australia'
    energy['Country'][73] = 'France'
    energy['Country'][164] = 'South Korea'

    
    GDP = GDP.drop(GDP.index[0 : 4])
    
    GDP = GDP.rename(columns = {'Data Source':'Country'})
    GDP = GDP.reset_index()
    GDP['Country'][97] = 'Hong Kong'
    GDP['Country'][123] = 'South Korea'
    GDP['Country'][109] = 'Iran'
    GDP = GDP[['Country','Unnamed: 50','Unnamed: 51','Unnamed: 52','Unnamed: 53','Unnamed: 54','Unnamed: 55','Unnamed: 56','Unnamed: 57','Unnamed: 58','Unnamed: 59']]
    GDP.columns = ['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
    #ScimEn = ScimEn.drop(ScimEn.index[15:])
   

    

    merge1 = pd.merge(ScimEn,energy,on = 'Country',how = 'outer')
    merge2 = pd.merge(merge1,GDP,on = 'Country',how = 'outer')
    
    #print(len(merge2))
    merge2 = merge2.set_index('Country')
    
    merge3 = pd.merge(ScimEn,energy,on = 'Country',how = 'inner')
    merge4 = pd.merge(merge3,GDP,on = 'Country',how = 'inner')
    merge4 = merge4.set_index('Country')

   
    return len(merge2.index) - len(merge4.index)

answer_two()
