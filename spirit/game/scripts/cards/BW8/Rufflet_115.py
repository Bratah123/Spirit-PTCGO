from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="d516bb27-1ed0-5413-aa4e-56ac77e4b013",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    display_name="Rufflet",
    searchable_by=["Rufflet", "Basic", "Rufflet"],
    subtypes=["Basic"],
    collector_number=115,
    set_code="BW8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=627,
    abilities=[
        Attack(
            title="Incessant Peck",
            game_text="Flip a coin until you get tails. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_damage(until_tails=True, bonus_per_heads=20),
        ),
    ],
)