"""STUB: effect not implemented — do not guess mechanics.
Rayquaza (Promo_XY #XY64): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9f0d3144-cfb5-5310-b361-868f6c211953",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=384,
    abilities=[
        Ability(
            title="Ozone Wall",
            game_text="As long as this Pok\u00e9mon is on your Bench, prevent all damage done to this Pok\u00e9mon by attacks (both yours and your opponent's.)",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 3 cards of your deck.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)