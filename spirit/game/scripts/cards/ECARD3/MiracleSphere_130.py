from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.card_effects.ecard import (
    TechnicalMachinePassive, evolved_of_types, freezing_force,
)
from spirit.game.attributes import PokemonTypes, Rarities, TrainerType


_attack = Attack(
    title="Freezing Force",
    game_text="If the Pokémon using this attack has Fire and Water basic Energy cards attached to it, this attack does 30 damage plus 10 more damage and the Defending Pokémon is now Burned. If the Pokémon using this attack has Water and Psychic basic Energy cards attached to it, choose an Energy card attached to the Defending Pokémon, if any, and your opponent shuffles that card into his or her deck.",
    cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
    damage=30,
    damage_operator="+",
    effect=freezing_force,
)

card = TrainerCardDef(
    guid="b3449b56-08c4-5ed5-b680-0d0609437ac7",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiracleSphere.Name",
    display_name="Miracle Sphere β",
    searchable_by=["Miracle Sphere \u03b2", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=130,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
card.attach_to = evolved_of_types(
    PokemonTypes.FIRE, PokemonTypes.WATER, PokemonTypes.PSYCHIC)
