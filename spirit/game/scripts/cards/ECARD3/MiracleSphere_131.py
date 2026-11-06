from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.card_effects.ecard import (
    TechnicalMachinePassive, evolved_of_types, thunder_force,
)
from spirit.game.attributes import PokemonTypes, Rarities, TrainerType


_attack = Attack(
    title="Thunder Force",
    game_text="If the Pokémon using this attack has Grass and Lightning basic Energy cards attached to it, the Defending Pokémon is now Poisoned and Asleep. If the Pokémon using this attack has Water and Lightning basic Energy cards attached to it, this attack does 30 damage plus 10 more damage and lets you put 1 damage counter on each of your opponent's Benched Pokémon.",
    cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
    damage=30,
    damage_operator="+",
    effect=thunder_force,
)

card = TrainerCardDef(
    guid="3ffafd21-663f-59fb-b757-499119bed57a",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiracleSphere.Name",
    display_name="Miracle Sphere γ",
    searchable_by=["Miracle Sphere \u03b3", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=131,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
card.attach_to = evolved_of_types(
    PokemonTypes.GRASS, PokemonTypes.WATER, PokemonTypes.LIGHTNING)
