from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="76c5e48a-6c73-52b1-a467-d21bacc80f2a",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    display_name="Nidorina",
    searchable_by=["Nidorina", "Stage 1", "Nidorina"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    family_id=29,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Strength",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)