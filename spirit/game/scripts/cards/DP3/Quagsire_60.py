"""STUB: effect not implemented — do not guess mechanics.
Quagsire (DP3 #60): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="d1a643f0-0d94-578d-a17e-58358a3803b9",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name",
    display_name="Quagsire",
    searchable_by=["Quagsire", "Stage 1", "Quagsire"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    family_id=194,
    abilities=[
        Ability(
            title="Aqua Healing",
            game_text="Once during your turn (before your attack), if Quagsire is your Active Pok\u00e9mon and the Defending Pok\u00e9mon has any Water Energy attached to it, you may remove 3 damage counters from Quagsire.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Muddy Water",
            game_text="Does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)