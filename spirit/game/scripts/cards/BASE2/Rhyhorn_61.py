from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import cant_attack_this_pokemon


card = PokemonCardDef(
    guid="7e4a047e-ec9a-5abb-bcf1-bea0793bc6dc",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name",
    display_name="Rhyhorn",
    searchable_by=["Rhyhorn", "Basic", "Rhyhorn"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="BASE2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=111,
    abilities=[
        Attack(
            title="Leer",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack Rhyhorn during your opponent's next turn. (Benching either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cant_attack_this_pokemon,
        ),
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
