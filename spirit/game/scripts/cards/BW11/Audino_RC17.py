from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="3010a7b7-957a-5210-82f2-760ab191a3bd",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name",
    display_name="Audino",
    searchable_by=["Audino", "Basic", "Audino"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="BW11",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Attack(
            title="Relaxed Roll",
            game_text="Flip a coin until you get tails. This attack does 30 damage times the number heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=30),
        ),
    ],
)