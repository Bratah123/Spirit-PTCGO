from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.card_effects.ecard import TechnicalMachinePassive, pokemon_has_type
from spirit.game.attributes import AttrID, CardType, PokemonTypes, Rarities, TrainerType


async def plunder(ctx):
    """Before damage, discard Trainer cards attached to the Defending Pokémon."""
    defending = ctx.opponent_active()
    if defending is not None:
        trainers = [ch for ch in list(defending.children)
                    if ch.get_attribute(AttrID.CARD_TYPE) == CardType.TRAINER.value]
        if trainers:
            await ctx.discard_cards(trainers)
    await ctx.deal_damage()

_attack = Attack(
    title="Plunder",
    game_text="Before doing damage, discard any Trainer cards attached to the Defending Pokémon.",
    cost={PokemonTypes.DARKNESS: 1},
    damage=10,
    effect=plunder,
    )

card = TrainerCardDef(
    guid="ebdc4f65-897f-548f-9d54-8deab3d4aabc",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarknessCube01.Name",
    display_name="Darkness Cube 01",
    searchable_by=["Darkness Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=119,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
card.attach_to = lambda p, _t=PokemonTypes.DARKNESS: pokemon_has_type(p, _t)
