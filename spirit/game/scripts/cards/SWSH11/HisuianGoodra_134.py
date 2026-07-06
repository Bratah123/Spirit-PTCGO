from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a04130db-d9da-503c-af2c-e4ea5789030f",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGoodra.Name",
    display_name="Hisuian Goodra",
    searchable_by=["Hisuian Goodra", "Stage 2", "HisuianGoodra"],
    subtypes=["Stage 2"],
    collector_number=134,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSliggoo.Name",
    family_id=704,
    abilities=[
        Ability(
            title="Metal Lodging",
            game_text="Prevent all damage done to each of your Basic Pok\u00e9mon that has any Metal Energy attached by attacks from your opponent's Pok\u00e9mon V.",
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)