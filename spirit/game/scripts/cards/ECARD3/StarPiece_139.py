from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import star_piece_between_turns


card = PokemonToolCardDef(
    guid="2dd3e3fd-7057-5a31-9a5b-db28082522d8",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StarPiece.Name",
    display_name="Star Piece",
    searchable_by=["Star Piece", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=139,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Star Piece",
            game_text="At any time between turns, if the Pokémon this card is attached to is Benched and has 2 or more damage counters on it, search your deck for an Evolution card that Pokémon evolves into and put it on top of that Pokémon. (This counts as evolving that Pokémon.) Shuffle your deck afterward. Then, discard Star Piece.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=star_piece_between_turns,
        ),
    ],
)
