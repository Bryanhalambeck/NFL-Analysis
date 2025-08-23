## 📂 Dataset: `nfl-data.csv`

For this project, I built a custom dataset (`nfl-data.csv`) covering every NFL team from 2018–2024.  

The following metrics were collected from [Sports Odds History](https://www.sportsoddshistory.com/nfl-regular-season-win-total-results-by-team/):
- **Vegas_OU** – Preseason over/under lines 
- **Actual_Wins** – Final regular season win total

The following metric was collected from [PhillyVoice](https://www.phillyvoice.com/ranking-nfl-teams-age-after-53-man-cutdowns-2024-edition/), which publishes a yearly article, released before the season, that ranks NFL rosters by average age after 53-man cutdowns:
- **Avg_Age** – Preseason roster average age

The following metrics were collected from [Football Outsiders / FTN Fantasy](https://ftnfantasy.com/nfl/2024-dvoa-projections), which publishes a yearly article with preseason DVOA projections (archived via the Wayback Machine for older seasons): 
- **Total_DVOA** – Overall projected team efficiency  
- **Off_DVOA** – Offensive efficiency projection  
- **Def_DVOA** – Defensive efficiency projection  
- **ST_DVOA** – Special teams efficiency projection  
- **Sched%** – Schedule difficulty rating  
- **Mean_Wins** – Average projected win total  
- **No1_Pick_Odds** – Probability of earning the #1 draft pick  
- **Playoff_Odds** – Probability of making the playoffs  
- **SB_Win_Odds** – Probability of winning the Super Bowl  

The following metrics were collected from [Pro-Football-Reference](https://www.pro-football-reference.com/years/2023/index.htm). These values were gathered at the end of the season from 2017–2023 (after the Super Bowl) and then attributed to the following year’s team (e.g., 2017 end-of-season  ratings were used as the 2018 team’s baseline). These represent previous-season performance metrics, not preseason projections.    
- **SOS** – End-of-season strength of schedule rating  
- **SRS** – Overall end-of-season rating combining point differential and schedule strength  
- **OSRS** – Offensive component of SRS  
- **DSRS** – Defensive component of SRS  

The following metrics were collected from [ESPN FPI](https://www.espn.com/nfl/fpi), I captured the preseason FPI ratings for every team as they appeared immediately before the season began (archived via the Wayback Machine for older seasons):  
- **FPI_Total** – Overall team rating (expected point margin per game vs. an average opponent on a neutral field)  
- **FPI_Off** – Offensive component of FPI  
- **FPI_Def** – Defensive component of FPI 

The following metrics were collected from [TeamRankings](https://www.teamrankings.com/nfl/), I gathered end-of-season values (after the Super Bowl) and attributed them to the following season’s team. These represent previous-season performance metrics, not preseason projections.    
- **Luck_Rating** – Measures how much a team’s record was influenced by randomness (e.g., close games, turnovers)  
- **Full_Season_Rating** – Predictive power rating for the team based on the entire season’s performance  
- **Momentum_Rating** – Predictive power rating based on the team’s **last 10 games** of the season  

📌 These metrics provide additional context on team variance, overall strength, and late-season trends that may carry over into the following year.  



