from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="edbf1497-983b-5d1d-9e31-d1dcc6722269",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name",
    display_name="Pansage",
    searchable_by=["Pansage", "Basic", "Pansage"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=511,
    abilities=[
        Attack(
            title="Bullet Seed",
            game_text="Flip 4 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(4, per_heads=10),
        ),
    ],
)