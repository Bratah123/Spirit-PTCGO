from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="58f2bb40-3f3c-51af-b131-0e87c04e6d0d",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mienfoo.Name",
    display_name="Mienfoo",
    searchable_by=["Mienfoo", "Basic", "Mienfoo"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=619,
    abilities=[
        Attack(
            title="Chop",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Spiral Kick",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)