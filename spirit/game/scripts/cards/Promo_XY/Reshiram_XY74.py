from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="6f07689b-6395-5128-8385-d9a661444b8b",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reshiram.Name",
    display_name="Reshiram",
    searchable_by=["Reshiram", "Basic", "Reshiram"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Repeater Blaze",
            game_text="Flip a coin until you get tails. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=flip_damage(until_tails=True, bonus_per_heads=20),
        ),
    ],
)