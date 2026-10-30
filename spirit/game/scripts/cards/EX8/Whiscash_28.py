"""STUB: effect not implemented — do not guess mechanics.
Whiscash (EX8 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import dwindling_wave, raging_tremble


card = PokemonCardDef(
    guid="3075b264-07b0-55c1-9896-d28de2f2043c",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whiscash.Name",
    display_name="Whiscash",
    searchable_by=["Whiscash", "Stage 1", "Whiscash"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="EX8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name",
    family_id=339,
    abilities=[
        Attack(
            title="Raging Tremble",
            game_text="Flip a coin. If heads, this attack does 10 damage for each damage counter on Whiscash to each Defending Pok\u00e9mon. If tails, this attack does 10 damage for each damage counter on Whiscash to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=raging_tremble(),
        ),
        Attack(
            title="Dwindling Wave",
            game_text="Does 70 damage minus 10 damage for each damage counter on Whiscash.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="-",
            # STUB: attack effect not implemented
            effect=dwindling_wave(),
        ),
    ],
)