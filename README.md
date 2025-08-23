## 📂 Dataset: `nfl-analysis-data.csv`

For this project, I built a custom dataset (`nfl-data.csv`) covering every NFL team from **2018–2024**.  

---

### Sports Odds History  
Collected from [Sports Odds History](https://www.sportsoddshistory.com/nfl-regular-season-win-total-results-by-team/).
- **Vegas_OU** – Preseason over/under lines  
- **Actual_Wins** – Final regular season win total  

---

### PhillyVoice  
Collected from [PhillyVoice](https://www.phillyvoice.com/ranking-nfl-teams-age-after-53-man-cutdowns-2024-edition/), which publishes a yearly article, released before the season, that ranks NFL rosters by average age after 53-man cutdowns. 
- **Avg_Age** – Preseason roster average age  

---

### Football Outsiders / FTN Fantasy  
Collected from [Football Outsiders / FTN Fantasy](https://ftnfantasy.com/nfl/2024-dvoa-projections), which publishes a yearly article with preseason DVOA projections (archived via the Wayback Machine for older seasons).
- **Total_DVOA** – Overall projected team efficiency  
- **Off_DVOA** – Offensive efficiency projection  
- **Def_DVOA** – Defensive efficiency projection  
- **ST_DVOA** – Special teams efficiency projection  
- **Sched%** – Schedule difficulty rating  
- **Mean_Wins** – Average projected win total  
- **No1_Pick_Odds** – Probability of earning the #1 draft pick  
- **Playoff_Odds** – Probability of making the playoffs  
- **SB_Win_Odds** – Probability of winning the Super Bowl  

---

### Pro-Football-Reference  
Collected from [Pro-Football-Reference](https://www.pro-football-reference.com/years/2023/index.htm). These values were gathered at the end of the season from **2017–2023** (after the Super Bowl) and then attributed to the following year’s team (e.g., 2017 end-of-season ratings were used as the 2018 team’s baseline). These represent **previous-season performance metrics**, not preseason projections.
- **SOS** – End-of-season strength of schedule rating  
- **SRS** – Overall end-of-season rating combining point differential and schedule strength  
- **OSRS** – Offensive component of SRS  
- **DSRS** – Defensive component of SRS  

---

### ESPN FPI  
Collected from [ESPN FPI](https://www.espn.com/nfl/fpi). I captured the preseason FPI ratings for every team as they appeared immediately before the season began (archived via the Wayback Machine for older seasons). 
- **FPI_Total** – Overall team rating (expected point margin per game vs. an average opponent on a neutral field)  
- **FPI_Off** – Offensive component of FPI  
- **FPI_Def** – Defensive component of FPI  

---

### TeamRankings  
Collected from [TeamRankings](https://www.teamrankings.com/nfl/). I gathered end-of-season values (after the Super Bowl) and attributed them to the following season’s team. These represent **previous-season performance metrics**, not preseason projections.  
- **Luck_Rating** – Measures how much a team was influenced by luck  
- **Full_Season_Rating** – Based on TeamRankings’ predictive power rating, rating for the team based on the entire season’s performance  
- **Momentum_Rating** – Based on TeamRankings’ last 10 games rating, reflecting team performance over the final 10 games of the season  
