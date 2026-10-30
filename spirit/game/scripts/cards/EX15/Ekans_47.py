from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fc0444bd-f5f2-52c6-86fe-08356cef2b53",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    display_name="Ekans δ",
    searchable_by=["Ekans \u03b4", "Basic", "Ekans"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=23,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Tail Snap",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)