from yatzy import Yatzy


def testChanceScoresSumOfAllDice():
    assert Yatzy.chance(1, 1, 3, 3, 6) == 14

def testChanceScoresSumOfAllDice2():
    assert Yatzy.chance(4, 5, 5, 6, 1) == 21


def testYatzyScores50WhenAllDiceEqual():
    assert Yatzy.yatzy([1, 1, 1, 1, 1]) == 50

def testYatzyScores50WithSixes():
    assert Yatzy.yatzy([6, 6, 6, 6, 6]) == 50

def testYatzyScores0WhenNotAllEqual():
    assert Yatzy.yatzy([1, 1, 1, 2, 1]) == 0


def testOnesScoressumOfOnes():
    assert Yatzy.ones(1, 1, 2, 4, 4) == 2

def testOnesScores0WhenNoOnes():
    assert Yatzy.ones(3, 3, 3, 4, 5) == 0

def testOnesScoresSingleOne():
    assert Yatzy.ones(1, 2, 3, 4, 5) == 1


def testTwosScoresSumOfTwos():
    assert Yatzy.twos(2, 3, 2, 5, 1) == 4

def testTwosScores0WhenNoTwos():
    assert Yatzy.twos(1, 3, 3, 4, 5) == 0


def testThreesScoresSumOfThrees():
    assert Yatzy.threes(3, 3, 3, 4, 5) == 9

def testThreesScores0WhenNoThrees():
    assert Yatzy.threes(1, 2, 4, 4, 5) == 0


def testFoursScoresSumOfFours():
    y = Yatzy(1, 1, 2, 4, 4)
    assert y.fours() == 8

def testFoursScores0WhenNoFours():
    y = Yatzy(1, 2, 3, 5, 6)
    assert y.fours() == 0


def testFivesScoresSumOfFives():
    y = Yatzy(5, 6, 5, 5, 2)
    assert y.fives() == 15

def testFivesScores0WhenNoFives():
    y = Yatzy(1, 2, 3, 4, 6)
    assert y.fives() == 0


def testSixesScoresSumOfSixes():
    y = Yatzy(1, 6, 3, 6, 5)
    assert y.sixes() == 12

def testSixesScores0WhenNoSixes():
    y = Yatzy(1, 2, 3, 4, 5)
    assert y.sixes() == 0


def testPairScores0WhenNoPair():
    assert Yatzy.score_pair(1, 2, 3, 4, 5) == 0

def testPairScoresHighestPairWhenTwoPairs():
    assert Yatzy.score_pair(3, 3, 3, 4, 4) == 8

def testPairScoresHighestPair():
    assert Yatzy.score_pair(1, 1, 6, 2, 6) == 12

def testPairScoresWhenThreeOfAKind():
    assert Yatzy.score_pair(3, 3, 3, 4, 1) == 6

def testPairScoresWhenFourOfAKind():
    assert Yatzy.score_pair(3, 3, 3, 3, 1) == 6


def testTwoPairScoresSumOfTwoPairs():
    assert Yatzy.two_pair(1, 1, 2, 3, 3) == 8

def testTwoPairScores0WhenOnePair():
    assert Yatzy.two_pair(1, 1, 2, 3, 4) == 0

def testTwoPairWithThreeOfAKind():
    assert Yatzy.two_pair(1, 1, 2, 2, 2) == 6

def testTwoPairScores0WhenFourOfAKind():
    assert Yatzy.two_pair(3, 3, 3, 3, 1) == 0


def testThreeOfAKindScoresSum():
    assert Yatzy.three_of_a_kind(3, 3, 3, 4, 5) == 9

def testThreeOfAKindScores0WhenOnlyPair():
    assert Yatzy.three_of_a_kind(3, 3, 4, 5, 6) == 0

def testThreeOfAKindWithFourOfAKind():
    assert Yatzy.three_of_a_kind(3, 3, 3, 3, 1) == 9


def testFourOfAKindScoresSum():
    assert Yatzy.four_of_a_kind(2, 2, 2, 2, 5) == 8

def testFourOfAKindScores0WhenOnlyThree():
    assert Yatzy.four_of_a_kind(2, 2, 2, 5, 5) == 0

def testFourOfAKindWithFiveOfAKind():
    assert Yatzy.four_of_a_kind(2, 2, 2, 2, 2) == 8


def testSmallStraightScores15():
    assert Yatzy.smallStraight(1, 2, 3, 4, 5) == 15

def testSmallStraightScores15Unordered():
    assert Yatzy.smallStraight(2, 3, 4, 5, 1) == 15

def testSmallStraightScores0WhenNotStraight():
    assert Yatzy.smallStraight(1, 2, 2, 4, 5) == 0

def testSmallStraightScores0ForLargeStraight():
    assert Yatzy.smallStraight(2, 3, 4, 5, 6) == 0


def testLargeStraightScores20():
    assert Yatzy.largeStraight(2, 3, 4, 5, 6) == 20

def testLargeStraightScores20Unordered():
    assert Yatzy.largeStraight(6, 2, 3, 4, 5) == 20

def testLargeStraightScores0WhenNotStraight():
    assert Yatzy.largeStraight(1, 2, 3, 4, 5) == 0


def testFullHouseScoresSumOfAllDice():
    assert Yatzy.fullHouse(1, 1, 2, 2, 2) == 8

def testFullHouseScores0WhenTwoPairs():
    assert Yatzy.fullHouse(2, 2, 3, 3, 4) == 0

def testFullHouseScores0WhenFiveOfAKind():
    assert Yatzy.fullHouse(4, 4, 4, 4, 4) == 0

def testFullHouseAnotherValidCase():
    assert Yatzy.fullHouse(6, 6, 6, 2, 2) == 22

#HOLI PROFEEE