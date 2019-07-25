from models import Pet
def seed_data():

    sD = Pet(name="Small Dogs",difficulty="hard",food="dry or wet commercial dog food",need1="often need to be walked", need2="need to be spayed or nutered")
    lD = Pet(name="Large Dogs",difficulty="hard",food="dry or wet commercial dog food",need1="certain small dogs need to be groomed constantly",need2="need to be spayed or nutered")
    cat = Pet(name="Cats",difficulty="hard",food="dry or wet commercial cat food",need1="need some kind of toy to scratch or play with",need2="need to be spayed or nutered")
    mice = Pet(name="Mice",difficulty="easy",food="commercial mouse food, and small portions of non citrus fruits and vegtables",need1="need an excersize wheel, and bedding")
    cS= Pet(name="Corn Snakes",difficulty="medium",food="frozen thawed mice",need1="needs a heat lamp")
    gF = Pet(name="Goldfish",difficulty="easy",food="commercial goldfish flakes",need1="need a water filter and change water constantly")


    sD.put()
    lD.put()
    cat.put()
    mice.put()
    cS.put()
    gF.put()
