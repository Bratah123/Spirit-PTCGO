from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import mini_metronome, snivel


card = PokemonCardDef(
    guid="f4633f7b-246f-5a21-9508-24393e008d71",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    display_name="Togepi",
    searchable_by=["Togepi", "Basic", "Togepi"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=175,
    abilities=[
        Attack(
            title="Snivel",
            game_text="If the Defending Pok\u00e9mon attacks Togepi during your opponent's next turn, any damage done to Togepi is reduced by 20 (before applying Weakness and Resistance). (Benching either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=snivel,
        ),
        Attack(
            title="Mini-Metronome",
            game_text="Flip a coin. If heads, choose 1 of the Defending Pok\u00e9mon's attacks. Mini-Metronome copies that attack except for its Energy cost. (You must still do anything else in order to use that attack.) (No matter what type the Defending Pok\u00e9mon is, Togepi's type is still Colorless.) Togepi performs that attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=mini_metronome,
        ),
    ],
)
