#!/usr/bin/python


import logging
import sys
import pkgutil


modules = {}
scores = {}
payoff = [[(3,3), (0,5)], [(5,0), (0,0)]]

def getImplementations(dirname):
    for importer, package_name, _  in pkgutil.iter_modules([dirname]):
        full_package_name = '%s.%s' % (dirname, package_name)
        if full_package_name not in sys.modules:
            module = importer.find_module(package_name).load_module(full_package_name)
            modules[package_name] = module
            print module




def runGames():
    for name in modules.keys():
        scores[name] = 0

    for name1,module1 in modules.iteritems():
        for name2, module2 in modules.iteritems():
            #logging.debug( "Game between {} and {}".format(name1, name2))

            previousChoice1 = previousChoice2 = None
            previousPayoff1 = previousPayoff2 = None
            gameScore1 = gameScore2 = 0
            for step in range(0, 1000):
                currentChoice1 = module1.play(previousChoice2, previousPayoff1)
                currentChoice2 = module2.play(previousChoice1, previousPayoff2)

                score = payoff[currentChoice1][currentChoice2]
                #logging.debug("Game {} Choices {}, {}, Scores {}".format(step, currentChoice1, currentChoice2, score))
                previousChoice1, previousChoice2 = currentChoice1, currentChoice2
                previousPayoff1 = score[0]
                previousPayoff2 = score[1]
                gameScore1 = gameScore1 + score[0]
                gameScore2 = gameScore2 + score[1]
                scores[name1] = scores[name1] + score[0]
                scores[name2] = scores[name2] + score[1]
            logging.debug( "Game between {} and {}: Scores {}, {}".format(name1, name2, gameScore1, gameScore2))


def printResults():
    sortedScores =  reversed(sorted(scores.items(), key=lambda p:p[1]))
    print '-------------------------'
    for item in sortedScores:
        print item[0], item[1]


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    logging.info("Starting up")
    getImplementations('implementations')
    runGames()
    printResults()

