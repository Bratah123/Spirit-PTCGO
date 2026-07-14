from spirit.game.data_utils import ABILITIES_BY_ID, SupporterCardDef
from spirit.game.attributes import Rarities, AttrID
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.passives import ability_locked


def _additional_order_active(ctx):
    """Alcremie's Additional Order: while it's the Active, Café Master does
    not end the turn (an ability, so Path to the Peak-style locks apply)."""
    active = ctx.my_active()
    if active is None or ability_locked(ctx.board, active):
        return False
    for entry in active.get_attribute(AttrID.PIE_ABILITIES) or []:
        if not isinstance(entry, dict):
            continue
        ability = ABILITIES_BY_ID.get(entry.get("abilityID"))
        if ability is not None and ability.title == "Additional Order":
            return True
    return False


async def cafe_master(ctx):
    """Choose up to 3 Benched Pokemon; for each, search a different type of
    basic Energy card and attach it to that Pokemon. Shuffle. End the turn."""
    bench = ctx.my_bench()
    targets = await ctx.choose_cards(
        bench, 3, minimum=0, prompt="Choose up to 3 of your Benched Pokémon.",
    ) if bench else []
    used_types = []
    for target in targets:
        snapshot = list(used_types)

        def _pred(card, _used=snapshot):
            types = card.get_attribute(AttrID.POKEMON_TYPES) or []
            return is_basic_energy_card(card) and bool(types) and types[0] not in _used

        picks = await ctx.search_deck(
            _pred, count=1, minimum=0,
            prompt="Choose a different type of basic Energy card to attach.",
        )
        if picks:
            energy = picks[0]
            await ctx.attach_energy(energy, target)
            types = energy.get_attribute(AttrID.POKEMON_TYPES) or []
            if types:
                used_types.append(types[0])
    await ctx.shuffle_deck()
    ctx.ends_turn = not _additional_order_active(ctx)


card = SupporterCardDef(
    guid="1c9c921d-ba43-52f9-aafd-3b1cbabf46a8",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CafMaster.Name",
    display_name="Café Master",
    searchable_by=["Café Master", "Cafe Master", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    effect=cafe_master
)
