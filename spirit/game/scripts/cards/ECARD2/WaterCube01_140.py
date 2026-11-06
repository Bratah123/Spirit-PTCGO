from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.card_effects.ecard import TechnicalMachinePassive, pokemon_has_type
from spirit.game.attributes import PokemonTypes, Rarities, TrainerType
from spirit.game.card_effects.attacks_common import snipe_attack


_attack = Attack(
    title="Splatter",
    game_text="Choose 1 of your opponent's Pokémon. This attack does 20 damage to that Pokémon. Don't apply Weakness or Resistance.",
    cost={PokemonTypes.WATER: 1},
    damage=0,
    effect=snipe_attack(20, pool="any", apply_modifiers=False),
    )

card = TrainerCardDef(
    guid="acac7eec-f073-54fa-b4e7-67d254f65d31",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WaterCube01.Name",
    display_name="Water Cube 01",
    searchable_by=["Water Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=140,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
card.attach_to = lambda p, _t=PokemonTypes.WATER: pokemon_has_type(p, _t)
