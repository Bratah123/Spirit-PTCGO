from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8ec29741-4d40-5971-b319-df414f489a47",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name",
    display_name="Vanilluxe",
    searchable_by=["Vanilluxe", "Stage 2", "Team Plasma", "Vanilluxe"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=29,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    family_id=582,
    abilities=[
        Attack(
            title="ChillMAX",
            game_text="Flip a coin for each Energy attached to this Pok\u00e9mon. This attack does 60 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Cold Breath",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)