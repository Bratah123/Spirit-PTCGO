"""STUB: effect not implemented — do not guess mechanics.
Klefki (XY3 #73): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="66a8f7cd-d636-5c03-a4d3-5fa56f54a569",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name",
    display_name="Klefki",
    searchable_by=["Klefki", "Basic", "Klefki"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=707,
    abilities=[
        Ability(
            title="Secret Key",
            game_text="Each of your Fairy Pok\u00e9mon's Resistance is now -40.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fairy Lock",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)