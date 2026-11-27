#To Do List Manager, Final Project. Intro to Programming, Ciara Patch
import time

sleep = time.sleep(0.5)
print(f". {sleep} . {sleep} .")

import asyncio

async def main():
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")

if __name__ == "__main__":
    asyncio.run(main())

#nested dictionary on fleshed out facts: official languages, tourist attractions, culture, food
locations={ #quick base facts that need nested
    "Bologna, Italy": "Kimi Antonelli formula 1 20 year old WDC born here - not capital. Oldest still running university (1088 University of Bologna). UNESCO Porticoes. Discovery of tortellini tied to city. Hidden canals",
    "Barcelona, Spain": "Capital of Spain, 9 UNESCO World Heritage Sites. La Diada de Sant Jordi holiday celebrated on April 23. Catalan and Spanish",
    "Brussels, Belgium": "Capital of Belgium, NATO headquarters. French and Dutch. Census says very international feel with 180+ nationalities and 100+ languages. Airport biggest chocolate sales",
    "Vienna, Austria": "Capital of Austria, population 2 mil and on Danube river. Acts as city and 1 of Austria's 9 federal states. Once the capital of Austro-Hungarian Empire. Oldest zoo (1752) and oldest ferris wheel (1897). Home of Mozart, Beethoven and Schubert",
    "Oslo, Norway": "Capital of Norway, founded around 1048 by King Harald Hardrada but had name changes in 1624 and 1925. Nicknamed Tigerstaden (Tiger City) after poem, 1 of highest electric car rates in world. 6 hours sunlight in winter, 19 hours summer"
           }