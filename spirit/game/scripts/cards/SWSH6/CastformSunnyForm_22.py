from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bba38fdc-6da1-54d9-9aa0-68e8f324be68",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CastformSunnyForm.Name",
    display_name="Castform Sunny Form",
    searchable_by=["Castform Sunny Form", "Basic", "CastformSunnyForm"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    family_id=351,
    abilities=[
        Ability(
            title="Weather Reading",
            game_text="If you have 8 or more Stadium cards in your discard pile, ignore all Energy in this Pok\u00e9mon's attack costs.",
            effect=unimplemented,
        ),
        Attack(
            title="High-Pressure Blast",
            game_text="Discard a Stadium in play. If you can't, this attack does nothing.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)