from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="464d5255-c6c9-5647-8f79-434ec12eeb82",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistea.Name",
    display_name="Sinistea",
    searchable_by=["Sinistea", "Basic", "Sinistea"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=854,
    abilities=[
        Attack(
            title="Furtive Drop",
            game_text="Put 2 damage counters on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)