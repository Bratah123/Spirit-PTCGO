from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.smp import shadowy_echoes


card = PokemonCardDef(
    guid="467af9c6-3ace-567d-a532-be88556ec559",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marshadow.Name",
    display_name="Marshadow",
    searchable_by=["Marshadow", "Basic", "Marshadow"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=802,
    abilities=[
        Attack(
            title="Shadowy Echoes",
            game_text="Put a Basic Pok\u00e9mon from each player's discard pile onto its owner's Bench.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=shadowy_echoes,
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=flip_or_nothing(),
        ),
    ],
)