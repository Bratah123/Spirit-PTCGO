from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy


async def frontier_road(ctx):
    """Once per turn, on move to Active: you may move any amount of Energy
    from your other Pokemon to it."""
    if not await ctx.ask_yes_no(
        "Move any amount of Energy from your other Pokémon to this Pokémon?"
    ):
        return
    sources = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
    if not sources:
        return
    await ctx.move_energy_freely(
        sources, [ctx.source], prompt="Choose an Energy to move")


card = PokemonCardDef(
    guid="1128014f-5fb1-51ad-a978-499755b49fcd",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WyrdeerV.Name",
    display_name="Wyrdeer V",
    searchable_by=["Wyrdeer V", "Basic", "V", "WyrdeerV"],
    subtypes=["Basic", "V"],
    collector_number=134,
    set_code="SWSH10",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=899,
    abilities=[
        Ability(
            title="Frontier Road",
            game_text="Once during your turn, when this Pokémon moves from your Bench to the Active Spot, you may move any amount of Energy from your other Pokémon to it.",
            trigger=Triggers.ON_MOVE_TO_ACTIVE,
            effect=frontier_road,
        ),
        Attack(
            title="Psyshield Bash",
            game_text="This attack does 40 damage for each Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="x",
            effect=damage_per(count_energy("self"), 40),
        ),
    ],
)
