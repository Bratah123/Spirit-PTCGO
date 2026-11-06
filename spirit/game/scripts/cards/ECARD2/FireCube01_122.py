from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.card_effects.ecard import TechnicalMachinePassive, pokemon_has_type
from spirit.game.attributes import PokemonTypes, Rarities, TrainerType
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions


_attack = Attack(
    title="Singe",
    game_text="The Defending Pokémon is now Burned.",
    cost={PokemonTypes.FIRE: 1},
    damage=0,
    effect=condition_attack(SpecialConditions.BURNED),
    )

card = TrainerCardDef(
    guid="61024ef9-d0d7-542b-8ef8-041f77f2d6da",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FireCube01.Name",
    display_name="Fire Cube 01",
    searchable_by=["Fire Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=122,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
card.attach_to = lambda p, _t=PokemonTypes.FIRE: pokemon_has_type(p, _t)
