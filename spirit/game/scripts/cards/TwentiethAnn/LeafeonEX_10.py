from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


async def _stadium_drain(ctx):
    """30+. If any Stadium is in play: +30 damage and heal 30 from this Pokémon."""
    if ctx.stadium_in_play() is None:
        await ctx.deal_damage()
        return
    await ctx.deal_damage(60)
    await ctx.heal(30, ctx.attacker)


card = PokemonCardDef(
    guid="b9275f7e-1c43-5bc4-8250-a3b373d21b49",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonEX.Name",
    display_name="Leafeon-EX",
    searchable_by=["Leafeon-EX", "Basic", "EX", "LeafeonEX"],
    subtypes=["Basic", "EX"],
    collector_number=10,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=470,
    abilities=[
        Attack(
            title="Leaf Blade",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
        Attack(
            title="Nature's Breath",
            game_text="If there is any Stadium card in play, this attack does 30 more damage and heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=_stadium_drain,
        ),
    ],
)