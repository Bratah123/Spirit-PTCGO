from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.attacks_common import recoil_attack


async def _giga_power(ctx):
    """80; you may do 40 more damage. If you do, 20 damage to itself."""
    if await ctx.ask_yes_no("Do 40 more damage (this Pokémon does 20 damage to itself)?"):
        await recoil_attack(20, damage=120)(ctx)
    else:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="503bc313-ab46-5910-aeaf-bd1169307f10",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeracrossEX.Name",
    display_name="Heracross-EX",
    searchable_by=["Heracross-EX", "Basic", "EX", "HeracrossEX"],
    subtypes=["Basic", "EX"],
    collector_number=105,
    set_code="XY3",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Giga Power",
            game_text="You may do 40 more damage. If you do, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=_giga_power,
        ),
    ],
)