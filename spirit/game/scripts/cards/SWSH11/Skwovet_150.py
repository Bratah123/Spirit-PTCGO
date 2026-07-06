from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e1085652-99ab-5ccf-bbf7-2375ff570059",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    display_name="Skwovet",
    searchable_by=["Skwovet", "Basic", "Skwovet"],
    subtypes=["Basic"],
    collector_number=150,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=819,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)