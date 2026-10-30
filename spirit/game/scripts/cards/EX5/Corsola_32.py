"""STUB: effect not implemented — do not guess mechanics.
Corsola (EX5 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.ex import coral_glow

card = PokemonCardDef(
    guid="1a20ab39-996d-5deb-ba58-a705ddbb187f",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corsola.Name",
    display_name="Corsola",
    searchable_by=["Corsola", "Basic", "Corsola"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=222,
    abilities=[
        Attack(
            title="Coral Glow",
            game_text="Draw a number of cards up to the number of your opponent's Basic Pok\u00e9mon in play. (You can't have more than 10 cards in your hand in this way.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=coral_glow(),
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)