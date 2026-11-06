from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, flip_damage


card = PokemonCardDef(
    guid="a37a1b12-3170-5745-91e7-940ae287810c",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhiteKyurem.Name",
    display_name="White Kyurem",
    searchable_by=["White Kyurem", "Basic", "WhiteKyurem"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DRAGON,
    family_id=646,
    abilities=[
        Attack(
            title="Damage Rush",
            game_text="Flip a coin until you get tails. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=20),
        ),
        Attack(
            title="Cold Fire",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=flip_bonus(40),
        ),
    ],
)