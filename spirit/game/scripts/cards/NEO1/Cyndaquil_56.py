from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import cant_attack_this_pokemon, swift


card = PokemonCardDef(
    guid="246fb783-1f4e-59f1-b144-9608ec3d49b8",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name",
    display_name="Cyndaquil",
    searchable_by=["Cyndaquil", "Basic", "Cyndaquil"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=155,
    abilities=[
        Attack(
            title="Leer",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack Cyndaquil during your opponent's next turn. (Benching or evolving either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cant_attack_this_pokemon,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9mon Powers, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=swift,
        ),
    ],
)
