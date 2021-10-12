
:- [artists, albums, tracks].


getArtistTracks(ArtistName,TrackIds,TrackNames) :-
	artist(ArtistName, _, AlbumIds),
	findall(TrackId, (member(X1,AlbumIds),album(X1,_,_,X2),member(TrackId,X2)), TrackIds),
	findall(TrackName, (member(X3,TrackIds), track(X3,TrackName,_,_,_)), TrackNames).


