"""STUB: effect not implemented — do not guess mechanics.
Unown [P] (DP5 #33): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="fdf85f2e-a1b8-55fa-97fa-d5388b52e22b",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownP.Name",
    display_name="Unown [P]",
    searchable_by=["Unown [P]", "Basic", "UnownP"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="DP5",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="PUT",
            game_text="Once during your turn (before your attack), if Unown P is on your Bench, you may put 1 damage counter on 1 of your Pok\u00e9mon (excluding any Unown).",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="Each player discards the top card of his or her deck. This attack does 20 damage plus 20 more damage for each Unown discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)