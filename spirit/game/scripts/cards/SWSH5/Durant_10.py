from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def devour(ctx):
    """For each of your Durant in play, discard the top card of your
    opponent's deck."""
    count = sum(
        1 for p in ctx.my_pokemon_in_play()
        if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Durant"
    )
    if count:
        await ctx.discard_cards(ctx.deck_top(count, player_id=ctx.opponent_id))

card = PokemonCardDef(
    guid="330eda35-2701-51b9-ab21-d990bb0f6db6",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic", "Durant"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=632,
    abilities=[
        Attack(
            title="Vise Grip",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Devour",
            game_text="For each of your Durant in play, discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=devour,
        ),
    ],
)