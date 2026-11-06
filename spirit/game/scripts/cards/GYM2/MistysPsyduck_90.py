from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import mistys_esp


card = PokemonCardDef(
    guid="ae0a2be7-a475-5475-aa2a-d37dbe1682e2",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysPsyduck.Name",
    display_name="Misty's Psyduck",
    searchable_by=["Misty's Psyduck", "Basic", "MistysPsyduck"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=54,
    abilities=[
        Attack(
            title="ESP",
            game_text="Flip 3 coins. If exactly 1 is heads, draw a card. If exactly 2 are heads, this attack does 20 damage. If all 3 are heads, choose 1 of the Defending Pok\u00e9mon's attacks. Misty's Psyduck copies that attack except for its Energy costs. (No matter what type the Defending Pok\u00e9mon is, Misty's Psyduck's type is still Water.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=mistys_esp,
        ),
    ],
)
