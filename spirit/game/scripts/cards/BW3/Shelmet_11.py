from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import named_in_play


async def mysterious_evolution(ctx):
    """If Karrablast is in play, search deck for an evolution of this Pokémon."""
    if not named_in_play("Karrablast", side="both")(ctx):
        return
    logic_name = ctx.attacker.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not logic_name:
        return
    picks = await ctx.search_deck(
        lambda c, name=logic_name: (
            c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name
        ),
        count=1, minimum=0,
        prompt="Choose a card that evolves from this Pokémon.",
    )
    if picks:
        await ctx.evolve_pokemon(ctx.attacker, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="489f3fbd-b612-5b4a-9a1b-2d90187bd979",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    display_name="Shelmet",
    searchable_by=["Shelmet", "Basic", "Shelmet"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=616,
    abilities=[
        Attack(
            title="Mysterious Evolution",
            game_text="If Karrablast is in play, search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon. (This counts as evolving this Pok\u00e9mon.) Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mysterious_evolution,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
