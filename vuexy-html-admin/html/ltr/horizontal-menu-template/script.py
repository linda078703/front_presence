import random 

def hjgj():
    lower = 'abcdefghijklmnopqrstvwxyz'
    uppercase='ABCDEFGHIJKMNOPQRSTVWXYZ'
    number='0123456789'
    symbole='()@!$+'
    mdp= lower+uppercase+number+symbole
    md= "".join(random.sample(mdp,k=5))
    print(md)

    return md


hjgj()


