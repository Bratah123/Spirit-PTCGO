from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.card_effects.ecard import TechnicalMachinePassive, pokemon_has_type
from spirit.game.attributes import PokemonTypes, Rarities, TrainerType
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions


_attack = Attack(
    title="Psy Confuse",
    game_text="The Defending Pokémon is now Confused.",
    cost={PokemonTypes.PSYCHIC: 1},
    damage=0,
    effect=condition_attack(SpecialConditions.CONFUSED),
    )

card = TrainerCardDef(
    guid="864afb6b-aea4-595d-8320-b04e5990d7a5",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PsychicCube01.Name",
    display_name="Psychic Cube 01",
    searchable_by=["Psychic Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=132,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
card.attach_to = lambda p, _t=PokemonTypes.PSYCHIC: pokemon_has_type(p, _t)
