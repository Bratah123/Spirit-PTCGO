from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


_FURY_CUTTER_BONUS = {1: 20, 2: 60, 3: 110}  # all heads: 120 total


async def _fury_cutter(ctx):
    results = await ctx.flip_coins(3, "Fury Cutter")
    heads = sum(1 for r in results if r)
    await ctx.deal_damage(ctx.ability.damage + _FURY_CUTTER_BONUS.get(heads, 0))


card = PokemonCardDef(
    guid="aa3df515-fef9-5416-8b65-c86f52df1d7e",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name",
    display_name="Parasect",
    searchable_by=["Parasect", "Stage 1", "Parasect"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SM1",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    family_id=46,
    abilities=[
        Attack(
            title="Fury Cutter",
            game_text="Flip 3 coins. If 1 of them is heads, this attack does 20 more damage. If 2 of them are heads, this attack does 60 more damage. If all of them are heads, this attack does 120 damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=_fury_cutter,
        ),
        Attack(
            title="Mushroom Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=heal_attack(30),
        ),
    ],
)