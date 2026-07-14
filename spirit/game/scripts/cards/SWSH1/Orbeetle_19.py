from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per


async def bugs_radar(ctx):
    if not await ctx.ask_yes_no(
        "Look at the top 3 cards of your opponent's deck and put them back "
        "in any order?"
    ):
        return
    top = ctx.deck_top(3, ctx.opponent_id)
    if len(top) <= 1:
        return
    picked_ids = await ctx.session.prompt_card_chooser(
        ctx.player_id, ctx.source.entity_id, top, len(top), minimum=len(top),
        prompt="Put the cards back in any order.", ordered=True,
    )
    by_id = {c.entity_id: c for c in top}
    order = [by_id[i] for i in picked_ids if i in by_id]
    for card in top:
        if card not in order:
            order.append(card)
    deck = ctx.board.find_player_area(ctx.opponent_id, "deck")
    for card in order:
        deck.children.remove(card)
    for card in reversed(order):
        deck.children.append(card)


card = PokemonCardDef(
    guid="a3dc1dd1-a9fa-57e2-94dd-9186bf97ac4b",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orbeetle.Name",
    display_name="Orbeetle",
    searchable_by=["Orbeetle", "Stage 2", "Orbeetle"],
    subtypes=["Stage 2"],
    collector_number=19,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dottler.Name",
    family_id=824,
    abilities=[
        Ability(
            title="Bug's Radar",
            game_text="Once during your turn, you may look at the top 3 cards of your opponent's deck and put them back in any order.",
            activation=Activations.ONCE_PER_TURN,
            effect=bugs_radar,
        ),
        Attack(
            title="Brainwave",
            game_text="This attack does 30 more damage for each Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=damage_per(count_energy("self", energy_type=PokemonTypes.PSYCHIC), 30, base=90),
        ),
    ],
)