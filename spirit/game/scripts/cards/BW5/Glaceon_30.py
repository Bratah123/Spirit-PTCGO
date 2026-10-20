from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


async def shadow_cyclone(ctx):
    await ctx.deal_damage()
    await ctx.move_energy_freely([ctx.attacker], ctx.my_bench(), max_count=1)


card = PokemonCardDef(
    guid="5263f286-8b54-5a3a-935a-e3edbbd122ba",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glaceon.Name",
    display_name="Glaceon",
    searchable_by=["Glaceon", "Stage 1", "Glaceon"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
        Attack(
            title="Reflect Energy",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=shadow_cyclone,
        ),
    ],
)