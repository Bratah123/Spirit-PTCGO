from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f0346398-a7f0-56f1-a8f9-f1aa6a22cf88",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EnamorusV.Name",
    display_name="Enamorus V",
    searchable_by=["Enamorus V", "Basic", "V", "EnamorusV"],
    subtypes=["Basic", "V"],
    collector_number=178,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=905,
    abilities=[
        Ability(
            title="Guardian of Love",
            game_text="Prevent all effects of your opponent's Pok\u00e9mon's Abilities done to each of your Pok\u00e9mon that has any Psychic Energy attached, except any Enamorus V.",
            effect=unimplemented,
        ),
        Attack(
            title="Blossom Tail",
            game_text="Attach up to 2 basic Energy cards from your discard pile to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)