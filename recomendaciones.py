from pyswip import Prolog
prolog = solution.Prolog()
list(prolog.query("getArtistTracks(X,TrackIds,TrackNames)")) == [{'X': 'Adele'}, {'X': 'Sam Smith'}]
for soln in prolog.query("getArtistTracks(X,Y,Z)"):
    print(soln["X"], "is the artist of", soln["Z"])
def public recomendado(artist){
	print(list(prolog.query("getArtistTracks(X,TrackIds,TrackNames)")) == [{'X': artist}]);
}