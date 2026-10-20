from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def superpower(ctx):
    """You may do 20 more damage; if you do, this Pokémon does 20 to itself."""
    if await ctx.ask_yes_no(
        "Do 20 more damage? If you do, this Pokémon does 20 damage to itself."
    ):
        await ctx.deal_damage(90)
        await ctx.deal_damage(20, target=ctx.attacker, apply_modifiers=False)
    else:
        await ctx.deal_damage(70)


card = PokemonCardDef(
    guid="8dbc2a03-62b3-58be-9871-b87694c4e1a9",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Throh.Name",
    display_name="Throh",
    searchable_by=["Throh", "Basic", "Throh"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=538,
    abilities=[
        Attack(
            title="Squeeze",
            game_text="Flip a coin. If heads, this attack does 20 more damage and the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Superpower",
            game_text="You may do 20 more damage. If you do, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=superpower,
        ),
    ],
)