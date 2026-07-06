from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7ce5897c-5258-5bc4-9bca-0e58f47b223d",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grapploct.Name",
    display_name="Grapploct",
    searchable_by=["Grapploct", "Stage 1", "Grapploct"],
    subtypes=["Stage 1"],
    collector_number=113,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    family_id=852,
    abilities=[
        Attack(
            title="Octolock",
            game_text="Until this Grapploct leaves the Active Spot, the Defending Pok\u00e9mon's attacks cost ColorlessColorless more, and the Defending Pok\u00e9mon can't retreat. This effect can't be applied more than once.",
            cost={PokemonTypes.FIGHTING: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Tough Swing",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)