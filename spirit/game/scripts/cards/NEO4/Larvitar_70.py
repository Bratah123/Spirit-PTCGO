from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import leer


card = PokemonCardDef(
    guid="9779c840-2ff4-57ce-965d-98ac9a53d359",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    display_name="Larvitar",
    searchable_by=["Larvitar", "Basic", "Larvitar"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=246,
    abilities=[
        Attack(
            title="Leer",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack during your opponent's next turn. (Benching or evolving either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=leer,
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
