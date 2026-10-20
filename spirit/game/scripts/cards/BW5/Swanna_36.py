from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0f84020f-c14e-5800-a59f-35112f495a02",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swanna.Name",
    display_name="Swanna",
    searchable_by=["Swanna", "Stage 1", "Swanna"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ducklett.Name",
    family_id=580,
    abilities=[
        Attack(
            title="Healing Dance",
            game_text="Heal 30 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Incessant Peck",
            game_text="Flip a coin until you get tails. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)