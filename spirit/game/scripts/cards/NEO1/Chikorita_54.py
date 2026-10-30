from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import growl


card = PokemonCardDef(
    guid="eb51c94d-4ab4-5d2c-8f62-411dff2cc2cf",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name",
    display_name="Chikorita",
    searchable_by=["Chikorita", "Basic", "Chikorita"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=152,
    abilities=[
        Attack(
            title="Growl",
            game_text="If the Defending Pok\u00e9mon attacks Chikorita during your opponent's next turn, any damage done to Chikorita is reduced by 10 (before applying Weakness and Resistance). (Benching or evolving either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=growl,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
