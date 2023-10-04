# Hex Chess (hex_chess)

This is a Python (pygame) GUI source project that allows two players to play hex chess in a window

!!! GAME IS CURRENTLY PLAYABLE !!!

# What is Hex Chess

You've played normal chess, with 64 squares, 8 pawns, various special pieces that you try to checkmate the opponents King.

This is the same but on a Hexagonal board, where there are now 9 pawns, 3 bishops, pieces can move in up to 6 directions (rather than 4)

All the special rules of checking, checkmating, promoting, etc are here

Note: Castling is not allowed!

# Design

A screen of height*width is represented with x, y cartesian coords - this is overlayed with a 6 sided hexagon board

HexTiles have their own coordinate system of q, r, s - to which a HexTile AND a piece on said Tile can work out through this system where it is, and where it wants to go

## Pieces
- Kings can move 1 in any direction, e.g. the 6 tiles around their edges + the 6 tiles 'pointed' to by their HexTiles' corners
- Queens can do all that a King can do i.e. 'in any direction' - but ARENT limited to 1 HexTile move
- Bishops can move along their HexTiles' corners for as long as they can go
- Rooks (Castles) can move in any 'Edge' direction for as long as their are HexTiles
- Knights move in the L shape, but go 2 HexTiles in an Edge direction, then left or right in an Edge direction
- Pawns can only move in a straight line (up or down the board). They can double move on their first go though

# Limitations
- All pieces move, but DONT understand 'in check' or 'checkmate'
- Pawns cant PROMOTE
- Pawns cant en passant
- Maybe 80% of a HexTile is registered via a click (Game will return none if it cant find it)

## TODO
- Re-use the 'step' once code across pawn, king, knight
- Re-use the 'kick stepping' code across rook, bishop, queen
- Add a check for 'in check'
- Add a check if in checkmate, player wins
- ~~Add the ability for a Pawn to be Promoted~~
- Add the ability for a Pawn to En passant 
- log what pieces a piece took
- log turn and piece moves
- add a pieces value back in (e.g. pawn=1, queen=9?)
- starting position
- current position
- last position
- need to have a list of pieces a player has

# Links
- https://www.redblobgames.com/grids/hexagons/
- https://en.wikipedia.org/wiki/Root_system
- https://levelup.gitconnected.com/chess-python-ca4532c7f5a4