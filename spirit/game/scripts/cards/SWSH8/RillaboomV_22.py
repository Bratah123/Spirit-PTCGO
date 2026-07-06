from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c4b208b1-047b-5332-91ba-c99f7503ccec",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RillaboomV.Name",
    display_name="Rillaboom V",
    searchable_by=["Rillaboom V", "Basic", "V", "Rapid Strike", "RillaboomV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=22,
    set_code="SWSH8",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=812,
    abilities=[
        Attack(
            title="Drain Punch",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Drum Rush",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
        ),
    ],
)