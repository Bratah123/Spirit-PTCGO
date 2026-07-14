from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def bite_together(ctx):
    """30, +60 more if another Durant is on your Bench."""
    name = ctx.attacker.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    on_bench = any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == name for p in ctx.my_bench())
    await ctx.deal_damage(90 if on_bench else 30)

card = PokemonCardDef(
    guid="f1844eb9-f5db-5ff6-a7e2-a3bd202dfbcf",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic", "Durant"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=632,
    abilities=[
        Attack(
            title="Bite Together",
            game_text="If Durant is on your Bench, this attack does 60 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bite_together,
        ),
    ],
)