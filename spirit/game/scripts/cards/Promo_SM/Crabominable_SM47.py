from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.sm3 import gutsy_hammer


card = PokemonCardDef(
    guid="0bb43b80-75a2-5586-a79b-b2d69f9ec1ee",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crabominable.Name",
    display_name="Crabominable",
    searchable_by=["Crabominable", "Stage 1", "Crabominable"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name",
    family_id=739,
    abilities=[
        Attack(
            title="Gutsy Hammer",
            game_text="This Pok\u00e9mon does 10 damage to itself for each damage counter on it.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=80,
            effect=gutsy_hammer,
        ),
        Attack(
            title="Double Stomp",
            game_text="Flip 2 coins. This attack does 40 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=80,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=40),
        ),
    ],
)
