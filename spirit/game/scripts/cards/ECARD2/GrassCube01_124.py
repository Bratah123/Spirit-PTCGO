from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.card_effects.ecard import TechnicalMachinePassive, pokemon_has_type
from spirit.game.attributes import PokemonTypes, Rarities, TrainerType
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions


_attack = Attack(
    title="Sleep Poison",
    game_text="The Defending Pokémon is now Asleep and Poisoned.",
    cost={PokemonTypes.GRASS: 1},
    damage=0,
    effect=condition_attack(SpecialConditions.ASLEEP, SpecialConditions.POISONED),
    )

card = TrainerCardDef(
    guid="a7ab2f81-e315-5718-8609-c1b3d67d6e68",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GrassCube01.Name",
    display_name="Grass Cube 01",
    searchable_by=["Grass Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=124,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
card.attach_to = lambda p, _t=PokemonTypes.GRASS: pokemon_has_type(p, _t)
