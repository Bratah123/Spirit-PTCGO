from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="452c164c-1029-5c52-a72a-acf8401510dc",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine", "Basic", "Carnivine"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=455,
    abilities=[
        Attack(
            title="Lure Poison",
            game_text="Switch the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon. The new Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Spit Squall",
            game_text="Your opponent puts the Defending Pok\u00e9mon and all cards attached to it into his or her hand.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)