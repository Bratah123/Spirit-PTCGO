from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e7c90e6e-d02d-570f-95ee-0b0688f0837a",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagearnaV.Name",
    display_name="Magearna V",
    searchable_by=["Magearna V", "Basic", "V", "MagearnaV"],
    subtypes=["Basic", "V"],
    collector_number=182,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=801,
    abilities=[
        Attack(
            title="Gear Throw",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Special Laser",
            game_text="If this Pok\u00e9mon has any Special Energy attached, this attack does 120 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)