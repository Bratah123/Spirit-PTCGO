from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def surprise_short(ctx):
    """Discard all Pokémon Tools from all of your opponent's Pokémon."""
    tools = [t for t, p in ctx.tools_in_play()
             if p.owning_player_id == ctx.opponent_id and not ctx.effects_blocked(p)]
    if tools:
        await ctx.discard_cards(tools)


card = PokemonCardDef(
    guid="03a3bbcb-9d1c-532e-9244-f29fb483bd9c",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Attack(
            title="Surprise Short",
            game_text="Discard all Pok\u00e9mon Tools from all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=surprise_short,
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
    ],
)