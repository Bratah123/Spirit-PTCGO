from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.passives_common import no_weakness_passive
from spirit.game.session.passives import carrier_pokemon
from spirit.game.card_effects.pokemon import energy_provides_type


def _psychic_attached(target, carrier):
    """If this Pokemon has any Psychic Energy attached, it has no Weakness."""
    return target is carrier_pokemon(carrier) and any(
        energy_provides_type(c, PokemonTypes.PSYCHIC.value) for c in target.children)


card = PokemonCardDef(
    guid="19992996-48af-5421-8fdf-7e4fb2b9b09e",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    display_name="Elgyem",
    searchable_by=["Elgyem", "Basic", "Elgyem"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=605,
    abilities=[
        Ability(
            title="Weak Barrier",
            game_text="If this Pok\u00e9mon has any Psychic Energy attached to it, this Pok\u00e9mon has no Weakness.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=no_weakness_passive(_psychic_attached),
        ),
        Attack(
            title="Quick Blow",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)