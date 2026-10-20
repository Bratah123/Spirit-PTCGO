"""STUB: effect not implemented — do not guess mechanics.
Yveltal-EX (Promo_XY #XY08): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1e73e8b6-8f1e-5fa1-89d2-bd9a417573f7",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.YveltalEX.Name",
    display_name="Yveltal-EX",
    searchable_by=["Yveltal-EX", "Basic", "EX", "YveltalEX"],
    subtypes=["Basic", "EX"],
    collector_number=8,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=717,
    abilities=[
        Attack(
            title="Evil Ball",
            game_text="This attack does 20 more damage times the amount of Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Y Cyclone",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)