"""STUB: effect not implemented — do not guess mechanics.
Shedinja (EX3 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import wonder_guard_passive, damage_curse

card = PokemonCardDef(
    guid="c985a9ad-7317-52cf-a6fc-46de3c4d3774",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja", "Stage 1", "Shedinja"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="EX3",
    rarity=Rarities.RareHolo,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Wonder Guard",
            game_text="Prevent all effects of attacks, including damage, done to Shedinja by your opponent's Evolved Pok\u00e9mon and Pok\u00e9mon-ex.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=wonder_guard_passive(),
        ),
        Attack(
            title="Damage Curse",
            game_text="Put 1 damage counter, plus 1 more damage counter for each damage counter on Shedinja, on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=damage_curse(),
        ),
    ],
)