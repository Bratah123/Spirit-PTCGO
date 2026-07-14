from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_special_energy


async def hack_off(ctx):
    """Discard a Pokémon Tool and a Special Energy from the opponent's Active."""
    await ctx.deal_damage()
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    tools = [t for t, p in ctx.tools_in_play() if p is target]
    if tools:
        await ctx.discard_cards(tools[:1])
    await ctx.discard_energy_from(
        target, 1, predicate=is_special_energy,
        prompt="Choose a Special Energy to discard from the Defending Pokémon")


card = PokemonCardDef(
    guid="4783dfac-25ae-5f0f-9813-0ac8c7ccf5c9",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScizorV.Name",
    display_name="Scizor V",
    searchable_by=["Scizor V", "Basic", "V", "ScizorV"],
    subtypes=["Basic", "V"],
    collector_number=183,
    set_code="SWSH3",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=212,
    abilities=[
        Attack(
            title="Hack Off",
            game_text="Discard a Pok\u00e9mon Tool and a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=hack_off,
        ),
        Attack(
            title="Slashing Claw",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)