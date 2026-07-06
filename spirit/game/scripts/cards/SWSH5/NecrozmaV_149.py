from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2066b050-2649-53bd-8001-c8d968fcd9ec",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NecrozmaV.Name",
    display_name="Necrozma V",
    searchable_by=["Necrozma V", "Basic", "V", "NecrozmaV"],
    subtypes=["Basic", "V"],
    collector_number=149,
    set_code="SWSH5",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=800,
    abilities=[
        Attack(
            title="Prismatic Ray",
            game_text="This attack also does 20 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Special Laser",
            game_text="If this Pok\u00e9mon has any Special Energy attached, this attack does 120 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)