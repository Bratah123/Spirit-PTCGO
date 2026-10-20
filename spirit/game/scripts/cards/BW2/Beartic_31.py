from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def superpower(ctx):
    """You may do 20 more damage; if you do, this Pokémon does 20 to itself."""
    if await ctx.ask_yes_no(
        "Do 20 more damage? If you do, this Pokémon does 20 damage to itself."
    ):
        await ctx.deal_damage(80)
        await ctx.deal_damage(20, target=ctx.attacker, apply_modifiers=False)
    else:
        await ctx.deal_damage(60)


card = PokemonCardDef(
    guid="f3a0b133-704b-5142-a78e-72b712c7beb2",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beartic.Name",
    display_name="Beartic",
    searchable_by=["Beartic", "Stage 1", "Beartic"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    family_id=613,
    abilities=[
        Attack(
            title="Icy Wind",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Superpower",
            game_text="You may do 20 more damage. If you do, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=superpower,
        ),
    ],
)
