
## 📂 Dataset: `nfl-data.csv`

For this project, I built a custom dataset (`nfl-data.csv`) covering every NFL team from 2018–2024.  
The goal was to capture both **preseason expectations** and **end-of-season outcomes** so I could measure which teams over- or underperformed.

The following metrics were collected from [Sports Odds History](https://www.sportsoddshistory.com/nfl-regular-season-win-total-results-by-team/):

- **Vegas_OU** – Preseason over/under lines 
- **Actual_Wins** – Final regular season win total

The following metric was collected from [PhillyVoice](https://www.phillyvoice.com/ranking-nfl-teams-age-after-53-man-cutdowns-2024-edition/), which publishes a yearly article ranking NFL rosters by average age after 53-man cutdowns:

- **Avg_Age** – Roster average age

The following metrics were collected from [Football Outsiders / FTN Fantasy](https://ftnfantasy.com/nfl/2024-dvoa-projections),  
which publishes a yearly article with **preseason DVOA projections** (archived via the Wayback Machine for older seasons).  

- **Total_DVOA** – Overall projected team efficiency  
- **Off_DVOA** – Offensive efficiency projection  
- **Def_DVOA** – Defensive efficiency projection  
- **ST_DVOA** – Special teams efficiency projection  
- **Sched%** – Schedule difficulty rating  
- **Mean_Wins** – Average projected win total  
- **No1_Pick_Odds** – Probability of earning the #1 draft pick  
- **Playoff_Odds** – Probability of making the playoffs  
- **SB_Win_Odds** – Probability of winning the Super Bowl  

The following metrics were collected from [Pro-Football-Reference](https://www.pro-football-reference.com/years/2023/index.htm):  

- **Strength of Schedule (`SOS`)** – End-of-season strength of schedule rating  
- **Simple Rating System (`SRS`)** – Overall end-of-season rating combining point differential and schedule strength  
- **Offensive SRS (`OSRS`)** – Offensive component of SRS  
- **Defensive SRS (`DSRS`)** – Defensive component of SRS  

These values were gathered for each season from **2017–2023** and then attributed to the following year’s team record (e.g., 2017 end-of-season ratings were used as the 2018 team’s baseline).  
This ensures the columns represent **last season’s final performance metrics**, not preseason projections.  

### **3. Preseason FPI Ratings**

Collected from [ESPN FPI](https://www.espn.com/nfl/fpi), with archived snapshots accessed via the **Wayback Machine** for each season:  

For every year **2018 through 2024**, I captured the **preseason FPI ratings** for every team as they appeared immediately before the season began.  

- **`FPI_Total`** – Overall team rating (expected point margin per game vs. an average opponent on a neutral field)  
- **`FPI_Off`** – Offensive component of FPI  
- **`FPI_Def`** – Defensive component of FPI  

📌 These values represent **preseason expectations** from ESPN’s analytics model, aligned with the same timing as Vegas and DVOA projections.  

### **4. TeamRankings Metrics**

Collected from [TeamRankings](https://www.teamrankings.com/nfl/):  

For every year **2018 through 2024**, I gathered end-of-season values (recorded after the Super Bowl) and attributed them to the **following season’s team record**, ensuring they reflect a team’s most recent performance baseline heading into the next year.  

- **`Luck_Rating`** – Measures how much a team’s record was influenced by randomness (e.g., close games, turnovers)  
- **`Full_Season_Rating`** – Predictive power rating for the team based on the entire season’s performance  
- **`Momentum_Rating`** – Predictive power rating based on the team’s **last 10 games** of the season  

📌 These metrics provide additional context on team variance, overall strength, and late-season trends that may carry over into the following year.  



