from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import BufferPiecePassive

card = PokemonToolCardDef(
    guid="5ffa0469-3da3-5699-8e4a-1e3091973dfa",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BufferPiece.Name",
    display_name="Buffer Piece",
    searchable_by=["Buffer Piece", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=83,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    passive=BufferPiecePassive(),
)
