from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import amnesia, lock_this_attack_on_flip


card = PokemonCardDef(
    guid="06d44465-a117-5a1f-a2f3-098161f9d803",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysPoliwag.Name",
    display_name="Misty's Poliwag",
    searchable_by=["Misty's Poliwag", "Basic", "MistysPoliwag"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=60,
    abilities=[
        Attack(
            title="Bubbles",
            game_text="Flip a coin. If tails, you can't use this attack during your next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=lock_this_attack_on_flip(heads=False),
        ),
        Attack(
            title="Amnesia",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 2},
            effect=amnesia,
        ),
    ],
)
