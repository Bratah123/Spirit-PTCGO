from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.attacks_common import flip_damage, count_energy


card = PokemonCardDef(
    guid="a3ce752b-1669-5bdc-afca-79a8da8a9428",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlazikenEX.Name",
    display_name="Blaziken-EX",
    searchable_by=["Blaziken-EX", "Basic", "EX", "BlazikenEX"],
    subtypes=["Basic", "EX"],
    collector_number=54,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=257,
    abilities=[
        Attack(
            title="Fist of Focus",
            game_text="Attach an Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=attach_from_discard(),
        ),
        Attack(
            title="Flare Storm",
            game_text="Flip a coin for each Fire Energy attached to this Pok\u00e9mon. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=flip_damage(bonus_per_heads=20, coins_from=count_energy("self", energy_type=PokemonTypes.FIRE)),
        ),
    ],
)