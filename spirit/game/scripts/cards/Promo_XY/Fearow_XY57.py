from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack, flip_damage


card = PokemonCardDef(
    guid="cb2115f7-2d0e-59ad-88f9-5e68ad26e0f2",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fearow.Name",
    display_name="Fearow",
    searchable_by=["Fearow", "Stage 1", "Fearow"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name",
    family_id=22,
    abilities=[
        Attack(
            title="Repeating Drill",
            game_text="Flip 5 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=5, per_heads=20),
        ),
        Attack(
            title="Nosedive",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=recoil_attack(20),
        ),
    ],
)