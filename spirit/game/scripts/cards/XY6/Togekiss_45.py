"""STUB: effect not implemented — do not guess mechanics.
Togekiss (XY6 #45): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a781d24d-5844-5d8e-96f5-60cc48f96e92",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name",
    display_name="Togekiss",
    searchable_by=["Togekiss", "Stage 2", "Togekiss"],
    subtypes=["Stage 2"],
    collector_number=45,
    set_code="XY6",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    family_id=175,
    abilities=[
        Attack(
            title="Powerful Slap",
            game_text="Flip a coin for each Energy attached to this Pok\u00e9mon. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Aura Sphere",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)