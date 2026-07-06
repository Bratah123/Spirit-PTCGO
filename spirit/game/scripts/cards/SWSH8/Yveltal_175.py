from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="79b0f864-4102-54b3-bfb5-46f7ff973a00",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name",
    display_name="Yveltal",
    searchable_by=["Yveltal", "Basic", "Single Strike", "Yveltal"],
    subtypes=["Basic", "Single Strike"],
    collector_number=175,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=717,
    abilities=[
        Attack(
            title="Dark Cutter",
            cost={PokemonTypes.DARKNESS: 2},
            damage=50,
        ),
        Attack(
            title="Single Strike Wings",
            cost={PokemonTypes.DARKNESS: 3},
            damage=110,
        ),
    ],
)