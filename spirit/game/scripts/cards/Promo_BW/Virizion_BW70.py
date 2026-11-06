from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.passives_common import TypedDamageBoostPassive


card = PokemonCardDef(
    guid="2c5a5858-6077-53b0-9c04-1b7be4856ce6",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Virizion.Name",
    display_name="Virizion",
    searchable_by=["Virizion", "Basic", "Virizion"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=640,
    abilities=[
        Ability(
            title="Justified",
            game_text="Each of this Pok\u00e9mon's attacks does 50 more damage to Darkness Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=TypedDamageBoostPassive(PokemonTypes.DARKNESS, 50, to_active_only=False),
        ),
        Attack(
            title="Leaf Blade",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)