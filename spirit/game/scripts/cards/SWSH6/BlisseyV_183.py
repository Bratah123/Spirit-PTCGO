from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy
from spirit.game.card_effects.pokemon import is_energy_card


async def natural_cure(ctx):
    """Whenever you attach an Energy card from your hand to this Pokémon, remove all Special Conditions from it."""
    if ctx.attaching_player_id != ctx.player_id or ctx.energy_receiver is not ctx.source:
        return
    await ctx.cure_all_conditions(ctx.source)


async def blissful_blast(ctx):
    """10, plus 30 more for each Energy attached to this Pokémon. If you did any damage, you may attach up to 3 Energy from your discard pile to this Pokémon."""
    amount = 10 + 30 * count_energy("self")(ctx)
    dealt = await ctx.deal_damage(amount)
    if dealt <= 0:
        return
    if not await ctx.ask_yes_no("Attach up to 3 Energy cards from your discard pile to this Pokémon?"):
        return
    energies = [c for c in ctx.discard_pile() if is_energy_card(c)]
    picks = await ctx.choose_cards(
        energies, 3, minimum=1,
        prompt="Choose up to 3 Energy cards to attach to this Pokémon.")
    for card in picks:
        await ctx.attach_energy(card, ctx.attacker)


card = PokemonCardDef(
    guid="431bd38a-b900-57f7-b9a5-bbb26630e66d",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlisseyV.Name",
    display_name="Blissey V",
    searchable_by=["Blissey V", "Basic", "V", "BlisseyV"],
    subtypes=["Basic", "V"],
    collector_number=183,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=250,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=242,
    abilities=[
        Ability(
            title="Natural Cure",
            game_text="Whenever you attach an Energy card from your hand to this Pok\u00e9mon, remove all Special Conditions from it.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=natural_cure,
        ),
        Attack(
            title="Blissful Blast",
            game_text="This attack does 30 more damage for each Energy attached to this Pok\u00e9mon. If you did any damage with this attack, you may attach up to 3 Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=blissful_blast,
        ),
    ],
)