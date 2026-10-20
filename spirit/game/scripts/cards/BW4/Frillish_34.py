from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="291aa293-ab8d-5d36-ac4b-29bb2b94fbcb",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    display_name="Frillish",
    searchable_by=["Frillish", "Basic", "Frillish"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=592,
    abilities=[
        Attack(
            title="Bubble",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Spit Poison",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)