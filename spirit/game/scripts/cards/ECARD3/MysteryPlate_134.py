from spirit.game.data_utils import TrainerCardDef, Attack
from spirit.game.attributes import PokemonTypes, Rarities, TrainerType
from spirit.game.card_effects.ecard import TechnicalMachinePassive, mystery_plate_beta


_attack = Attack(
    title="Stone Crush",
    game_text="If your opponent has 5 or more Prizes, draw 3 cards. If your opponent has only 1 Prize, choose 2 Energy cards attached to the Defending Pokémon (1 if there is only 1). Your opponent shuffles those cards into his or her deck.",
    cost={PokemonTypes.COLORLESS: 1},
    damage=0,
    effect=mystery_plate_beta,
)

card = TrainerCardDef(
    guid="476b9808-6971-5be2-ad19-73e228ec2598",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryPlate.Name",
    display_name="Mystery Plate β",
    searchable_by=["Mystery Plate \u03b2", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=134,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    abilities=[_attack],
)
card.passive = TechnicalMachinePassive(_attack)
