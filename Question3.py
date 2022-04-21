import pandas as pd
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
euro12 = pd.read_csv(url, ',')
euro12
euro12.Goals
euro12.Team.count()
discipline = euro12[['Team','Yellow Cards','Red Cards']]
discipline
discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)
discipline['Yellow Cards'].mean()
euro12[euro12.Goals > 6]
euro12[euro12.Team.str.startswith('G')]
euro12.head(7)
euro12.head(13)
euro12.set_index('Team', inplace=True)
euro12
euro12.loc[['England', 'Italy', 'Russia'], 'Shooting Accuracy']