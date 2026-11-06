from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.session.passives import carrier_pokemon
from spirit.game.models.board import EnergyEntity


def _no_energy(pokemon, carrier):
    """If this Pokemon has no Energy attached to it, it has no Retreat Cost."""
    return pokemon is carrier_pokemon(carrier) and not any(
        isinstance(c, EnergyEntity) for c in pokemon.children)


card = PokemonCardDef(
    guid="76171ee9-444f-55b9-be06-dba5a2558e64",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    display_name="Zubat",
    searchable_by=["Zubat", "Basic", "Zubat"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="BW8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=41,
    abilities=[
        Ability(
            title="Free Flight",
            game_text="If this Pok\u00e9mon has no Energy attached to it, this Pok\u00e9mon has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=retreat_free_when(_no_energy),
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)