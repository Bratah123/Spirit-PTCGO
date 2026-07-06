from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="19a60e2c-584e-5106-bbda-42b0070e9dd3",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HonchkrowV.Name",
    display_name="Honchkrow V",
    searchable_by=["Honchkrow V", "Basic", "V", "HonchkrowV"],
    subtypes=["Basic", "V"],
    collector_number=162,
    set_code="SWSH9",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=430,
    abilities=[
        Ability(
            title="Boss Pockets",
            game_text="This Pok\u00e9mon may have up to 4 Pok\u00e9mon Tools attached to it. If it loses this Ability, discard Pok\u00e9mon Tools from it until only 1 remains.",
            effect=unimplemented,
        ),
        Attack(
            title="Fearsome Shadow",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)