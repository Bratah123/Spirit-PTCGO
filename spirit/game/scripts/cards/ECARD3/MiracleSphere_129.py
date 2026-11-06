from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.card_effects.ecard import (
    TechnicalMachinePassive, evolved_of_types, fire_force,
)
from spirit.game.attributes import PokemonTypes, Rarities, TrainerType


_attack = Attack(
    title="Fire Force",
    game_text="If the Pokémon using this attack has Fire and Lightning basic Energy cards attached to it, the Defending Pokémon is now Confused. If the Pokémon using this attack has Fire and Fighting basic Energy cards attached to it, this attack does 30 damage plus 10 more damage and removes 3 damage counters from the Pokémon that Miracle Sphere α is attached to.",
    cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
    damage=30,
    damage_operator="+",
    effect=fire_force,
)

card = TrainerCardDef(
    guid="a3d4bb05-9af5-5fd7-b5e4-c5266ebf9123",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiracleSphere.Name",
    display_name="Miracle Sphere α",
    searchable_by=["Miracle Sphere \u03b1", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=129,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
card.attach_to = evolved_of_types(
    PokemonTypes.FIRE, PokemonTypes.LIGHTNING, PokemonTypes.FIGHTING)
