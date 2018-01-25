#include <iostream>
#include <vector>
#include <algorithm>

std::vector < std::vector < int >>
dp_layer(int depth, std::vector < std::vector < int >>&prev_layer)
{
    std::vector < std::vector < int >>joe;
}

double max_bracket(int n, std::vector < std::vector < int >>&prob)
{
    int expected = 0;
    return expected / 100.0;
}

int main()
{
    int n = 0;
    std::cin >> n;

    int numTeams = 1;
    for (int i = 0; i < n; i++) {
	numTeams *= 2;
    }

    std::vector < std::vector < int >>prob(numTeams);
    for (int i = 0; i < numTeams; i++) {
	for (int j = 0; j < numTeams; j++) {
	    prob[i].push_back(0);
	    std::cin >> prob[i][j];
	}
    }

    std::cout << max_bracket(n, prob) << std::endl;

    return 0;
}
