from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d1169a49-4ff4-567f-a285-893d22c0a060",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    display_name="Trapinch δ",
    searchable_by=["Trapinch \u03b4", "Basic", "Trapinch"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=328,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Dig",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)