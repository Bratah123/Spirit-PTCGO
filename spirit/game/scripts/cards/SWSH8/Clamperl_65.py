from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8ceabda3-917b-5ae1-ae2f-c6791fef3a94",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    display_name="Clamperl",
    searchable_by=["Clamperl", "Basic", "Fusion Strike", "Clamperl"],
    subtypes=["Basic", "Fusion Strike"],
    collector_number=65,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=366,
    abilities=[
        Attack(
            title="Bursting Bubble",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)