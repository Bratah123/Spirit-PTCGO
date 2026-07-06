from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e7302307-c6a3-5a2b-9054-3b3128f1fd6f",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalion.Name",
    display_name="Cobalion",
    searchable_by=["Cobalion", "Basic", "Cobalion"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=638,
    abilities=[
        Ability(
            title="Justified Law",
            game_text="Your Basic Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Darkness Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Follow-Up",
            game_text="Choose up to 2 of your Benched Pok\u00e9mon. For each of those Pok\u00e9mon, search your deck for a basic Energy card and attach it to that Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)