Contributed by : Sundaram Agnihotri
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach :

1 : The score for a pair (i,j) is score=values[i]+values[j]+i-j  rewritten as: score=(values[i]+i)+(values[j]-j)

2 : Track the maximum value of (values[i]+i) seen so far, denoted as maxLeftScore

3 : For each index j, calculate the current score as: score=maxLeftScore+(values[j]-j)
Update maxLeftScore to include the current index j as: maxLeftScore=maxLeftScore=max(maxLeftScore,values[j]+j)

int maxScoreSightseeingPair(vector<int>& values) {
    int maxLeftScore = values[0], maxScore = 0;
    for (int i = 1; i < values.size(); i++) {
        maxScore = max(maxScore, maxLeftScore + values[i] - i);
        maxLeftScore = max(maxLeftScore, values[i] + i);
    }
    return maxScore;
}

