from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, spread_damage


card = PokemonCardDef(
    guid="80ef77f5-88bc-5ae3-a798-233837671061",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=["Kyogre", "Basic", "Kyogre"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=382,
    abilities=[
        Attack(
            title="Spring Tides",
            game_text="Flip a coin until you get tails. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=30),
        ),
        Attack(
            title="Ocean Cyclone",
            game_text="This attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=spread_damage(10, also_base=True),
        ),
    ],
)