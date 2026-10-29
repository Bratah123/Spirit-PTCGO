from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="a9c98a31-4f44-58c1-8ec3-46ac398db226",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name",
    display_name="Druddigon",
    searchable_by=["Druddigon", "Basic", "Druddigon"],
    subtypes=["Basic"],
    collector_number=157,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=621,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. This attack does 30 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=gust_attack(damage_to_new_active=30),
        ),
        Attack(
            title="Dragon Tail",
            game_text="Flip 2 coins. This attack does 100 damage for each heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=100),
        ),
    ],
)