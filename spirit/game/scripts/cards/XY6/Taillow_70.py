from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="a33c45f3-4284-54b0-900b-e7dd54cfda30",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name",
    display_name="Taillow",
    searchable_by=["Taillow", "Basic", "Taillow"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="XY6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=276,
    abilities=[
        Attack(
            title="Double Peck",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=10),
        ),
    ],
)