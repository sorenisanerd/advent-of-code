package day19

import (
	"os"

	"github.com/sorenisanerd/adventofcode/utils"
)

type blueprint struct {
	id        int
	robotCost []utils.V
	maxCost   utils.V
	//	ore, clay, obsidian, geode
}

func (bp *blueprint) CalculateMaxCost() {
	bp.maxCost = utils.V{0, 0, 0, 0}
	for i := range bp.robotCost {
		for j := range bp.robotCost[i] {
			bp.maxCost[j] = utils.Max(bp.maxCost[j], bp.robotCost[i][j])
		}
	}
}

func (bp blueprint) timeNeeded(state State) utils.V {
	//	ore, clay, obsidian, geode
	v := utils.V{0, 0, 0, 0}
	for i, rc := range bp.robotCost {
		neededResources := rc.AddV(state.resources.MultInt(-1))
		for j := range neededResources {
			if neededResources[j] > 0 {
				var timeNeeded int

				if state.robots[j] == 0 {
					timeNeeded = 10000
				} else {
					timeNeeded = neededResources[j] / state.robots[j]
					// Poor man's Ceil
					if neededResources[j]%state.robots[j] > 0 {
						timeNeeded++
					}
				}
				v[i] = utils.Max(v[i], timeNeeded)
			}
		}
	}
	return v
}

func loadBlueprints(filename string) []blueprint {
	rv := []blueprint{}
	data := string(utils.Must(os.ReadFile, filename))
	for _, l := range utils.SplitLines(data) {
		ints := utils.ExtractInts(l)
		robotCosts := []utils.V{}
		//	ore, clay, obsidian, geode
		robotCosts = append(robotCosts,
			// ore robot
			utils.V{ints[1], 0, 0, 0},
			// clay robot
			utils.V{ints[2], 0, 0, 0},
			// obsidian robot
			utils.V{ints[3], ints[4], 0, 0},
			// geode robot
			utils.V{ints[5], 0, ints[6], 0})
		bp := blueprint{
			id:        ints[0],
			robotCost: robotCosts,
		}
		bp.CalculateMaxCost()
		rv = append(rv, bp)
	}
	return rv
}

type State struct {
	//	ore, clay, obsidian, geode
	robots    utils.V
	resources utils.V
}

func (s State) Copy() State {
	return State{
		robots:    utils.V{s.robots[0], s.robots[1], s.robots[2], s.robots[3]},
		resources: utils.V{s.resources[0], s.resources[1], s.resources[2], s.resources[3]},
	}

}

func newState() State {
	return State{
		//	ore, clay, obsidian, geode
		robots:    utils.V{1, 0, 0, 0},
		resources: utils.V{0, 0, 0, 0},
	}
}

func dfs(bp blueprint, timeLeft int, state State, ans *int) {
	if timeLeft == 0 {
		return
	}

	// Base case is just hanging out doing nothing until time runs out
	rv := (timeLeft)*state.robots[3] + state.resources[3]

	if rv > *ans {
		*ans = rv
	}

	// What we have:
	absoluteBestCase := state.resources[3]
	// plus what we can produce with our current robots:
	absoluteBestCase += timeLeft * state.robots[3]
	// plus what we could produce if we could continuously
	// churn out more geode robots
	absoluteBestCase += timeLeft * (timeLeft - 1) / 2

	if absoluteBestCase <= *ans {
		return
	}

	timeNeeded := bp.timeNeeded(state)
	for i := len(timeNeeded) - 1; i >= 0; i-- {
		if i < 3 {
			// i == 3 is geode robots and we don't want to limit those,
			// but for all the other ones, we'll cap the number of robots
			// at whichever other robot cost the most of this kind of
			// resource
			if bp.maxCost[i] <= state.robots[i] {
				continue
			}
		}
		if timeNeeded[i] <= (timeLeft - 1) {
			// Let's try building one of these
			robot := utils.V{0, 0, 0, 0}
			robot[i] = 1

			// Copy the state
			newState := state //.Copy()

			// Add the resources the robots will produce in that time
			newState.resources = state.resources.AddV(state.robots.MultInt(timeNeeded[i] + 1))

			// Build the robot
			newState.robots = newState.robots.AddV(robot)

			if newState.robots[i] == state.robots[i] {
				panic("")
			}

			// Remove the resources needed to build the robot
			newState.resources = newState.resources.AddV(bp.robotCost[i].MultInt(-1))

			dfs(bp, timeLeft-timeNeeded[i]-1, newState, ans)
		}
	}
}

func PartA(filename string) int {
	rv := 0
	blueprints := loadBlueprints(filename)
	for _, bp := range blueprints {
		ans := 0
		dfs(bp, 24, newState(), &ans)
		rv += bp.id * ans
	}
	return rv
}

func PartB(filename string) int {
	rv := 1
	blueprints := loadBlueprints(filename)
	for _, bp := range blueprints[:utils.Min(len(blueprints), 3)] {
		ans := 0
		dfs(bp, 32, newState(), &ans)
		rv *= ans
	}
	return rv
}
