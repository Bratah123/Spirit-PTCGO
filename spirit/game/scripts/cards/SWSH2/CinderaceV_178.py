from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="47f8f433-e678-5249-9378-924d1dd3764a",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CinderaceV.Name",
    display_name="Cinderace V",
    searchable_by=["Cinderace V", "Basic", "V", "CinderaceV"],
    subtypes=["Basic", "V"],
    collector_number=178,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=815,
    abilities=[
        Ability(
            title="Field Runner",
            game_text="If a Stadium is in play, this Pok\u00e9mon has no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Crimson Legs",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)