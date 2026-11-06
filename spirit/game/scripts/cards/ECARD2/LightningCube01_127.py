from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.card_effects.ecard import TechnicalMachinePassive, pokemon_has_type
from spirit.game.attributes import AttrID, PokemonTypes, Rarities, TrainerType


async def discharge(ctx):
    """Discard all Lightning Energy; flip that many coins; 40x heads."""
    me = ctx.source
    lightning = []
    for ch in list(ctx.attached_energies(me)):
        types = ch.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.LIGHTNING.value in types:
            lightning.append(ch)
    if not lightning:
        return
    await ctx.discard_cards(lightning)
    results = await ctx.flip_coins(len(lightning), "Discharge")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.deal_damage(amount=40 * heads)

_attack = Attack(
    title="Discharge",
    game_text="Discard all Lightning Energy cards attached to this Pokémon. Then, flip a number of coins equal to the number of Energy cards discarded that way. This attack does 40 damage times the number of heads.",
    cost={PokemonTypes.LIGHTNING: 1},
    damage=0,
    effect=discharge,
    )

card = TrainerCardDef(
    guid="54711d47-a6a0-568e-9d1c-611671551d1c",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LightningCube01.Name",
    display_name="Lightning Cube 01",
    searchable_by=["Lightning Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=127,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
card.attach_to = lambda p, _t=PokemonTypes.LIGHTNING: pokemon_has_type(p, _t)
