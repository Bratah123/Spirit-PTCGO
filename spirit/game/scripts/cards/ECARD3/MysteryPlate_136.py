from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities, TrainerType
from spirit.game.card_effects.ecard import TechnicalMachinePassive, mystery_plate_delta


_attack = Attack(
    title="Healing Oasis",
    game_text="If your opponent has 5 or more Prizes, search your deck for up to 3 basic Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward. If your opponent has exactly 2 Prizes, remove all damage counters from 1 of your Pokémon.",
    cost={PokemonTypes.COLORLESS: 1},
    damage=0,
    effect=mystery_plate_delta,
)

card = TrainerCardDef(
    guid="80309a3f-6cbc-5966-b3af-13753e616cdd",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryPlate.Name",
    display_name="Mystery Plate δ",
    searchable_by=["Mystery Plate \u03b4", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=136,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
