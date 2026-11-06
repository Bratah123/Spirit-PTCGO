from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import cant_attack_this_pokemon


card = PokemonCardDef(
    guid="9fcb5c26-89a1-5f00-8d2f-2cecc43bb8f7",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name",
    display_name="Scizor",
    searchable_by=["Scizor", "Stage 1", "Scizor"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Attack(
            title="Leer",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack Scizor during your opponent's next turn. (Benching either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cant_attack_this_pokemon,
        ),
        Attack(
            title="Metal Pincer",
            game_text="Flip a coin until you get tails. This attack does 30 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_damage(until_tails=True, bonus_per_heads=10),
        ),
    ],
)
