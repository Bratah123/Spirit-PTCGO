from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack


async def _power_pinch(ctx):
    """Flip 2 coins. For each heads, discard an Energy from the Defending Pokémon."""
    results = await ctx.flip_coins(2, "Power Pinch")
    heads = sum(1 for r in results if r)
    defender = ctx.defender
    if not heads or defender is None or ctx.effects_blocked(defender):
        return
    await ctx.discard_energy_from(
        defender, heads, prompt="Choose Energy to discard from the Defending Pokémon")


card = PokemonCardDef(
    guid="6f513721-8cb4-5951-9c5a-e622e7f9167a",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir",
    searchable_by=["Pinsir", "Basic", "Pinsir"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Power Pinch",
            game_text="Flip 2 coins. For each heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_power_pinch,
        ),
        Attack(
            title="Grip and Squeeze",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)