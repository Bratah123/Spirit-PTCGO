from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.session.passives import carrier_pokemon
from spirit.game.card_effects.pokemon import energy_provides_type


def _has_grass(pokemon, carrier):
    """If this Pokemon has any Grass Energy attached, it has no Retreat Cost."""
    return pokemon is carrier_pokemon(carrier) and any(
        energy_provides_type(c, PokemonTypes.GRASS.value) for c in pokemon.children)


card = PokemonCardDef(
    guid="8a2c8cea-36c4-5b14-b7f3-9470a41f2c77",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Serperior.Name",
    display_name="Serperior",
    searchable_by=["Serperior", "Stage 2", "Serperior"],
    subtypes=["Stage 2"],
    collector_number=118,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    family_id=495,
    abilities=[
        Ability(
            title="Royal Garden",
            game_text="If this Pok\u00e9mon has any Grass Energy attached to it, this Pok\u00e9mon has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=retreat_free_when(_has_grass),
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)