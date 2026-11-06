from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.card_effects.ecard import TechnicalMachinePassive, desert_burn
from spirit.game.attributes import PokemonTypes, Rarities, TrainerType


_attack = Attack(
    title="Desert Burn",
    game_text="If your opponent has 5 or more Prizes, search your deck for a Trainer card, show it to your opponent, and put it into your hand. If your opponent has only 1 Prize, the Defending Pokémon is now Burned, Paralyzed, and Poisoned.",
    cost={PokemonTypes.COLORLESS: 1},
    effect=desert_burn,
)

card = TrainerCardDef(
    guid="515fe3e5-53e1-55f4-a1f8-bd47e4158edd",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryPlate.Name",
    display_name="Mystery Plate α",
    searchable_by=["Mystery Plate \u03b1", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=133,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
