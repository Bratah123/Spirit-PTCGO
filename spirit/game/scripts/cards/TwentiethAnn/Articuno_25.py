"""STUB: effect not implemented — do not guess mechanics.
Articuno (TwentiethAnn #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a0dd86c9-449d-5554-8b14-e1e61ef61764",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic", "Articuno"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=144,
    abilities=[
        Attack(
            title="Find Ice",
            game_text="Search your deck for up to 3 Water Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Freezing Wind",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)