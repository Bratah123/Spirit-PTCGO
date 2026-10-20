"""STUB: effect not implemented — do not guess mechanics.
Mr. Mime (TwentiethAnn #52): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="90958556-9b46-5853-b9ca-ad96725df857",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=122,
    abilities=[
        Ability(
            title="Bench Barrier",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon by attacks.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Juggling",
            game_text="Flip 4 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)