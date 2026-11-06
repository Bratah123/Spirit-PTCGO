from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.attributes import (
    PokemonTypes, Rarities, SpecialConditions, TrainerType,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import TechnicalMachinePassive

_paralyzing_gaze = Attack(
    title="Paralyzing Gaze",
    game_text="The Defending Pokémon is now Paralyzed.",
    cost={PokemonTypes.COLORLESS: 1},
    damage=0,
    effect=condition_attack(SpecialConditions.PARALYZED),
)

card = TrainerCardDef(
    guid="66be2075-cf24-5927-8a3c-4417587c8c4c",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MultiTechnicalMachine01.Name",
    display_name="Multi Technical Machine 01",
    searchable_by=["Multi Technical Machine 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=144,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_paralyzing_gaze],
)
card.passive = TechnicalMachinePassive(_paralyzing_gaze)
