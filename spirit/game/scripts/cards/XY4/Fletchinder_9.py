from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f213a0fd-48e4-5b46-9527-8117c43a461c",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    display_name="Fletchinder",
    searchable_by=["Fletchinder", "Stage 1", "Fletchinder"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)