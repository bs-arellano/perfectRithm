from  pyswip import Prolog
prolog=Prolog()
prolog.consult("solution.pl")
g= prolog.query("getArtistTracks(_,_,TrackNames)")
L=list(g)
print(L)
