from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def touch_of_happiness(ctx):
    """On play from hand to Bench: you may heal 10 damage from your Active Pokémon."""
    active = ctx.my_active()
    if active is None:
        return
    if await ctx.ask_yes_no("Heal 10 damage from your Active Pokémon?"):
        await ctx.heal(10, active)

card = PokemonCardDef(
    guid="7b844792-7fb1-5bea-838c-34688347d4a1",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    display_name="Togepi",
    searchable_by=["Togepi", "Basic", "Togepi"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=175,
    abilities=[
        Ability(
            title="Touch of Happiness",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may heal 10 damage from your Active Pok\u00e9mon.",
            trigger=Triggers.ON_PLAY,
            effect=touch_of_happiness,
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)