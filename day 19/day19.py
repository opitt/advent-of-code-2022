from copy import deepcopy

OBS = "obs"
ORE = "ore"
GEO = "geo"
CLAY = "clay"

def find_opportunities(bots, minerals):
    bot_costs = {"ore":  {"ore": 4},
                "clay": {"ore": 2},
                "obs":  {"ore": 3, "clay": 14},
                "geo":  {"ore": 2, "obs": 7}}

    geo_max  = min(minerals[ORE] // bot_costs[GEO][ORE], 
                   minerals[OBS] // bot_costs[GEO][OBS])
    obs_max  = min(minerals[ORE] // bot_costs[OBS][ORE],
                   minerals[CLAY] // bot_costs[OBS][CLAY])
    clay_max =     minerals[ORE] // bot_costs[CLAY][ORE]
    ore_max  =     minerals[ORE] // bot_costs[ORE][ORE]

    opportunities = []
    for geo in range(0,geo_max+1):
        for obs in range(0, obs_max+1):
            for clay in range(0, clay_max+1):
                for ore in range(0, ore_max+1):
                    opp_minerals = deepcopy(minerals)
                    # geo bot cost
                    opp_minerals[ORE] -= geo * bot_costs[GEO][ORE]
                    opp_minerals[OBS] -= geo * bot_costs[GEO][OBS]
                    # obs bot cost
                    opp_minerals[ORE] -= obs * bot_costs[OBS][ORE]
                    opp_minerals[CLAY] -= obs * bot_costs[OBS][CLAY]
                    # clay bot cost
                    opp_minerals[ORE] -= clay * bot_costs[CLAY][ORE]
                    # ore bot cost
                    opp_minerals[ORE] -= ore * bot_costs[ORE][ORE]

                    if min(opp_minerals.values())>=0:
                        #only valid combinations
                        opp_bots = deepcopy(bots)
                        opp_bots[GEO] += geo
                        opp_bots[OBS] += obs
                        opp_bots[CLAY] += clay
                        opp_bots[ORE] += ore
                        opportunities.append((opp_bots,opp_minerals))
    return opportunities


def simulate(minute, bots, minerals, memo={}):
#    print(f"({minute}) bots({bots.values()}) minerals({minerals.values()})")
    
    k = (tuple(bots.values()), tuple(minerals.values()), minute)
    if memo.get(k, None) != None:
        return memo[k]

    # harvest minerals with current bots
    for bot, bot_count in bots.items():
        minerals[bot] += bot_count

    if minute == 24:
        return minerals[GEO]
    
    geo_max = 0
    for opp_bots, opp_minerals in find_opportunities(bots, minerals):        
        geo_sim = simulate(minute+1, opp_bots, opp_minerals, memo)
        geo_max = max(geo_max, geo_sim)

    memo[k] = geo_max
    return geo_max    


def solve():
    bots = {"ore": 1,
            "clay": 0,
            "obs": 0,
            "geo": 0}

    minerals = {"ore": 0,
                "clay": 0,
                "obs": 0,
                "geo": 0}

    res = simulate(1, bots, minerals)
    print(f"Solution 1 ... {res}")

solve()
