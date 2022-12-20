from copy import deepcopy
from time import time

OBS = "obs"
ORE = "ore"
GEO = "geo"
CLAY = "clay"


def find_opportunities(bot_costs, bots, minerals):

    geo_max = (minerals[ORE] // bot_costs[GEO][ORE]
               ) > 0 and (minerals[OBS] // bot_costs[GEO][OBS]) > 0
    obs_max = (minerals[ORE] // bot_costs[OBS][ORE]
               ) > 0 and (minerals[CLAY] // bot_costs[OBS][CLAY]) > 0
    clay_max = (minerals[ORE] // bot_costs[CLAY][ORE]) > 0
    ore_max = (minerals[ORE] // bot_costs[ORE][ORE]) > 0

    opportunities = []
    for geo in range(0, geo_max+1):
        for obs in range(0, obs_max+1):
            for clay in range(0, clay_max+1):
                for ore in range(0, ore_max+1):
                    if (geo+obs+clay+ore) <= 1:  # zero or one bot can be crafted in one round; not two bots
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

                        opp_bots = deepcopy(bots)
                        opp_bots[GEO] += geo
                        opp_bots[OBS] += obs
                        opp_bots[CLAY] += clay
                        opp_bots[ORE] += ore
                        opportunities.append((opp_bots, opp_minerals))
    return opportunities


def simulate(minute, bot_costs, bots, minerals, memo={}):
    k = (minute, tuple(bots.values()), tuple(minerals.values()))  #
    if memo.get(k, None) != None:
        return memo[k]

    # harvest minerals with current bots
    for bot, bot_count in bots.items():
        minerals[bot] += bot_count

    if minute == 24:
        return minerals[GEO]

    if minute == 23 and bots[GEO]==0:
        return 0

    geo_max = 0
    for opp_bots, opp_minerals in find_opportunities(bot_costs, bots, minerals):
        geo_sim = simulate(minute+1, bot_costs, opp_bots, opp_minerals, memo)
        geo_max = max(geo_max, geo_sim)

    #memo[k] = geo_max
    return geo_max


def solve():
    # Blueprint 2:
    #  Each ore robot costs 2 ore.
    #  Each clay robot costs 3 ore.
    #  Each obsidian robot costs 3 ore and 8 clay.
    #  Each geode robot costs 3 ore and 12 obsidian.
    bot_costs = {"ore":  {"ore": 2},
                 "clay": {"ore": 3},
                 "obs":  {"ore": 3, "clay": 8},
                 "geo":  {"ore": 3, "obs": 12}}

    bots = {"ore": 1,
            "clay": 0,
            "obs": 0,
            "geo": 0}

    minerals = {"ore": 0,
                "clay": 0,
                "obs": 0,
                "geo": 0}

    res = simulate(1, bot_costs, bots, minerals)
    print(f"Solution 1 ... {res}")


start = time()
solve()
print(f"{time()-start:>4} sec")
