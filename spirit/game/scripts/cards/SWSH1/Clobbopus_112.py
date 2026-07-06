from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="97a4beeb-d5b7-524b-acf0-8354e8d48bbc",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    display_name="Clobbopus",
    searchable_by=["Clobbopus", "Basic", "Clobbopus"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=852,
    abilities=[
        Attack(
            title="Punch",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
        ),
    ],
)