import numpy as np
import pandas as pd
import re

def clean_genres(df):

    '''
    This is  a function to clean the genre column of a dataframe.
    It takes a dataframe as input and returns a cleaned genre column.
    Parameters:
        df (pd.DataFrame): The input dataframe containing the genre column.
    Returns:
        pd.Series: The cleaned genre column.
    '''
    
    df['corrected'] =df['Genre'] 
    df['corrected']=df['corrected'].str.strip()
    df['corrected']=df['corrected'].str.replace(' - ', '|')
    df['corrected']=df['corrected'].str.replace(' / ', '|')
    df['corrected']=df['corrected'].str.replace('/', '|')
    df['corrected']=df['corrected'].str.replace(' & ', '|')
    df['corrected']=df['corrected'].str.replace(', ', '|')
    df['corrected']=df['corrected'].str.replace('; ', '|')
    df['corrected']=df['corrected'].str.replace('bio-pic', 'biography')
    df['corrected']=df['corrected'].str.replace('biopic', 'biography')
    df['corrected']=df['corrected'].str.replace('biographical', 'biography')
    df['corrected']=df['corrected'].str.replace('biodrama', 'biography')
    df['corrected']=df['corrected'].str.replace('bio-drama', 'biography')
    df['corrected']=df['corrected'].str.replace('biographic', 'biography')
    df['corrected']=df['corrected'].str.replace(' \\(film genre\\)', '')
    df['corrected']=df['corrected'].str.replace('animated','animation')
    df['corrected']=df['corrected'].str.replace('anime','animation')
    df['corrected']=df['corrected'].str.replace('children\'s','children')
    df['corrected']=df['corrected'].str.replace('comedey','comedy')
    df['corrected']=df['corrected'].str.replace('\\[not in citation given\\]','')
    df['corrected']=df['corrected'].str.replace(' set 4,000 years ago in the canadian arctic','')
    df['corrected']=df['corrected'].str.replace('historical','history')
    df['corrected']=df['corrected'].str.replace('romantic','romance')
    df['corrected']=df['corrected'].str.replace('3-d','animation')
    df['corrected']=df['corrected'].str.replace('3d','animation')
    df['corrected']=df['corrected'].str.replace('viacom 18 motion pictures','')
    df['corrected']=df['corrected'].str.replace('sci-fi','science_fiction')
    df['corrected']=df['corrected'].str.replace('ttriller','thriller')
    df['corrected']=df['corrected'].str.replace('.','')
    df['corrected']=df['corrected'].str.replace('based on radio serial','')
    df['corrected']=df['corrected'].str.replace(' on the early years of hitler','war')
    df['corrected']=df['corrected'].str.replace('sci fi','science_fiction')
    df['corrected']=df['corrected'].str.replace('science fiction','science_fiction')
    df['corrected']=df['corrected'].str.replace(' (30min)','')
    df['corrected']=df['corrected'].str.replace('16 mm film','short')
    df['corrected']=df['corrected'].str.replace('\\[140\\]','drama')
    df['corrected']=df['corrected'].str.replace('\\[144\\]','')
    df['corrected']=df['corrected'].str.replace(' for ','')
    df['corrected']=df['corrected'].str.replace('adventures','adventure')
    df['corrected']=df['corrected'].str.replace('kung fu','martial_arts')
    df['corrected']=df['corrected'].str.replace('kung-fu','martial_arts')
    df['corrected']=df['corrected'].str.replace('martial arts','martial_arts')
    df['corrected']=df['corrected'].str.replace('world war ii','war')
    df['corrected']=df['corrected'].str.replace('world war i','war')
    df['corrected']=df['corrected'].str.replace('biography about montreal canadiens star|maurice richard','biography')
    df['corrected']=df['corrected'].str.replace('bholenath df|cinekorn entertainment','')
    df['corrected']=df['corrected'].str.replace(' \\(volleyball\\)','sports')
    df['corrected']=df['corrected'].str.replace('spy film','spy')
    df['corrected']=df['corrected'].str.replace('anthology film','anthology')
    df['corrected']=df['corrected'].str.replace('biography fim','biography')
    df['corrected']=df['corrected'].str.replace('avant-garde','avant_garde')
    df['corrected']=df['corrected'].str.replace('biker film','biker')
    df['corrected']=df['corrected'].str.replace('buddy cop','buddy')
    df['corrected']=df['corrected'].str.replace('buddy film','buddy')
    df['corrected']=df['corrected'].str.replace('comedy 2-reeler','comedy')
    df['corrected']=df['corrected'].str.replace('films','')
    df['corrected']=df['corrected'].str.replace('film','')
    df['corrected']=df['corrected'].str.replace('biography of pioneering american photographer eadweard muybridge','biography')
    df['corrected']=df['corrected'].str.replace('british-german co-production','')
    df['corrected']=df['corrected'].str.replace('bruceploitation','martial_arts')
    df['corrected']=df['corrected'].str.replace('comedy-drama adaptation of the mordecai richler novel','comedy-drama')
    df['corrected']=df['corrected'].str.replace('df by the mob\\|knkspl','')
    df['corrected']=df['corrected'].str.replace('df','')
    df['corrected']=df['corrected'].str.replace('movie','')
    df['corrected']=df['corrected'].str.replace('coming of age','coming_of_age')
    df['corrected']=df['corrected'].str.replace('coming-of-age','coming_of_age')
    df['corrected']=df['corrected'].str.replace('drama about child soldiers','drama')
    df['corrected']=df['corrected'].str.replace('(( based).+)','')
    df['corrected']=df['corrected'].str.replace('(( co-produced).+)','')
    df['corrected']=df['corrected'].str.replace('(( adapted).+)','')
    df['corrected']=df['corrected'].str.replace('(( about).+)','')
    df['corrected']=df['corrected'].str.replace('musical b','musical')
    df['corrected']=df['corrected'].str.replace('animationchildren','animation|children')
    df['corrected']=df['corrected'].str.replace(' period','period')
    df['corrected']=df['corrected'].str.replace('drama loosely','drama')
    df['corrected']=df['corrected'].str.replace(' \\(aquatics|swimming\\)','sports')
    df['corrected']=df['corrected'].str.replace(' \\(aquatics|swimming\\)','sports')
    df['corrected']=df['corrected'].str.replace("yogesh dattatraya gosavi's directorial debut \\[9\\]",'')
    df['corrected']=df['corrected'].str.replace("war-time","war")
    df['corrected']=df['corrected'].str.replace("wartime","war")
    df['corrected']=df['corrected'].str.replace("ww1","war")
    df['corrected']=df['corrected'].str.replace('unknown','')
    df['corrected']=df['corrected'].str.replace("wwii","war")
    df['corrected']=df['corrected'].str.replace('psychological','psycho')
    df['corrected']=df['corrected'].str.replace('rom-coms','romance')
    df['corrected']=df['corrected'].str.replace('true crime','crime')
    df['corrected']=df['corrected'].str.replace('\\|007','spy')
    df['corrected']=df['corrected'].str.replace('slice of life','slice_of_life')
    df['corrected']=df['corrected'].str.replace('computer animation','animation')
    df['corrected']=df['corrected'].str.replace('gun fu','martial_arts')
    df['corrected']=df['corrected'].str.replace('j-horror','horror')
    df['corrected']=df['corrected'].str.replace(' \\(shogi|chess\\)','')
    df['corrected']=df['corrected'].str.replace('afghan war drama','war drama')
    df['corrected']=df['corrected'].str.replace('\\|6 separate stories','')
    df['corrected']=df['corrected'].str.replace(' \\(30min\\)','')
    df['corrected']=df['corrected'].str.replace(' (road bicycle racing)','sports')
    df['corrected']=df['corrected'].str.replace(' v-cinema','')
    df['corrected']=df['corrected'].str.replace('tv miniseries','tv_miniseries')
    df['corrected']=df['corrected'].str.replace('\\|docudrama','\\|documentary|drama')
    df['corrected']=df['corrected'].str.replace(' in animation','|animation')
    df['corrected']=df['corrected'].str.replace('((adaptation).+)','')
    df['corrected']=df['corrected'].str.replace('((adaptated).+)','')
    df['corrected']=df['corrected'].str.replace('((adapted).+)','')
    df['corrected']=df['corrected'].str.replace('(( on ).+)','')
    df['corrected']=df['corrected'].str.replace('american football','sports')
    df['corrected']=df['corrected'].str.replace('dev\\|nusrat jahan','sports')
    df['corrected']=df['corrected'].str.replace('television miniseries','tv_miniseries')
    df['corrected']=df['corrected'].str.replace(' \\(artistic\\)','')
    df['corrected']=df['corrected'].str.replace(' \\|direct-to-dvd','')
    df['corrected']=df['corrected'].str.replace('history dram','history drama')
    df['corrected']=df['corrected'].str.replace('martial art','martial_arts')
    df['corrected']=df['corrected'].str.replace('psycho thriller,','psycho|thriller')
    df['corrected']=df['corrected'].str.replace('\\|1 girl\\|3 suitors','')
    df['corrected']=df['corrected'].str.replace(' \\(road bicycle racing\\)','sports')
    filterE = df['corrected']=="ero"
    df.loc[filterE,'corrected']="adult"
    filterE = df['corrected']=="music"
    df.loc[filterE,'corrected']="musical"
    filterE = df['corrected']=="-"
    df.loc[filterE,'corrected']=''
    filterE = df['corrected']=="comedy–drama"
    df.loc[filterE,'corrected'] = "comedy|drama"
    filterE = df['corrected']=="comedy–horror"
    df.loc[filterE,'corrected'] = "comedy|horror"
    df['corrected']=df['corrected'].str.replace(' ','|')
    df['corrected']=df['corrected'].str.replace(',','|')
    df['corrected']=df['corrected'].str.replace('-','')
    df['corrected']=df['corrected'].str.replace('actionadventure','action|adventure')
    df['corrected']=df['corrected'].str.replace('actioncomedy','action|comedy')
    df['corrected']=df['corrected'].str.replace('actiondrama','action|drama')
    df['corrected']=df['corrected'].str.replace('actionlove','action|love')
    df['corrected']=df['corrected'].str.replace('actionmasala','action|masala')
    df['corrected']=df['corrected'].str.replace('actionchildren','action|children')

    df['corrected']=df['corrected'].str.replace('fantasychildren\\|','fantasy|children')
    df['corrected']=df['corrected'].str.replace('fantasycomedy','fantasy|comedy')
    df['corrected']=df['corrected'].str.replace('fantasyperiod','fantasy|period')
    df['corrected']=df['corrected'].str.replace('cbctv_miniseries','tv_miniseries')
    df['corrected']=df['corrected'].str.replace('dramacomedy','drama|comedy')
    df['corrected']=df['corrected'].str.replace('dramacomedysocial','drama|comedy|social')
    df['corrected']=df['corrected'].str.replace('dramathriller','drama|thriller')
    df['corrected']=df['corrected'].str.replace('comedydrama','comedy|drama')
    df['corrected']=df['corrected'].str.replace('dramathriller','drama|thriller')
    df['corrected']=df['corrected'].str.replace('comedyhorror','comedy|horror')
    df['corrected']=df['corrected'].str.replace('sciencefiction','science_fiction')
    df['corrected']=df['corrected'].str.replace('adventurecomedy','adventure|comedy')
    df['corrected']=df['corrected'].str.replace('animationdrama','animation|drama')
    df['corrected']=df['corrected'].str.replace('\\|\\|','|')
    df['corrected']=df['corrected'].str.replace('muslim','religious')
    df['corrected']=df['corrected'].str.replace('thriler','thriller')
    df['corrected']=df['corrected'].str.replace('crimethriller','crime|thriller')
    df['corrected']=df['corrected'].str.replace('fantay','fantasy')
    df['corrected']=df['corrected'].str.replace('actionthriller','action|thriller')
    df['corrected']=df['corrected'].str.replace('comedysocial','comedy|social')
    df['corrected']=df['corrected'].str.replace('martialarts','martial_arts')
    df['corrected']=df['corrected'].str.replace('\\|\\(children\\|poker\\|karuta\\)','')
    df['corrected']=df['corrected'].str.replace('epichistory','epic|history')

    df['corrected']=df['corrected'].str.replace('erotica','adult')
    df['corrected']=df['corrected'].str.replace('erotic','adult')

    df['corrected']=df['corrected'].str.replace('((\\|produced\\|).+)','')
    df['corrected']=df['corrected'].str.replace('chanbara','chambara')
    df['corrected']=df['corrected'].str.replace('comedythriller','comedy|thriller')
    df['corrected']=df['corrected'].str.replace('biblical','religious')
    df['corrected']=df['corrected'].str.replace('biblical','religious')
    df['corrected']=df['corrected'].str.replace('colour\\|yellow\\|productions\\|eros\\|international','')
    df['corrected']=df['corrected'].str.replace('\\|directtodvd','')
    df['corrected']=df['corrected'].str.replace('liveaction','live|action')
    df['corrected']=df['corrected'].str.replace('melodrama','drama')
    df['corrected']=df['corrected'].str.replace('superheroes','superheroe')
    df['corrected']=df['corrected'].str.replace('gangsterthriller','gangster|thriller')

    df['corrected']=df['corrected'].str.replace('heistcomedy','comedy')
    df['corrected']=df['corrected'].str.replace('heist','action')
    df['corrected']=df['corrected'].str.replace('historic','history')
    df['corrected']=df['corrected'].str.replace('historydisaster','history|disaster')
    df['corrected']=df['corrected'].str.replace('warcomedy','war|comedy')
    df['corrected']=df['corrected'].str.replace('westerncomedy','western|comedy')
    df['corrected']=df['corrected'].str.replace('ancientcostume','costume')
    df['corrected']=df['corrected'].str.replace('computeranimation','animation')
    df['corrected']=df['corrected'].str.replace('dramatic','drama')
    df['corrected']=df['corrected'].str.replace('familya','family')
    df['corrected']=df['corrected'].str.replace('familya','family')
    df['corrected']=df['corrected'].str.replace('dramedy','drama|comedy')
    df['corrected']=df['corrected'].str.replace('dramaa','drama')
    df['corrected']=df['corrected'].str.replace('famil\\|','family')

    df['corrected']=df['corrected'].str.replace('superheroe','superhero')
    df['corrected']=df['corrected'].str.replace('biogtaphy','biography')
    df['corrected']=df['corrected'].str.replace('devotionalbiography','devotional|biography')
    df['corrected']=df['corrected'].str.replace('docufiction','documentary|fiction')

    df['corrected']=df['corrected'].str.replace('familydrama','family|drama')

    df['corrected']=df['corrected'].str.replace('espionage','spy')
    df['corrected']=df['corrected'].str.replace('supeheroes','superhero')
    df['corrected']=df['corrected'].str.replace('romancefiction','romance|fiction')
    df['corrected']=df['corrected'].str.replace('horrorthriller','horror|thriller')

    df['corrected']=df['corrected'].str.replace('suspensethriller','suspense|thriller')
    df['corrected']=df['corrected'].str.replace('musicaliography','musical|biography')
    df['corrected']=df['corrected'].str.replace('triller','thriller')

    df['corrected']=df['corrected'].str.replace('\\|\\(fiction\\)','|fiction')

    df['corrected']=df['corrected'].str.replace('romanceaction','romance|action')
    df['corrected']=df['corrected'].str.replace('romancecomedy','romance|comedy')
    df['corrected']=df['corrected'].str.replace('romancehorror','romance|horror')

    df['corrected']=df['corrected'].str.replace('romcom','romance|comedy')
    df['corrected']=df['corrected'].str.replace('rom\\|com','romance|comedy')
    df['corrected']=df['corrected'].str.replace('satirical','satire')

    df['corrected']=df['corrected'].str.replace('science_fictionchildren','science_fiction|children')
    df['corrected']=df['corrected'].str.replace('homosexual','adult')
    df['corrected']=df['corrected'].str.replace('sexual','adult')

    df['corrected']=df['corrected'].str.replace('mockumentary','documentary')
    df['corrected']=df['corrected'].str.replace('periodic','period')
    df['corrected']=df['corrected'].str.replace('romanctic','romantic')
    df['corrected']=df['corrected'].str.replace('politics','political')
    df['corrected']=df['corrected'].str.replace('samurai','martial_arts')
    df['corrected']=df['corrected'].str.replace('tv_miniseries','series')
    df['corrected']=df['corrected'].str.replace('serial','series')

    filterE = df['corrected']=="musical–comedy"
    df.loc[filterE,'corrected'] = "musical|comedy"

    filterE = df['corrected']=="roman|porno"
    df.loc[filterE,'corrected'] = "adult"


    filterE = df['corrected']=="action—masala"
    df.loc[filterE,'corrected'] = "action|masala"


    filterE = df['corrected']=="horror–thriller"
    df.loc[filterE,'corrected'] = "horror|thriller"

    filterE = df['corrected']=="drama|romance|adult|children"
    df.loc[filterE,'corrected'] = "drama|romance|adult"

    df['corrected']=df['corrected'].str.replace('\\|–\\|','|')
    df['corrected']=df['corrected'].str.strip(to_strip='\\|')
    df['corrected']=df['corrected'].str.replace('actionner','action')
    df['corrected']=df['corrected'].str.strip()
    df['GenreSplit']=df['corrected'].str.split('|')
    df['GenreSplit']= df['GenreSplit'].apply(np.sort).apply(np.unique)
    df['GenreSplit'] = df['GenreSplit'].apply(lambda x: '|'.join(x))
    df['GenreSplit'] = df['GenreSplit'].apply(lambda x: 'NA' if (len(x) == 0 or x[0]==' ' or x[0]=='') else x)

    df['Genre'] = df['GenreSplit']
    df.drop(columns=['corrected','GenreSplit'], inplace=True)

    return df['Genre']