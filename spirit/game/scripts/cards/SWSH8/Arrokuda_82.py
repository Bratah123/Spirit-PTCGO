from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="682b7068-bf66-5097-9f86-a5ecc3f8df7f",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arrokuda.Name",
    display_name="Arrokuda",
    searchable_by=["Arrokuda", "Basic", "Arrokuda"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=846,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)