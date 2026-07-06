from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="de5cc39e-51d7-5249-bb10-e97dae23b065",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    display_name="Quilava",
    searchable_by=["Quilava", "Stage 1", "Quilava"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name",
    family_id=155,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Flare",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)