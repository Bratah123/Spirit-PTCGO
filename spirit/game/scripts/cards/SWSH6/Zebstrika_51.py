from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4a94074c-03f8-5607-9fab-39f665824742",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zebstrika.Name",
    display_name="Zebstrika",
    searchable_by=["Zebstrika", "Stage 1", "Rapid Strike", "Zebstrika"],
    subtypes=["Stage 1", "Rapid Strike"],
    collector_number=51,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    family_id=522,
    abilities=[
        Attack(
            title="Coordinated Bolt",
            game_text="If 1 of your other Rapid Strike Pok\u00e9mon used an attack during your last turn, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Spark Rush",
            game_text="Flip a coin until you get tails. This attack does 90 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)