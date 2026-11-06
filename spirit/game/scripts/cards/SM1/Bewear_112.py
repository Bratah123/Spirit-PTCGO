from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack, recoil_attack


async def _giga_power(ctx):
    """80; you may do 40 more damage. If you do, 20 damage to itself."""
    if await ctx.ask_yes_no("Do 40 more damage (this Pokémon does 20 damage to itself)?"):
        await recoil_attack(20, damage=120)(ctx)
    else:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="a9852cbf-2e01-58f0-85a7-60d7e07b3703",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name",
    display_name="Bewear",
    searchable_by=["Bewear", "Stage 1", "Bewear"],
    subtypes=["Stage 1"],
    collector_number=112,
    set_code="SM1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    family_id=759,
    abilities=[
        Attack(
            title="Bear Hug",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Superpower",
            game_text="You may do 40 more damage. If you do, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=_giga_power,
        ),
    ],
)