from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


async def nurturing(ctx):
    """Choose 1 of your Pokémon; search deck for a card that evolves from it
    and evolve; shuffle afterward."""
    candidates = ctx.my_pokemon_in_play()
    if not candidates:
        return
    targets = await ctx.choose_cards(
        candidates, 1,
        prompt="Choose 1 of your Pokémon.",
    )
    if not targets:
        return
    target = targets[0]
    logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if logic_name:
        picks = await ctx.search_deck(
            lambda c, name=logic_name: (
                c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name
            ),
            count=1, minimum=0,
            prompt="Choose a card that evolves from that Pokémon.",
        )
        if picks:
            await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="643fe14e-d600-5a3a-84f7-8360d09515d5",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leavanny.Name",
    display_name="Leavanny",
    searchable_by=["Leavanny", "Stage 2", "Leavanny"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name",
    family_id=540,
    abilities=[
        Attack(
            title="Nurturing",
            game_text="Choose 1 of your Pok\u00e9mon. Search your deck for a card that evolves from that Pok\u00e9mon and put it onto that Pok\u00e9mon. (This counts as evolving that Pok\u00e9mon.) Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=nurturing,
        ),
        Attack(
            title="X-Scissor",
            game_text="Flip a coin. If heads, this attack does 50 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(50),
        ),
    ],
)
