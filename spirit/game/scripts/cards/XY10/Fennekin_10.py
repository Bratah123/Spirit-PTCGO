from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_defender_attacks


async def scarf_hold(ctx):
    """30 damage. Flip: heads, Defending Pokémon can't attack next turn."""
    await ctx.deal_damage()
    if (await ctx.flip_coins(1, ctx.ability.title))[0]:
        lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="8e0ab179-ad86-5b68-ad3b-e59105ebe22d",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name",
    display_name="Fennekin",
    searchable_by=["Fennekin", "Basic", "Fennekin"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="XY10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=653,
    abilities=[
        Attack(
            title="Will-O-Wisp",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Tail Whip",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=scarf_hold,
        ),
    ],
)