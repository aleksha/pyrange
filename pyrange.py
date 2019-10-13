from scipy.interpolate import interp1d
import numpy as np


class material:
    "Material class"
    def __init__(self , name ):
        self.name = name
        if name == "H2":
            data_file = open("Hydrogen.txt", "r")
            T= [] ; R = []
            t = [] ; r = []
            num = 0
            for line in data_file:
                if line[0]!="#" or len(line)<1 :
                    num+=1
                    if num%2 :
                        T.append( float(line[:-1].split("  ")[1]) )
                        R.append( float(line[:-1].split("  ")[6] )/0.0000899 )
                    else:
                        t.append( float(line[:-1].split("  ")[1]) )
                        r.append( float(line[:-1].split("  ")[6] )/0.0000899 )

            TT = np.array(T)
            RR = np.array(R)

            tt = np.array(t[2:-2])
            rr = np.array(r[2:-2])

            f1 = interp1d(TT, RR, kind='linear')
            f2 = interp1d(TT, RR, kind='quadratic')
            f3 = interp1d(tt, rr, kind='cubic')
            self.func = f3
        
