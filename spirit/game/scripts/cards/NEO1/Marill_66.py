from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection
from spirit.game.card_effects.ecard import paralyze_or_recoil


card = PokemonCardDef(
    guid="7759dcf0-ceef-5275-9036-07d7157bfbbb",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    display_name="Marill",
    searchable_by=["Marill", "Basic", "Marill"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=183,
    abilities=[
        Attack(
            title="Defense Curl",
            game_text="Flip a coin. If heads, prevent all damage done to Marill during your opponent's next turn. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_protection(prevent=True),
        ),
        Attack(
            title="Bubble Bomb",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, Marill does 10 damage to itself.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=paralyze_or_recoil(10),
        ),
    ],
)
