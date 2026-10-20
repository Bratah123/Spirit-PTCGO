from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.card_effects.attacks_common import flip_damage


def _yoga_guard_pred(calc, carrier):
    return calc.is_attack and calc.target is carrier and not calc.to_active


card = PokemonCardDef(
    guid="691c1480-4aa7-5c6f-9b25-24d84f79df91",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name",
    display_name="Carbink",
    searchable_by=["Carbink", "Basic", "Carbink"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="XY6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=703,
    abilities=[
        Ability(
            title="Jewel Armor",
            game_text="As long as this Pok\u00e9mon is on your Bench, prevent all damage done to this Pok\u00e9mon by attacks (both yours and your opponent's).",
            passive=prevent_damage_when(_yoga_guard_pred, attacks_only=False),
        ),
        Attack(
            title="Spin Tackle",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=flip_damage(tails_self_damage=20),
        ),
    ],
)