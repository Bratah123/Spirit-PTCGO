from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers
from spirit.game.attributes import AbilityTypes, Rarities
from spirit.game.card_effects.ex import BufferPiecePassive, buffer_piece_discard_end_opponent_turn

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
    granted_abilities=[
        Ability(
            title="Buffer Piece",
            game_text="At the end of your opponent's turn after you played Buffer Piece, discard Buffer Piece.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=buffer_piece_discard_end_opponent_turn(
                "5ffa0469-3da3-5699-8e4a-1e3091973dfa"),
        ),
    ],
)
