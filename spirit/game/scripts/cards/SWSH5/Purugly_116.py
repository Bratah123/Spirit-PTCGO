from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="83cfecbd-ff00-52c6-96bc-a6a9f7394578",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Purugly.Name",
    display_name="Purugly",
    searchable_by=["Purugly", "Stage 1", "Purugly"],
    subtypes=["Stage 1"],
    collector_number=116,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Glameow.Name",
    family_id=431,
    abilities=[
        Attack(
            title="Caturday",
            game_text="Draw 3 cards. If you do, this Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
        ),
    ],
)