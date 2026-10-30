"""STUB: effect not implemented — do not guess mechanics.
Unown [?] (DP6 #82): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="21b76a27-7bd2-5a06-8200-a8572810e378",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name",
    display_name="Unown [?]",
    searchable_by=["Unown [?]", "Basic", "Unown"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="?",
            game_text="Once during your turn (before your attack), if Unown ? is on your Bench, you may choose a Pok\u00e9mon in your hand and put it face down. Your opponent guesses a type of that Pok\u00e9mon. Reveal that card. If your opponent guessed wrong, draw a card. Then, put that card back into your hand.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="Discard up to 2 cards from your hand. For each card you discarded, draw a card.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)