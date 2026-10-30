from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import flashing_eyes


card = PokemonCardDef(
    guid="3b3c85b5-4735-54d0-b45b-c828b757251a",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningNoctowl.Name",
    display_name="Shining Noctowl",
    searchable_by=["Shining Noctowl", "Basic", "ShiningNoctowl"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="NEO4",
    rarity=Rarities.Shining,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=164,
    abilities=[
        Attack(
            title="Flashing Eyes",
            game_text="Flip 3 coins. If exactly 1 is heads, the Defending Pok\u00e9mon is now Asleep. If exactly 2 are heads, the Defending Pok\u00e9mon is now Confused. If all 3 are heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flashing_eyes,
        ),
    ],
)
