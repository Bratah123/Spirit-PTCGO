from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="456792c8-64cd-5682-91be-3f7bb6ab887e",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesVoltorb.Name",
    display_name="Lt. Surge's Voltorb",
    searchable_by=["Lt. Surge's Voltorb", "Basic", "LtSurgesVoltorb"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=100,
    abilities=[
        Attack(
            title="Spin Ball",
            game_text="Flip 1 coin. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=1, per_heads=20),
        ),
        Attack(
            title="Double Spin",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=20),
        ),
    ],
)
