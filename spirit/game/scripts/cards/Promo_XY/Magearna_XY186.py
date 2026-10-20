"""STUB: effect not implemented — do not guess mechanics.
Magearna (Promo_XY #XY186): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2d3fcf1e-c5a4-5441-a844-6ba3e1a1d6c0",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magearna.Name",
    display_name="Magearna",
    searchable_by=["Magearna", "Basic", "Magearna"],
    subtypes=["Basic"],
    collector_number=186,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=801,
    abilities=[
        Attack(
            title="Entertain",
            game_text="Heal 40 damage from 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Prismatic Wave",
            game_text="This attack does 20 damage times the number of different types of Pok\u00e9mon on your opponent's Bench.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)