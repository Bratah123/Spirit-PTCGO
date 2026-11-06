from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="44d8914f-a9ef-5c01-87e2-e7712d657adc",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    display_name="Scraggy",
    searchable_by=["Scraggy", "Basic", "Scraggy"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=559,
    abilities=[
        Attack(
            title="Tail Rap",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(2, per_heads=20),
        ),
    ],
)