from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="ddc407c6-833b-501a-b441-384fd3302fb3",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurEX.Name",
    display_name="Venusaur-EX",
    searchable_by=["Venusaur-EX", "Basic", "EX", "VenusaurEX"],
    subtypes=["Basic", "EX"],
    collector_number=123,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    family_id=3,
    abilities=[
        Attack(
            title="Poison Powder",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Jungle Hammer",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=heal_attack(30),
        ),
    ],
)