from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="895c1576-4cee-5c73-a9a3-05d9c7fae233",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carkol.Name",
    display_name="Carkol",
    searchable_by=["Carkol", "Stage 1", "Carkol"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rolycoly.Name",
    family_id=837,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)