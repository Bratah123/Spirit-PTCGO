from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.sm5 import RotoMotorPassive

card = PokemonCardDef(
    guid="4ae9eab2-8bea-5bde-aa3e-9404c4b00d6b",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WashRotom.Name",
    display_name="Wash Rotom",
    searchable_by=["Wash Rotom", "Basic", "WashRotom"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=479,
    abilities=[
        Ability(
            title="Roto Motor",
            game_text="If you have 9 or more Pok\u00e9mon Tool cards in your discard pile, ignore all Energy in the attack cost of each of this Pok\u00e9mon's attacks.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=RotoMotorPassive(),
        ),
        Attack(
            title="Wash Arrow",
            game_text="This attack does 50 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(50, pool='bench', count=1),
        ),
    ],
)