"""STUB: effect not implemented — do not guess mechanics.
M Charizard-EX (TwentiethAnn #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6ccebbb1-7d1e-50a3-960f-a58b9a0d72f3",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MCharizardEX.Name",
    display_name="M Charizard-EX",
    searchable_by=["M Charizard-EX", "MEGA", "EX", "MCharizardEX"],
    subtypes=["MEGA", "EX"],
    collector_number=12,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Heat Typhoon",
            game_text="Flip a coin for each Fire Energy attached to this Pok\u00e9mon. This attack does 50 more damage for each heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)