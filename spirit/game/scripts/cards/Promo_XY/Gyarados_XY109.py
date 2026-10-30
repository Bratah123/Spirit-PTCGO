from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage, flip_damage, count_energy


card = PokemonCardDef(
    guid="2916ad73-6f9d-5ce5-9dbd-e012545dfe8a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=109,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Berserker Splash",
            game_text="This attack does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=spread_damage(10, side='both', also_base=True),
        ),
        Attack(
            title="Aqua Tail",
            game_text="Flip a coin for each Water Energy attached to this Pok\u00e9mon. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator="+",
            effect=flip_damage(coins_from=count_energy('self', energy_type=PokemonTypes.WATER), bonus_per_heads=30),
        ),
    ],
)