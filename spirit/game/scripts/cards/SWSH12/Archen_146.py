from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4138182b-6e6d-5d91-9fc9-ff728367083f",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archen.Name",
    display_name="Archen",
    searchable_by=["Archen", "Stage 1", "Archen"],
    subtypes=["Stage 1"],
    collector_number=146,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name",
    family_id=566,
    abilities=[
        Attack(
            title="Flap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)