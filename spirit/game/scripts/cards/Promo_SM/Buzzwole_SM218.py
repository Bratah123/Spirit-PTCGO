from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.sm12 import beast_boost_passive


card = PokemonCardDef(
    guid="e0144fb3-8739-5b2a-b914-eb5d0c1bb964",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Buzzwole.Name",
    display_name="Buzzwole",
    searchable_by=["Buzzwole", "Basic", "Ultra Beast", "Buzzwole"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=218,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=794,
    abilities=[
        Ability(
            title="Beast Boost",
            game_text="This Pok\u00e9mon's attacks do 20 more damage to your opponent's Active Pok\u00e9mon for each Prize card you have taken (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=beast_boost_passive,
        ),
        Attack(
            title="Touchdown",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=heal_attack(30),
        ),
    ],
)