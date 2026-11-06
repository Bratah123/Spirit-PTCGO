from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_damage


async def _karate_chop(ctx):
    """80 damage minus 10 for each damage counter on this Pokemon."""
    me = ctx.attacker
    counters = max(0, ctx.max_hp(me) - me.get_attribute(AttrID.HP, 0)) // 10
    amount = 80 - 10 * counters
    if amount > 0:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="3839d1de-9217-5d12-bde9-dbed8bb22468",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    display_name="Primeape",
    searchable_by=["Primeape", "Stage 1", "Primeape"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="BW9",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=30),
        ),
        Attack(
            title="Karate Chop",
            game_text="Does 80 damage minus 10 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
            damage_operator="-",
            effect=_karate_chop,
        ),
    ],
)