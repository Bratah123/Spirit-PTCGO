"""STUB: effect not implemented — do not guess mechanics.
Blastoise-EX (Promo_XY #XY30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="730c1c62-b926-54bc-aca7-c3d542a18bff",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseEX.Name",
    display_name="Blastoise-EX",
    searchable_by=["Blastoise-EX", "Basic", "EX", "BlastoiseEX"],
    subtypes=["Basic", "EX"],
    collector_number=30,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=9,
    abilities=[
        Attack(
            title="Rapid Spin",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. Then, your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Splash Bomb",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.WATER: 3},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)