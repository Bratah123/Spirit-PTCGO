"""STUB: effect not implemented — do not guess mechanics.
Unown [V] (DP6 #79): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import dp5_torterra_30_earthquake


card = PokemonCardDef(
    guid="61039d44-3ae7-591d-a294-715f4f711a92",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownV.Name",
    display_name="Unown [V]",
    searchable_by=["Unown [V]", "Basic", "UnownV"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="VACATION",
            game_text="Once during your turn (before your attack), you may remove 2 damage counters from each of your Pok\u00e9mon. If you do, your turn ends. This power can't be used if Unown V is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="Does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=dp5_torterra_30_earthquake(),
        ),
    ],
)