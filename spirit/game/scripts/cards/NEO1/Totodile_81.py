from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import cant_attack_this_pokemon


card = PokemonCardDef(
    guid="796b35ca-cf03-5b3f-9ab5-3adb33af6887",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    display_name="Totodile",
    searchable_by=["Totodile", "Basic", "Totodile"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=158,
    abilities=[
        Attack(
            title="Leer",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack Totodile during your opponent's next turn. (Benching or evolving either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cant_attack_this_pokemon,
        ),
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=10),
        ),
    ],
)
