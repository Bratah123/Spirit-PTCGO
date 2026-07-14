from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_discard


def _is_leon(card):
    definition = def_for(card.archetype_id)
    return bool(definition) and getattr(definition, "display_name", "") == "Leon"


async def _battle_sense(ctx):
    if not await ctx.ask_yes_no("Look at the top 3 cards of your deck?"):
        return
    top = ctx.deck_top(3)
    if not top:
        return
    picks = await ctx.choose_cards(
        top, 1, minimum=1,
        prompt="Put 1 card into your hand. Discard the other cards.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    rest = [c for c in top if c not in picks]
    if rest:
        await ctx.discard_cards(rest)


card = PokemonCardDef(
    guid="b5b1a323-c6ec-5e9b-8867-be373de5a922",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=25,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Battle Sense",
            game_text="Once during your turn, you may look at the top 3 cards of your deck and put 1 of them into your hand. Discard the other cards.",
            activation=Activations.ONCE_PER_TURN,
            effect=_battle_sense,
        ),
        Attack(
            title="Royal Blaze",
            game_text="This attack does 50 more damage for each Leon card in your discard pile.",
            cost={PokemonTypes.FIRE: 2},
            damage=100,
            damage_operator="+",
            effect=damage_per(count_discard("mine", pred=_is_leon), 50, base=100),
        ),
    ],
)