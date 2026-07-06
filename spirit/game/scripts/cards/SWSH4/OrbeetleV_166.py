from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4c4e0a56-b3ab-5e26-8f54-1d2d6cb78a1d",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OrbeetleV.Name",
    display_name="Orbeetle V",
    searchable_by=["Orbeetle V", "Basic", "V", "OrbeetleV"],
    subtypes=["Basic", "V"],
    collector_number=166,
    set_code="SWSH4",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=826,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Mysterious Wave",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)