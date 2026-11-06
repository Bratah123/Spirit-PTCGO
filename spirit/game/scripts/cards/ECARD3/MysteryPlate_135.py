from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities, TrainerType
from spirit.game.card_effects.ecard import TechnicalMachinePassive, mystery_plate_gamma


_attack = Attack(
    title="Retro Cave",
    game_text="If your opponent has 5 or more Prizes, shuffle your hand into your deck and then draw 6 cards. If your opponent has exactly 2 Prizes, choose 1 of your opponent's Evolved Pokémon. Your opponent puts the top card on that Evolved Pokémon on the bottom of his or her deck. (This counts as devolving that Pokémon.)",
    cost={PokemonTypes.COLORLESS: 1},
    damage=0,
    effect=mystery_plate_gamma,
)

card = TrainerCardDef(
    guid="2df7341b-3e56-5074-bb39-e25cf8758790",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryPlate.Name",
    display_name="Mystery Plate γ",
    searchable_by=["Mystery Plate \u03b3", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=135,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
