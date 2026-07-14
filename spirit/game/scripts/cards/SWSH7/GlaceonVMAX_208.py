from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.card_effects.pokemon import is_pokemon_vmax
from spirit.game.session.passives import carrier_pokemon


def _is_glaceon_vmax(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    return definition is not None and definition.display_name == "Glaceon VMAX"


CRYSTAL_VEIL_PASSIVE = prevent_damage_when(
    lambda calc, carrier: carrier_pokemon(carrier) is calc.target
    and is_pokemon_vmax(calc.attacker.archetype_id)
    and not _is_glaceon_vmax(calc.attacker)
)

card = PokemonCardDef(
    guid="1f989bbf-8fde-5e51-a5f4-67c18d056999",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonVMAX.Name",
    display_name="Glaceon VMAX",
    searchable_by=["Glaceon VMAX", "VMAX", "GlaceonVMAX"],
    subtypes=["VMAX"],
    collector_number=208,
    set_code="SWSH7",
    rarity=Rarities.RareRainbow,
    hp=310,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonV.Name",
    family_id=471,
    abilities=[
        Ability(
            title="Crystal Veil",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon VMAX, except any Glaceon VMAX.",
            passive=CRYSTAL_VEIL_PASSIVE,
        ),
        Attack(
            title="Max Icicle",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=snipe_attack(30, also_base=True),
        ),
    ],
)