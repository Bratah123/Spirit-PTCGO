from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

_FURY_CUTTER_BONUS = {1: 20, 2: 70, 3: 140}


async def fury_cutter(ctx):
    results = await ctx.flip_coins(3, "Fury Cutter")
    heads = sum(1 for r in results if r)
    bonus = _FURY_CUTTER_BONUS.get(heads, 0)
    await ctx.deal_damage(ctx.ability.damage + bonus)

card = PokemonCardDef(
    guid="04d1750c-3ff7-58b0-bff6-08eb5fde6516",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Escavalier.Name",
    display_name="Escavalier",
    searchable_by=["Escavalier", "Stage 1", "Escavalier"],
    subtypes=["Stage 1"],
    collector_number=124,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    family_id=588,
    abilities=[
        Attack(
            title="Fury Cutter",
            game_text="Flip 3 coins. If 1 of them is heads, this attack does 20 more damage. If 2 of them are heads, this attack does 70 more damage. If all of them are heads, this attack does 140 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator="+",
            effect=fury_cutter,
        ),
        Attack(
            title="Seashell Attack",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)