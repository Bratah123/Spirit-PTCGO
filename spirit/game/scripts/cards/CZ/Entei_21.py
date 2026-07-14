from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.models.board import BoardState


def _has_fire_energy(pokemon, carrier):
    return pokemon is carrier and any(
        energy_provides_type(e, PokemonTypes.FIRE.value)
        for e in BoardState.attached_energies(pokemon)
    )


card = PokemonCardDef(
    guid="fae64169-d66c-5a75-a3ec-3aad1982f203",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic", "Entei"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="CZ",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Ability(
            title="Explosive Heat Dash",
            game_text="If this Pok\u00e9mon has any Fire Energy attached, it has no Retreat Cost.",
            passive=retreat_free_when(_has_fire_energy),
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)