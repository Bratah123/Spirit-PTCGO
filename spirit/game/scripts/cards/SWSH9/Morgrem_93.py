from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="68694c53-b0ed-5bfc-9257-d4525d9b947d",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name",
    display_name="Morgrem",
    searchable_by=["Morgrem", "Stage 1", "Morgrem"],
    subtypes=["Stage 1"],
    collector_number=93,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Impidimp.Name",
    family_id=859,
    abilities=[
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)