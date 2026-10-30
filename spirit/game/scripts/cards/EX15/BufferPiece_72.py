from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers
from spirit.game.attributes import AbilityTypes, Rarities
from spirit.game.card_effects.ex import BufferPiecePassive, buffer_piece_discard_end_opponent_turn

card = PokemonToolCardDef(
    guid="2156c9b9-71dd-5cc2-a75f-abff81a01197",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BufferPiece.Name",
    display_name="Buffer Piece",
    searchable_by=["Buffer Piece", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=72,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    passive=BufferPiecePassive(),
    granted_abilities=[
        Ability(
            title="Buffer Piece",
            game_text="At the end of your opponent's turn after you played Buffer Piece, discard Buffer Piece.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=buffer_piece_discard_end_opponent_turn(
                "2156c9b9-71dd-5cc2-a75f-abff81a01197"),
        ),
    ],
)
