from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.models.board import BoardState


def _has_any_energy(pokemon, carrier):
    return pokemon is carrier and bool(BoardState.attached_energies(pokemon))


card = PokemonCardDef(
    guid="3cc16986-3a72-5156-9262-6ee2d092a4a1",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    display_name="Tynamo",
    searchable_by=["Tynamo", "Basic", "Tynamo"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=602,
    abilities=[
        Ability(
            title="Levitate",
            game_text="If this Pok\u00e9mon has any Energy attached, it has no Retreat Cost.",
            passive=retreat_free_when(_has_any_energy),
        ),
        Attack(
            title="Tiny Charge",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)