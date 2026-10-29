from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import attack_effect_shield_passive
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="3bae83c7-5b4d-57a0-ab30-3467901522a4",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name",
    display_name="Cosmog",
    searchable_by=["Cosmog", "Basic", "Cosmog"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=789,
    abilities=[
        Ability(
            title="Unaware",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=attack_effect_shield_passive(),
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=flip_or_nothing(),
        ),
    ],
)