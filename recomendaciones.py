from pyswip import Prolog
prolog = solution.Prolog()
list(prolog.query("getArtistTracks(X,TrackIds,TrackNames)")) == [{'X': 'Adele'}, {'X': 'Sam Smith'}]
for soln in prolog.query("father(X,Y,Z)"):
    print(soln["X"], "is the artist of", soln["Z"])