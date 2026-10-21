from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack


async def _jagged_fang(ctx):
    """100; discard an Energy from this Pokemon, then one from the opponent's Active."""
    await ctx.deal_damage()
    if ctx.attached_energies(ctx.attacker):
        await ctx.discard_energy_from(ctx.attacker, 1, minimum=1, prompt="Discard an Energy from this Pokémon")
    d = ctx.defender
    if d is not None and ctx.attached_energies(d) and not ctx.effects_blocked(d):
        await ctx.discard_energy_from(d, 1, minimum=1, prompt="Discard an Energy from the Defending Pokémon")


card = PokemonCardDef(
    guid="413be683-827b-52e1-8626-124a1eef5f58",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SharpedoEX.Name",
    display_name="Sharpedo-EX",
    searchable_by=["Sharpedo-EX", "Basic", "EX", "SharpedoEX"],
    subtypes=["Basic", "EX"],
    collector_number=152,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=319,
    abilities=[
        Attack(
            title="Hunt",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon. This attack does 30 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=gust_attack(damage_to_new_active=30),
        ),
        Attack(
            title="Jagged Fang",
            game_text="Discard an Energy attached to this Pok\u00e9mon. Then, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=_jagged_fang,
        ),
    ],
)