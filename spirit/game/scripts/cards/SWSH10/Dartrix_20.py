from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c0f846cb-87df-5e0f-9ac6-90b9dea7ebeb",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    display_name="Dartrix",
    searchable_by=["Dartrix", "Stage 1", "Dartrix"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name",
    family_id=722,
    abilities=[
        Attack(
            title="Flap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)