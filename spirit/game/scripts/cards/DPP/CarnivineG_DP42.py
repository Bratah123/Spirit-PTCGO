"""STUB: effect not implemented — do not guess mechanics.
Carnivine G (DPP #DP42): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2aff0171-638d-5ddc-85c7-7ec0218f8d60",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CarnivineG.Name",
    display_name="Carnivine G",
    searchable_by=["Carnivine G", "Basic", "SP", "CarnivineG"],
    subtypes=["Basic", "SP"],
    collector_number=42,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=455,
    abilities=[
        Attack(
            title="Power Whip",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage for each Energy attached to Carnivine G to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Grass Knot",
            game_text="Does 20 damage plus 10 more damage for each Colorless Energy in the Defending Pok\u00e9mon's Retreat Cost (after applying effects to the Retreat Cost).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)